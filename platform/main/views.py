import io
# from .main import generate_sign
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import FilesAdmin
from django.http import FileResponse



def home(request):
    files = FilesAdmin.objects.all()  # .filter(owner=request.user.username)
    return render(request, 'WaveWordANIMA.html', {'files': files}, status=200)


# @login_required()
def booking(request, ):
    # model = main.generate_sign()
    # generate = model.predict()
    
    """buffer = io.BytesIO()
    p= canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world")
    p.showPage()
    p.save()
    buffer.seek(0)
    """
    filepath = FilesAdmin.objects.all()  # .filter(owner=request.user.username)
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf') #as_attachment=True, #buffer=io.BytesIO().seek(0),
                        #filename=file.name) # '/media/media/Mickas_CV.pdf')
    