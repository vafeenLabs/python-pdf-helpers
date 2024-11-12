from pdf2docx import Converter
from docx2pdf import convert
from os import listdir

cv_obj = Converter("artur.pdf")
cv_obj.convert("artur.docx")
cv_obj.close()
