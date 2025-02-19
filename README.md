🌿 Plant Disease Prediction 🔍
🚀 AI-powered web app to detect plant diseases from leaf images using Deep Learning (CNN) & Django
 --img

🏆 About the Project
Plant Disease Prediction is a deep learning-based web application designed to detect plant diseases from images of leaves. This tool helps farmers, researchers, and agriculturists by providing an AI-driven solution for identifying plant diseases early and taking preventive actions.

📸 Upload an image of a plant leaf
🔍 AI analyzes the image using a trained CNN model
📊 Instant results: Healthy or Diseased (with disease name)
🌍 Web-based solution powered by Django
🚀 Tech Stack
Component	Technology Used
Frontend	HTML, CSS, JavaScript
Backend	Django, Python
Deep Learning	PyTorch, CNN
Deployment	Django Web Framework
📂 Project Structure
php
Copy
Edit
📦 plant_disease_prediction
│── 📂 prediction            # Model and prediction logic
│   ├── model.py            # CNN model structure
│   ├── predict.py          # Image classification logic
│   ├── plant_disease_model.pt  # Pre-trained model file
│── 📂 static                # CSS, JS, and images
│── 📂 templates             # HTML templates
│── 📂 app                   # Django application
│   ├── views.py            # Handles requests and responses
│   ├── urls.py             # URL routing
│── manage.py                # Django entry point
│── requirements.txt         # Required dependencies
│── README.md                # Documentation
🌱 How It Works?
Upload an Image 📸
Select a plant leaf image from your device
AI Model Analyzes 🧠
The deep learning model (CNN) processes the image
Instant Results ⚡
Get a prediction: "Healthy" ✅ or "Diseased" ❌ with disease name
⚙️ Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/parash-ax/plant-disease-prediction.git
cd plant-disease-prediction
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run Django Server
bash
Copy
Edit
python manage.py runserver
4️⃣ Open the Web App
Open http://127.0.0.1:8000/ in your browser
🎯 Model Details
Convolutional Neural Network (CNN) Model:

Trained on plant leaf images 🌱
Multiple convolutional layers for feature extraction 🧠
Fully connected layers for classification 🎯
Prediction Classes:
✅ Healthy
❌ Diseased (E.g., Late Blight, Rust, etc.)

🖼️ Screenshots
(Add screenshots of your web app interface and model predictions here!)

📌 Future Enhancements
✅ Increase dataset size for better accuracy
✅ Support multiple plant species
✅ Deploy on cloud platforms (AWS, Heroku, etc.)
✅ Mobile App Integration

🤝 Contributions
👨‍💻 Contributions are welcome! If you’d like to improve the model or UI, feel free to:

Fork this repository
Create a new branch (feature-new)
Submit a pull request 🚀
⭐ Support & Credits
🌟 If you like this project, give it a star! ⭐
🙏 Thanks to deep learning & open-source datasets for making this project possible!
