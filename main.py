from datetime import datetime
from lingua import Language, LanguageDetectorBuilder
import PyPDF2
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import *
import gtts
from playsound import playsound
languages = [Language.ENGLISH, Language.UKRAINIAN, Language.RUSSIAN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
def open_file():
    name = askopenfilename()
    if name.split('.')[-1] == 'pdf':
        open_and_read_file(name)
    if name:
        line.delete(0.0, END)
        line.insert(0.0, name)


def open_and_read_file(path):
    file = open(path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(file)
    num_page = pdfReader.numPages
    for x in range(num_page):
        lang = 'en'
        date_string = datetime.now().strftime("%d%m%Y%H%M%S")
        page = pdfReader.getPage(x)
        lang_text = detector.detect_language_of(page.extractText())
        if lang_text == Language.UKRAINIAN:
            print('ua')
            lang = 'uk'
        elif lang_text == Language.ENGLISH:
            print('en')
            lang = 'en'
        elif lang_text == Language.RUSSIAN:
            print('ru')
            lang = 'ru'
        t1 = gtts.gTTS(page.extractText(), lang=lang)
        t1.save(f'{date_string}.mp3')
        playsound(f'{date_string}.mp3')


canvas = Tk()
canvas.geometry('800x500')

image = Image.open('icon.png')
label_photo = ImageTk.PhotoImage(image)
label1 = Label(image=label_photo)
label1.grid(row=0, column=1)
line = Text(width=100, height=1)
line.grid(row=1, column=0, columnspan=3)
b1 = Button(text='Open', command=open_file, width=50)
b1.grid(row=2, column=1)
canvas.mainloop()









