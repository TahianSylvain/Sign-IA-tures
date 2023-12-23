import io
from .models import FilesAdmin
from django.shortcuts import render


def home(request):
    files = FilesAdmin.objects.all()  # .filter(owner=request.user.username)
    return render(
        request, './dist/index.html',  # 'WaveWordANIMA.html', 
        {'files': files}, status=200 )
