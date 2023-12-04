from reportlab.pdfbase import pdfmetrics, ttfonts


def load_font_family():
    pdfmetrics.registerFont(ttfonts.TTFont(
        'Conquest',  
        'font/Conquest-8MxyM.ttf'   # chmod 777 access
        )
    )
    pdfmetrics.registerFont(ttfonts.TTFont(
        'WinterSong',
        'font/WinterSong-owRGB.ttf'
        )
    )
    
    
""" ####### Putting the IMAGE file ######## """ 
from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas


def draw_pdf(text, image_path):
    canvas = Canvas('output.pdf')
    """    (y=840)
            | 
            |
            |
            |
            |
            |
    pdf ==> |_ _ _ _ _ _ _ _(x=590) 
    """
    
    """Add Top Right Item"""
    canvas.drawImage(image_path, x=390, y=640, width=200, height=200)
    # canvas.setFillColor(HexColor('#000000'))
    canvas.setFont('Conquest', 18)  # Helvetica
    canvas.drawString(470, 655, text)
    
    """Add  Top Left Item"""
    canvas.drawImage(image_path, x=0, y=640, width=200, height=200)
    canvas.setFont('WinterSong', 18)  #Helvetica
    canvas.drawString(50, 655, text)
    
    """Add  Center Right Item"""    
    canvas.drawImage(image_path, x=390, y=320, width=200, height=200)
    canvas.setFont('WinterSong', 18)  #Helvetica
    canvas.drawString(0, 220, text)
    
    """Add  Center Left Item"""    
    canvas.drawImage(image_path, x=0, y=320, width=200, height=200)
    canvas.setFont('WinterSong', 18)  #Helvetica
    canvas.drawString(0, 220, text)
    
    """Add  Bottom Right Item"""
    canvas.drawImage(image_path, x=0, y=0, width=200, height=200)
    canvas.setFont('WinterSong', 18)  #Helvetica
    canvas.drawString(50, 20, text)
    
    """Add  Bottom Right Item"""    
    canvas.drawImage(image_path, x=390, y=0, width=200, height=200)
    canvas.setFont('WinterSong', 18)  #Helvetica
    canvas.drawString(460, 20, text)
    
    canvas.save()



if __name__ == '__main__':
    text = 'MEOW'
    load_font_family()
    draw_pdf(text, image_path='sign2.jpeg')
    
