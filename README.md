🌱 BhoomiByte
AI-Powered Rice Crop Support Platform
BhoomiByte is an agricultural support platform designed to help rice farmers identify possible leaf diseases and find practical, easy-to-understand guidance. The project connects crop disease detection with visual explanations and pesticide-label assistance, with a separate planned TinyFish module for online agricultural tasks.
Crop focus: Rice 🌾
💡 The Problem
Rice farmers may not have quick access to agricultural experts when crop diseases appear. Delayed identification can damage crops and reduce yields. Farmers may also struggle to understand pesticide labels, compare product information, or navigate agricultural support and crop-insurance processes.
🚀 Project Idea
BhoomiByte aims to turn a photo of a rice leaf into useful information. Rather than showing only a predicted disease name, the platform is designed to help farmers inspect the prediction and explore possible next steps.
Core Capabilities
- Rice leaf disease detection: Analyze a rice leaf image and predict a possible disease.
- Explainable results: Use Grad-CAM visualizations, where integrated, to highlight image regions that may influence a prediction.
- Pesticide-label assistance: Use OCR to read text on product labels and help compare the listed active ingredient with relevant guidance.
- Low-connectivity focus: Keep core image diagnosis separate from optional online services, supporting a workflow intended for areas with unreliable internet access.
🧠 Technical Approach
- MobileNetV2: Extract visual features from rice leaf images.
- RBF-SVM: Classify extracted image features to predict a possible disease.
- Grad-CAM: Provide a visual explanation of image regions that may have influenced a model prediction.
- OCR (for example, PaddleOCR where integrated): Read pesticide-label text for active-ingredient checks.
Core workflow: Rice leaf image → preprocessing → MobileNetV2 feature extraction → RBF-SVM classification → prediction and supporting guidance.
🐟 TinyFish Integration — Separate Planned Module
TinyFish is planned as an optional online web-agent module that operates after the core disease-detection workflow. It is intended to help farmers find information and prepare administrative paperwork without delaying local image analysis.
1. Agricultural Product and Market Discovery
- Search supported public agricultural e-commerce websites for products matching a relevant active ingredient.
- Gather available product details, pack sizes, listed prices, and availability when the websites expose that information.
- Present results for the farmer to compare; availability and prices may vary by location and time.
2. Crop-Insurance and Relief Form Assistance
- Help locate relevant public crop-insurance or agricultural relief portals.
- Use farmer-reviewed diagnostic and crop-loss details to prepare a draft or checklist of information needed for an application.
- Keep the farmer in control of personal data, document review, and final submission.
3. Proposed Workflow
1. The core model predicts a possible rice leaf disease.
2. If the farmer chooses online assistance, the application sends the relevant query to the TinyFish module.
3. TinyFish navigates supported websites and gathers available information.
4. BhoomiByte displays the findings or a draft for the farmer to review.
5. The farmer decides what to do next and approves any consequential action.
4. Integration Boundaries
- TinyFish requires an internet connection and compatible SDK configuration.
- It does not replace or perform the MobileNetV2 + RBF-SVM disease classification.
- Website layouts, access restrictions, and data availability may affect results.
- Product matches and prices must be verified before purchase or use.
- Form submission, purchases, or sharing personal information must not happen without the farmer's explicit review and authorization.
Status: TinyFish integration is planned; the features above should not be treated as available until implemented and tested.

🌾 Expected Impact
BhoomiByte aims to help farmers recognize potential crop problems earlier, better understand model results, investigate product information, and reduce friction when finding agricultural support resources.
🔭 Future Vision
The long-term vision is to develop BhoomiByte into a farmer-friendly rice crop support platform with stronger field validation, multilingual guidance, offline-friendly access, and carefully supervised TinyFish workflows for market research and draft relief-form assistance.
🛡️ Responsible Use
BhoomiByte is intended to support—not replace—professional agricultural advice. AI predictions can be incorrect, and OCR can misread labels. Farmers should confirm uncertain diagnoses with a qualified agricultural expert and follow official product labels and local regulations before applying pesticides.
BhoomiByte 🌱 — Smarter Rice Farming Through Machine Learning.
