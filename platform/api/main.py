import random
from reportlab.pdfbase import pdfmetrics, ttfonts

direct_path = '/home/tahiana/Documents/PY/IA/Sign-IA-tures/platform/api/'

def load_font_family():
    pdfmetrics.registerFont(ttfonts.TTFont(
        'Conquest',  
        direct_path + '/font/Conquest-8MxyM.ttf'   # chmod 777 access
        )
    )
    pdfmetrics.registerFont(ttfonts.TTFont(
        'WinterSong',
        direct_path + '/font/WinterSong-owRGB.ttf'
        )
    )
    pdfmetrics.registerFont(ttfonts.TTFont(
        'BeckyTahlia',
        direct_path + '/font/BeckyTahlia-MP6r.ttf'
        )
    )
    pdfmetrics.registerFont(ttfonts.TTFont(
        'BelieveIt',
        direct_path + '/font/BelieveIt-DvLE.ttf'
        )
    )
    pdfmetrics.registerFont(ttfonts.TTFont(
        'GloriousFree',
        direct_path + '/font/GloriousFree-dBR6.ttf'
        )
    )
    pdfmetrics.registerFont(ttfonts.TTFont(
        'Halimun',
        direct_path + '/font/Halimun-W7jn.ttf'
        )
    )
    
    
""" ####### Putting the IMAGE file ######## """ 
from reportlab.lib.colors import HexColor
from reportlab.pdfgen.canvas import Canvas


def draw_pdf(text, image_path):
    font_list: list[str] = [
        'Halimun',
        'Conquest',
        'WinterSong',
        'BeckyTahlia',
        'BelieveIt',
        'GloriousFree',
    ]
    
    canvas = Canvas(f'./static/{text}_output.pdf')
    """    (y=840)
            | 
            |
            |
            | [L]      [R]
            |
            |
    pdf ==> |_ _ _ _ _ _ _ _(x=590) 
    """
    
    """Add Top Right Item"""
    canvas.drawImage(image_path, x=390, y=640, width=200, height=200)
    unique_randomed_font: str = random.choice(font_list)
    print(unique_randomed_font)
    canvas.setFont(unique_randomed_font, 18)
    font_list.remove(unique_randomed_font) # unicity constraint
    canvas.drawString(470, 655, text)
    
    """Add  Top Left Item"""
    canvas.drawImage(image_path, x=0, y=640, width=200, height=200)
    unique_randomed_font: str = random.choice(font_list)
    print(unique_randomed_font)
    canvas.setFont(unique_randomed_font, 18)
    font_list.remove(unique_randomed_font) # unicity constraint
    canvas.drawString(50, 655, text)
    
    """Add  Center Right Item"""    
    canvas.drawImage(image_path, x=390, y=320, width=200, height=200)
    unique_randomed_font: str = random.choice(font_list)
    print(unique_randomed_font)
    canvas.setFont(unique_randomed_font, 18)
    font_list.remove(unique_randomed_font) # unicity constraint
    canvas.drawString(470, 320, text)
    
    """Add  Center Left Item"""    
    canvas.drawImage(image_path, x=0, y=320, width=200, height=200)
    unique_randomed_font: str = random.choice(font_list)
    print(unique_randomed_font)
    canvas.setFont(unique_randomed_font, 18)
    font_list.remove(unique_randomed_font) # unicity constraint
    canvas.drawString(50, 320, text)
    
    """Add  Bottom Left Item"""
    canvas.drawImage(image_path, x=0, y=0, width=200, height=200)
    unique_randomed_font: str = random.choice(font_list)
    print(unique_randomed_font)
    canvas.setFont(unique_randomed_font, 18)
    font_list.remove(unique_randomed_font) # unicity constraint
    canvas.drawString(50, 20, text)
    
    """Add  Bottom Right Item"""    
    canvas.drawImage(image_path, x=390, y=0, width=200, height=200)
    unique_randomed_font: str = random.choice(font_list)
    print(unique_randomed_font)
    canvas.setFont(unique_randomed_font, 18)
    font_list.remove(unique_randomed_font) # unicity constraint
    canvas.drawString(460, 20, text)
    
    canvas.save()


def main(text: str):    
    load_font_family()
    draw_pdf(text.capitalize(), image_path=direct_path+'/font/sign2.jpeg')
    return 'Generation done!'
        
main('TahianSylvain')
