# 🌾 Crop Dekho
**Edge-Deployable Diagnostic Triage & Autonomous Agronomic Web Agent**

Built by **Team Code_care** · Bharati Vidyapeeth's College of Engineering (BVCOE)

---

## 📌 Problem Statement
Diagnosing a crop disease is only step zero. In real-world agriculture:
* Field experts and agronomists are rarely accessible in remote farming belts.
* Local treatment options, fungicide costs, and availability are fragmented across unstandardized vendor websites.
* Government relief schemes and crop insurance compensation portals involve complex, friction-heavy documentation.

Traditional CV apps end at a classification label. **Crop Dekho** bridges the gap from field-level diagnosis to real-world commercial and administrative action.

---

## 🚀 Solution: Tiered Inference & Action Architecture

### 1. Tier 1: The Offline Edge Engine (Default)
* **Backbone:** MobileNetV2 acts as a frozen feature extractor yielding a $1280$-dimensional continuous embedding space.
* **Classifier:** Non-linear Support Vector Machine (SVM) with an RBF kernel, maximizing decision boundaries between early-stage fungal lesions.
* **Performance:** Sub-50ms inference, ~14MB memory footprint, fully functional on entry-level Android devices without thermal throttling or cloud dependence.
* **Safety Net:** Top-3 confidence thresholding (60% gating cutoff) to flag visually ambiguous lesions for human review.

### 2. Tier 2: The Large Action Model (TinyFish Web Agent)
* **Market Sourcing:** Autonomous web agent navigates agri-commerce portals (e.g., BigHaat) in stealth mode to extract live pricing, packaging sizes, and availability for recommended active chemicals.
* **Administrative Form Assistance:** Pre-fills structured claim data into state crop-loss and insurance portals, enabling a rapid "review-and-sign" workflow for the farmer.
* **Resilient Fallback:** Implements regional proxy routing and local cache fallbacks to maintain utility under high-latency network conditions.

### 3. Explainable AI (Grad-CAM)
* Integrates Gradient-weighted Class Activation Mapping hooked to MobileNetV2's final convolutional layer (`out_relu`).
* Produces spatial heatmaps to visually verify that feature attention isolates necrotic margins rather than background soil or lighting artifacts.

---

## 🛠️ Tech Stack
* **Deep Learning & Computer Vision:** TensorFlow, Keras 3, OpenCV
* **Machine Learning & Pipeline:** Scikit-Learn (SVM), NumPy, Joblib
* **Web Automation / LAM:** TinyFish Python SDK
* **Visual Attribution:** Matplotlib, Grad-CAM

---

## 📂 Repository Structure

```text
├── Demo.ipynb                        # Master interactive evaluation & demo notebook
├── Training.ipynb                    # Baseline model training and feature extraction
├── rice_model_detect_diseases.keras  # Pre-trained MobileNetV2 feature backbone
├── crop_dekho_svm.pkl                # Trained RBF-kernel SVM classifier
├── requirements.txt                  # Environment dependencies
├── .gitignore                        # Git exclusion rules
└── README.md                         # Project documentation