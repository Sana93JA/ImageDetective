from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from .detection import Detection

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def detect(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        original_url, detected_url = Detection.detect(filename)
        return render(request, 'core/detect.html', {
            'original_file_url': original_url,
            'uploaded_file_url': detected_url
        })
    return render(request, 'core/detect.html')
