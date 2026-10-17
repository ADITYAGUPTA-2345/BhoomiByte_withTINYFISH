import re
import cv2
import numpy as np
from paddleocr import PaddleOCR

# 1. Known Agronomic Active Compounds & Fertilizer Registry
COMMON_AGRI_CHEMICALS = [
    # Fungicides & Bactericides
    "tricyclazole", "copper oxychloride", "streptocycline", "mancozeb",
    "propiconazole", "hexaconazole", "carbendazim", "kasugamycin",
    "isoprothiolane", "validamycin", "thifluzamide", "azoxystrobin",
    "tebuconazole", "chlorothalonil", "captan", "difenoconazole",
    # Insecticides
    "chlorpyrifos", "imidacloprid", "cartap hydrochloride", "fipronil",
    "lambda-cyhalothrin", "thiamethoxam", "acephate", "emamectin benzoate",
    # Fertilizers / Nutrients
    "urea", "diammonium phosphate", "dap", "muriate of potash", "mop",
    "zinc sulphate", "ferrous sulphate", "borax", "single super phosphate", "ssp",
    "nitrogen", "phosphorus", "potassium", "npk"
]

# Disease-to-Approved-Active-Formulations Matrix
DISEASE_CHEMICAL_REGISTRY = {
    "Blast": {
        "approved_actives": ["tricyclazole", "isoprothiolane", "kasugamycin", "edifenphos"],
        "standard_formulation": "Tricyclazole (75% WP) @ 0.6g/L"
    },
    "Bacterial_Blight": {
        "approved_actives": ["copper oxychloride", "streptocycline"],
        "standard_formulation": "Copper Oxychloride (50% WP) @ 2.5g/L or Streptocycline @ 1g/10L"
    },
    "Brown_Spot": {
        "approved_actives": ["mancozeb", "propiconazole", "carbendazim", "zineb"],
        "standard_formulation": "Mancozeb (75% WP) @ 2.0g/L"
    },
    "Sheath_Blight": {
        "approved_actives": ["propiconazole", "hexaconazole", "validamycin", "thifluzamide"],
        "standard_formulation": "Propiconazole (25% EC) @ 1.0ml/L"
    },
    "Leaf_Scald": {
        "approved_actives": ["hexaconazole", "carbendazim", "benomyl", "thiophanate-methyl"],
        "standard_formulation": "Hexaconazole (5% EC) @ 2.0ml/L"
    }
}

class ChemicalVerifier:
    def __init__(self, lang="en", use_gpu=False):
        """
        Initializes the offline PaddleOCR engine.
        `use_angle_cls=True` automatically handles upside-down or sideways bottle labels.
        """
        self.ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=use_gpu, show_log=False)

    def preprocess_messy_image(self, img):
        """
        Cleans field photos: removes color noise, fixes sun glare, and boosts text contrast.
        """
        # Convert to grayscale to remove distracting background colors
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
        # This equalizes lighting across shiny, curved cylindrical bottles
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        enhanced_gray = clahe.apply(gray)
        
        # Convert back to BGR format as PaddleOCR expects a 3-channel array
        enhanced_bgr = cv2.cvtColor(enhanced_gray, cv2.COLOR_GRAY2BGR)
        return enhanced_bgr

    def extract_label_text(self, image_input):
        """
        Applies OpenCV preprocessing, then runs OCR on the cleaned image array.
        """
        if isinstance(image_input, str):
            img = cv2.imread(image_input)
        else:
            img = image_input

        if img is None:
            raise ValueError("Unable to read image input. Verify the file path or image array.")

        # Apply the glare-reduction and contrast boost
        cleaned_img = self.preprocess_messy_image(img)

        # Run OCR on the enhanced image
        results = self.ocr.ocr(cleaned_img, cls=True)
        detected_lines = []

        if results and results[0] is not None:
            for box, (text, conf) in results[0]:
                if conf > 0.40:  # Filter out low-confidence OCR noise
                    detected_lines.append(text.strip())

        raw_text = " ".join(detected_lines).lower()
        return detected_lines, raw_text

    def parse_concentrations(self, text):
        """
        Extracts agricultural formulation codes and concentrations (e.g., 75% WP, 50% EC, 10% GR).
        """
        pattern = r"\b\d+(?:\.\d+)?\s*%\s*(?:wp|ec|sc|sp|gr|sl|wg|fs|w/w|w/v)?\b"
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        return [m.strip().upper() for m in set(matches)]

    def analyze_bottle(self, image_input, target_disease=None):
        """
        Complete verification pipeline matching detected compounds against protocols.
        """
        lines, clean_text = self.extract_label_text(image_input)
        concentrations = self.parse_concentrations(clean_text)

        # Detect any registered chemicals mentioned on the label
        detected_actives = []
        for chemical in COMMON_AGRI_CHEMICALS:
            if re.search(rf"\b{re.escape(chemical)}\b", clean_text):
                detected_actives.append(chemical.title())

        # Build output structure
        report = {
            "detected_actives": list(set(detected_actives)),
            "detected_formulations": concentrations,
            "raw_text_summary": clean_text[:300] + ("..." if len(clean_text) > 300 else ""),
            "verification_status": "UNVERIFIED",
            "message": "No active disease specified for comparative validation."
        }

        # If a target disease is provided, evaluate compatibility
        if target_disease:
            clean_disease = target_disease.strip()
            if clean_disease in DISEASE_CHEMICAL_REGISTRY:
                protocol = DISEASE_CHEMICAL_REGISTRY[clean_disease]
                approved_list = protocol["approved_actives"]
                
                matched = [c for c in detected_actives if c.lower() in approved_list]

                if matched:
                    report["verification_status"] = "VERIFIED_COMPATIBLE"
                    report["matched_chemical"] = matched[0]
                    report["message"] = (
                        f"Active ingredient '{matched[0]}' is clinically approved for {clean_disease.replace('_', ' ')}. "
                        f"Recommended dosage: {protocol['standard_formulation']}."
                    )
                else:
                    report["verification_status"] = "MISMATCH_ALERT"
                    report["message"] = (
                        f"Warning: Label does not contain recommended active compounds for {clean_disease.replace('_', ' ')}. "
                        f"Approved actives are: {', '.join([c.title() for c in approved_list])}."
                    )
            else:
                report["verification_status"] = "UNKNOWN_DISEASE"
                report["message"] = f"Disease '{clean_disease}' has no registered chemical protocol."

        return report