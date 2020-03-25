from PyPDF2 import PdfFileMerger
import os
import glob

os.chdir(os.path.dirname(os.path.realpath(__file__)))

for dir in glob.glob(os.getcwd() + "/*/"):
    os.chdir(dir)
    dirname = os.getcwd().split("\\")[-1]
    merger = PdfFileMerger()
    try:
        os.remove("combined.pdf")
    except OSError:
        pass
    pdfs = glob.glob("*.pdf")
    print("On Directory %s" % dirname)
    for pdf in pdfs:
        print(pdf)
        merger.append(pdf)
    if merger is not None:
        merger.write("combined.pdf")
        merger.close()
    os.chdir("..")
