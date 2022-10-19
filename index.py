# Solo UTF-8

from encodings import utf_8
from parse import doIt
from tkinter.filedialog import askopenfile, Tk

Tk().withdraw()
Direccion = askopenfile(
    title="Abrir Archivo de Grámatica",
    filetypes=(("Text Files", "*.txt"),))

text = ""

with open(Direccion.name, "r") as contentFile:
    text = contentFile.read()

doIt(text)
