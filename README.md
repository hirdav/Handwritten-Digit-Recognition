
# Handwritten Digit Recognition  

## Description  
This project trains and evaluates a deep learning model to recognize handwritten digits from custom image datasets. It supports training with user-supplied images, testing model accuracy, and predicting digits from images stored in a folder.  

## Tech Stack  
- **TensorFlow/Keras** – Model training and inference  
- **OpenCV** – Image processing  
- **NumPy** – Data manipulation  
- **Matplotlib** – Visualization (if needed)  

## Dataset  
- The dataset consists of handwritten digit images collected from various sources.  
- All training images should be placed in `handwritten_images/` before training.  

## Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/HANDWRITTEN_DIGIT_RECOGNITION.git  
   cd HANDWRITTEN_DIGIT_RECOGNITION  
   ```  

2. **Install dependencies**  
   ```bash
   pip install tensorflow numpy opencv-python matplotlib  
   ```  

## Usage  

### 1. Train the Model  
   Place all labeled handwritten digit images in `handwritten_images/` before running:  
   ```bash
   python train_model.py  
   ```  
   This will train the model on your dataset and save it as `mnist_model.h5`.  

### 2. Test the Model  
   ```bash
   python test_model.py  
   ```  
   This evaluates the trained model on a test dataset and logs accuracy.  

### 3. Predict Digits from Images  
   Ensure all handwritten images to be predicted are stored in `handwritten_images/`, then run:  
   ```bash
   python predict.py  
   ```  
   This script will predict digits for all PNG images in the folder and log results in `logs/predict.log`.  

### 4. Run All Steps in One Command  
   ```bash
   python main.py  
   ```  
   This executes training, testing, and prediction sequentially.  

## File Structure  
```
HANDWRITTEN_DIGIT_RECOGNITION/  
├── handwritten_images/      # Folder containing handwritten digit images  
├── logs/                    # Stores logs for training, testing, and predictions  
│   ├── predict.log  
│   ├── test.log  
│   └── train.log  
├── main.py                  # Runs training, testing, and prediction sequentially  
├── mnist_model.h5           # Trained model file  
├── predict.py               # Predicts digits from images in handwritten_images/  
├── test_model.py            # Evaluates the model accuracy  
├── train_model.py           # Trains the model using custom dataset  
└── README.md                # Project documentation  
```

## Logging  
- **Train logs**: `logs/train.log`  
- **Test logs**: `logs/test.log`  
- **Prediction logs**: `logs/predict.log` (with timestamps)  

## GitHub Setup  
To upload this project to GitHub:  

1. **Initialize a Git repository**  
   ```bash
   git init  
   ```  
2. **Add all files**  
   ```bash
   git add .  
   ```  
3. **Commit the changes**  
   ```bash
   git commit -m "Initial commit - Handwritten Digit Recognition"  
   ```  
4. **Create a repository on GitHub**  
5. **Link the local repo to GitHub**  
   ```bash
   git remote add origin https://github.com/your-username/HANDWRITTEN_DIGIT_RECOGNITION.git  
   ```  
6. **Push the code**  
   ```bash
   git push -u origin main  
   ```  

---
