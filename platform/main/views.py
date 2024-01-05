import io
from .models import FilesAdmin
from django.shortcuts import render


def home(request):
    return render(
        request, './dist/index.html',  # 'WaveWordANIMA.html', 
        {'files': "hello world"}, status=200 )
