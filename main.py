from reportlab.platypus import SimpleDocTemplate, Paragraph
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