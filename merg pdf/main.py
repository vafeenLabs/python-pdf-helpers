from pypdf import PdfMerger
from os import listdir

def pdf_name(spisok: list[str]):
    spisok2 = list()
    for name in spisok:
        if name[-4::] == ".pdf":
            spisok2.append(name)
    return spisok2

pdfs = pdf_name(listdir())

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()