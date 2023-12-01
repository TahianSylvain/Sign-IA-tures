import io
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import FilesAdmin
from django.http import FileResponse


def home(request):
    files = FilesAdmin.objects.all()  # .filter(owner=request.user.username)
    return render(request, 'index.html', {'files': files}, status=200)


"""from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch

def generate_pdf(text):
    # Create a new PDF document
    doc = SimpleDocTemplate('output.pdf')

    # Create a paragraph style with Times New Roman font
    style = ParagraphStyle(name='TimesNewRoman',
                           fontName='Times-New-Roman',
                           fontSize=12)

    # Create a paragraph with the text
    paragraph = Paragraph(text, style)

    # Add the paragraph to the document
    doc.build([paragraph])

if __name__ == '__main__':
    text = 'This is a test string in Times New Roman font.'
    generate_pdf(text)
"""

@login_required()
def booking(request, ):
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
    