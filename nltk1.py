import nltk
import PyPDF2

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

'''document = 'Assets,liabilities, are financial terms.'
sentences = nltk.sent_tokenize(document)

data = []
for sent in sentences:
    data = data + nltk.pos_tag(nltk.word_tokenize(sent))
 
for word in data:
    if 'NNS' in word[1]:
        print(word)
'''

pdfFileObj = open('Sample PDF.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)

page = pdfReader.getPage(1)
page_content = page.extractText()
print(page_content)