from docx2pdf import convert
from os import listdir
# from msvcrt import getch

def docx_name(spisok: list[str]):
    spisok2 = list()
    for name in spisok:
        if name[-5::] == ".docx":
            spisok2.append(name)
    return spisok2


spisok = docx_name(listdir())
postfix = "[converted to pdf].pdf"
for doc in spisok:
    print(doc)
    convert(doc, doc[:-5:] + postfix)

# print("End of the program. Waiting for button press ...")
# getch()
