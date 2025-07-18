
# 🧠 Brain Tumor Classification Using CNN

This project uses a Convolutional Neural Network (CNN) to classify brain MRI images into four categories: **Glioma**, **Meningioma**, **Pituitary Tumor**, and **No Tumor**.

## 📌 Overview

- Built with **TensorFlow/Keras** using custom CNN architecture.
- Applied **data augmentation** and **dropout** to improve generalization and reduce overfitting.
- Deployed using **Streamlit** for real-time predictions from user-uploaded MRI images.

## 📁 Dataset Structure

```
dataset/
├── train/
│   ├── glioma/
│   ├── meningioma/
│   ├── pituitary/
│   └── no_tumor/
└── test/
    ├── glioma/
    ├── meningioma/
    ├── pituitary/
    └── no_tumor/
```

## ⚙️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/brain-tumor-classification.git
   cd brain-tumor-classification
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional if `brain_tumor_multiclass_model.h5` is present):
   ```python
   python train_model.py
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 🖼️ Output Example

- **Input:** MRI scan image  
- **Output:** Predicted class: `Meningioma` (Confidence: 97%)

## 📌 Tech Stack

- Python, TensorFlow, Keras
- Streamlit (for UI)
- Matplotlib, NumPy

## 📬 Contact

**Your Name**  
GitHub: [github.com/yourusername](https://github.com/yourusername)  
Email: your.email@example.com
