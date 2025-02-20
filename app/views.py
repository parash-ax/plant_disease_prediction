import numpy as np
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image # type: ignore
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Ensure index.html exists in 'templates' folder

# Load your trained Keras model
model_path = "app/models/plant_disease_prediction_model.h5"  # Adjust if needed
model = load_model(model_path)  # Load the model

# Define image processing (adjust based on model training)
def preprocess_image(img):
    img = img.resize((224, 224))  # Resize to match model input size
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0  # Normalize if required
    return img

@csrf_exempt  # Remove if CSRF token is properly handled
def analyze(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        img = Image.open(file).convert('RGB')  # Convert image to RGB
        img = preprocess_image(img)

        # Get model prediction
        prediction = model.predict(img)
        predicted_class = np.argmax(prediction, axis=1)[0]  # Get highest probability class index

        # Map class index to disease name (update based on your model's labels)
        class_labels = ['Apple___Apple_scab','Apple___Black_rot''Apple___Cedar_apple_rust','Apple___healthy','Blueberry___healthy','Cherry_(including_sour)___Powdery_mildew','Cherry_(including_sour)___healthy','Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Common_rust_','Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot','Grape___Esca_(Black_Measles)','Grape___Leaf_blight_(Isariopsis_Leaf_Spot)','Grape___healthy','Orange___Haunglongbing_(Citrus_greening)','Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot','Pepper,_bell___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy','Raspberry___healthy','Soybean___healthy', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']  # Adjust based on your model
        result = class_labels[predicted_class] if predicted_class < len(class_labels) else "Unknown"

        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request'}, status=400)
