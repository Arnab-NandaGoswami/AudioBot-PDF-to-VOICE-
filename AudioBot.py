import pyttsx3
import PyPDF2
book = open('CS.pdf','rb') # instead of CS.pdf, use your own file.pdf
pdfReader=PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
speaker.setProperty('rate', 135)
volume = speaker.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
speaker.setProperty('volume',1.0)
print(volume)
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
