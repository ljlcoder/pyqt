import pandas as pd
from docx import Document
from pptx import Presentation
#pip install python-docs,python-pptx,pandas
class File_reader:
    def __init__(self):
        pass
    def read_txt(self,path):
        with open(path,"r",encoding="utf-8") as f:
            return f.read()

    def read_excel(self,path):
        return pd.read_excel(path).to_string()

    def read_docx(self,path):
        document = Document(path)
        return [paragraph.text for paragraph in document.paragraphs]

    def read_pptx(self,path):
        presentation = Presentation(path)
        return [slide.title.text for slide in presentation.slides]



reader=File_reader()
res=reader.read_txt("H:\python\pyqt\docx_search\demo.txt")
print(res)