# 🌱 Plant Disease Prediction

![Plant Disease Detection](https://www.letsnurture.com/wp-content/uploads/2021/02/Plant-disease-classifier-with-ai-blog-banner.jpg)

## 📌 About the Project
This project is a **Deep Learning-based Plant Disease Prediction System** that classifies plant leaf images into different disease categories. The model uses **Convolutional Neural Networks (CNNs)** trained on a dataset of plant leaf images to identify various diseases and provide possible remedies.

---

## 🚀 Features
✅ Upload an image of a plant leaf
✅ Get instant disease classification results
✅ Provides potential remedies for identified diseases
✅ Simple and user-friendly web interface using **Django**
✅ Uses **PyTorch (.pth model)** for inference

---

## 📂 Folder Structure
```bash
📦 plant_disease_prediction
 ┣ 📂 static
 ┃ ┗ 📂 images  # Contains UI assets
 ┣ 📂 templates  # HTML Files for UI
 ┣ 📂 prediction  # Model and inference code
 ┣ ┣ 📜 model.py  # CNN model structure
 ┣ ┣ 📜 predict.py  # Prediction logic
 ┣ ┣ 📜 plant_disease_model_1_latest.pth  # Trained model file
 ┣ 📜 app.py  # Flask/Django Backend
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 README.md  # This file
```

---

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/parash-ax/plant-disease-prediction.git
cd plant-disease-prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Web App
For **Django Users**:
```bash
python manage.py runserver
```

For **Flask Users**:
```bash
python app.py
```

The web app will run at **http://127.0.0.1:8000/** (Django) or **http://127.0.0.1:5000/** (Flask).

---

![Demo GIF](https://cainvas-static.s3.amazonaws.com/media/user_data/cainvas-admin/grape-_leaf.gif)


---

## 📌 Model Details
- **Architecture**: Convolutional Neural Network (CNN)
- **Framework**: PyTorch
- **Dataset**: PlantVillage Dataset
- **Accuracy**: ~97%

---

## 🤖 Technologies Used
- **Python**
- **Django / Flask**
- **PyTorch**
- **HTML, CSS, JavaScript**
- **Bootstrap**

---

## 🛠️ Troubleshooting
🔹 **Error: 'collections.OrderedDict' object has no attribute 'eval'**
   - Ensure that you are loading the model correctly:
   ```python
   model = CNN_Model()  # Initialize the model class
   model.load_state_dict(torch.load('plant_disease_model_1_latest.pth'))
   model.eval()
   ```

🔹 **ModuleNotFoundError: No module named 'keras.engine'**
   - If using a `.h5` Keras model, install dependencies:
   ```bash
   pip install keras tensorflow
   ```

---

## 👨‍💻 Author
🔹 **PARASHRAM A**  
🔹 [GitHub](https://github.com/parash-ax)  
🔹 [LinkedIn](https://linkedin.com/in/parash1310-a-)

---

## 📜 License
This project is licensed under the **MIT License**.

---

⭐ **If you like this project, don't forget to star the repo!** ⭐
