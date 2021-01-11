import pyttsx3
import PyPDF2

def readMybook():
	pdf_read = PyPDF2.PdfFileReader(open('python_digital_forensics_tutorial.pdf', 'rb'))

	reader = pyttsx3.init()
	reader.setProperty('rate', 200)

	for page_num in range(pdf_read.numPages):
	    text =  pdf_read.getPage(page_num).extractText()
	    reader.say(text)
	    reader.runAndWait()
	reader.stop()
