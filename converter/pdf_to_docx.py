from pdf2docx import Converter
from os import listdir
# from msvcrt import getch

def pdf_name(spisok: list[str]):
    spisok2 = list()
    for name in spisok:
        if name[-4::] == ".pdf":
            spisok2.append(name)
    return spisok2

spisok = pdf_name(listdir())
postfix = "[converted to docx].docx"

for pdf in spisok:
    print(pdf)
    # convert(doc, doc[:-5:] + postfix)
    cv_obj = Converter(pdf)
    cv_obj.convert(pdf[:-4:]+postfix)
    cv_obj.close()

# print("End of the program. Waiting for button press ...")
# getch()
