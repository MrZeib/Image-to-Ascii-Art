import pywhatkit
from tkinter.filedialog import askopenfilename

img = askopenfilename()
ascii_art = pywhatkit.image_to_ascii_art(img, "ascii_art.txt")
