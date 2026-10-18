# 🌱 Crop_Dekho

### AI-Powered Rice Crop Support Platform

crop_dekho is an agricultural support platform designed to help rice farmers identify possible leaf diseases and find practical, easy-to-understand guidance. It combines machine-learning-based disease detection with visual explanations and pesticide-label assistance, with a separate planned TinyFish module for online agricultural tasks.

**Crop focus:** Rice 🌾

---

## 📌 Table of Contents

- [The Problem](#-the-problem)
- [Project Idea](#-project-idea)
- [Core Capabilities](#-core-capabilities)
- [Technical Approach](#-technical-approach)
- [TinyFish Integration](#-tinyfish-integration--planned-module)
- [Expected Impact](#-expected-impact)
- [Future Vision](#-future-vision)
- [Responsible Use](#-responsible-use)

## 💡 The Problem

Rice farmers may not have quick access to agricultural experts when crop diseases appear. Delayed identification can damage crops and reduce yields. Farmers may also struggle to understand pesticide labels, compare product information, or navigate agricultural support and crop-insurance processes.

A disease prediction alone may not provide enough help. Farmers also need understandable information to decide what to check or do next.

## 🚀 Project Idea

BhoomiByte aims to turn a photo of a rice leaf into useful, understandable information. Rather than showing only a predicted disease name, the platform is designed to help farmers inspect the prediction and explore possible next steps.

The core diagnosis workflow is intended to work separately from optional online services, supporting use in areas where internet connectivity may be unreliable.

## ✨ Core Capabilities

- **Rice leaf disease detection:** Analyze a rice leaf image and predict a possible disease.
- **Explainable results:** Use Grad-CAM visualizations, where integrated, to highlight image regions that may have influenced a prediction.
- **Pesticide-label assistance:** Use optical character recognition (OCR) to read text on product labels and help compare the listed active ingredient with relevant guidance.
- **Low-connectivity focus:** Keep core image diagnosis separate from optional online services so internet access is not required for every step of the intended workflow.

## 🧠 Technical Approach

- **MobileNetV2:** Extract visual features from rice leaf images.
- **RBF-SVM:** Classify the extracted features to predict a possible disease.
- **Grad-CAM:** Generate a visual explanation of image regions that may have influenced a model prediction.
- **OCR:** Read pesticide-label text to support active-ingredient checks. PaddleOCR may be used where it is integrated and configured.

**Core workflow:**

```text
Rice Leaf Image
      ↓
Image Preprocessing
      ↓
MobileNetV2 Feature Extraction
      ↓
RBF-SVM Classification
      ↓
Predicted Disease
      ↓
Prediction Review and Supporting Guidance
```

Grad-CAM and OCR are supporting modules and depend on their integration in the running application.

## 🐟 TinyFish Integration — Planned Module

TinyFish is planned as an optional, internet-connected web-agent module that operates downstream of the core disease-detection workflow. Its purpose is to help farmers discover agricultural product information and prepare information for relevant administrative processes, without delaying local image analysis.

### 1. Agricultural Product and Market Discovery

- Search supported public agricultural e-commerce websites for products matching a relevant active ingredient.
- Collect available product details, pack sizes, listed prices, and availability where the websites provide this information.
- Present the results for the farmer to compare, noting that prices and availability can vary by location and time.

### 2. Crop-Insurance and Relief Form Assistance

- Help locate relevant public crop-insurance or agricultural-relief portals.
- Use farmer-reviewed diagnostic and crop-loss details to prepare a draft or checklist of information needed for an application.
- Keep the farmer in control of personal information, document review, and final submission.

### 3. Proposed Workflow

```text
Core Disease Prediction
          ↓
Farmer Requests Online Assistance
          ↓
TinyFish Web Agent
          ↓
Supported Websites and Public Information
          ↓
Results or Draft Information in BhoomiByte
          ↓
Farmer Reviews and Decides Next Steps
```

### 4. Integration Boundaries

- TinyFish requires an internet connection and compatible SDK configuration.
- It does not replace or perform the MobileNetV2 + RBF-SVM disease classification.
- Website layouts, access restrictions, and data availability may affect results.
- Product matches and prices must be verified before purchase or use.
- Any form submission, purchase, or sharing of personal information must require the farmer's explicit review and authorization.

> **Status:** TinyFish integration is planned. These workflows should not be considered available until implemented and tested.

## 🌾 Expected Impact

BhoomiByte aims to help farmers:

- Recognize possible crop problems earlier.
- Better understand model predictions.
- Investigate agricultural product information.
- Find relevant agricultural support resources with less friction.

## 🔭 Future Vision

The long-term vision is to develop crop_dekho into a farmer-friendly rice crop support platform with:

- Stronger validation on real-world field images.
- Multilingual and accessible guidance.
- Offline-friendly access to core diagnostic features.
- Carefully supervised TinyFish workflows for market research and draft relief-form assistance.

## 🛡️ Responsible Use

crop_dekho is intended to support—not replace—professional agricultural advice.

- AI predictions can be incorrect, particularly when image quality is poor or field conditions differ from the training data.
- OCR can misread pesticide labels. Always verify product details against the official label.
- Confirm uncertain diagnoses with a qualified agricultural expert or local extension officer.
- Follow official product instructions and local regulations before applying pesticides.
- Keep farmers in control of their personal information and any consequential online action.

---

**BhoomiByte 🌱 — Smarter Rice Farming Through Machine Learning.**
