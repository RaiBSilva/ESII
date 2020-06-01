# -----------------------------------------------------------------------------------------
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO


def lerPDF(arquivoPDF):
    # PDFResourceManager Usado para armazenar recursos compartilhados
    # como fontes e imagens
    recursos = PDFResourceManager()
    buffer = StringIO()
    layoutParams = LAParams()
    dispositivo = TextConverter(recursos, buffer, laparams=layoutParams)
    process_pdf(recursos, dispositivo, arquivoPDF)
    dispositivo.close()
    conteudo = buffer.getvalue()
    buffer.close()
    return conteudo


# # print(stringSaida)

# arquivoTxt = open("teste.txt","w", encoding="utf-8")
# arquivoTxt.write(stringSaida)
# arquivoTxt.close()

# arquivoPDF.close()
# ----------------------------------------------------------------------------------------



