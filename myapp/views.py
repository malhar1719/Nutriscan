# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageUploadForm
from inference_sdk import InferenceHTTPClient

def scan_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded file to a temporary location
            uploaded_file = request.FILES['image']
            file_path = handle_uploaded_file(uploaded_file)

            # Call the InferenceHTTPClient with the file path
            CLIENT = InferenceHTTPClient(
                api_url="http://detect.roboflow.com",
                api_key="sAdRD9RvWmx3ozjS6U5r"
            )
            result = CLIENT.infer(file_path, model_id="nutriscan-final/2")

            # Process the result as needed
            return render(request, 'result.html', {'result': result})
    else:
        form = ImageUploadForm()
    return render(request, 'scan_image.html', {'form': form})

def handle_uploaded_file(uploaded_file):
    # Save the uploaded file to a temporary location
    file_path = 'temp_image.jpg'
    with open(file_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    return file_path
