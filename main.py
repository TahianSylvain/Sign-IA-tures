from reportlab.platypus import SimpleDocTemplate, Paragraph\
    , Image, SimpleDocTemplate
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch

""" New to download the Times-New-Roman.ttf
from reportlab.lib.fonts import ttfonts
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(ttfonts.TTFont(
    'Times-New-Roman', 'Times-New-Roman.ttf'))
"""


def generate_pdf(text):
    # Create a new PDF document
    doc = SimpleDocTemplate('output.pdf')

    # Create a paragraph style with Times New Roman font
    style = ParagraphStyle(name='TimesNewRoman',
                        #    fontName='Times-New-Roman',
                           fontSize=12)

    #Create an Img from the media/file
    image: any = object
    # image = Image('./lvlind10.png', x=200, y=500, width=200, height=200)

    # Create a paragraph with the text
    paragraph = Paragraph(text, style)

    # Add the paragraph to the document
    doc.build([paragraph, image])


if __name__ == '__main__':
    text = 'This is a test string in Times New Roman font.'
    generate_pdf(text)