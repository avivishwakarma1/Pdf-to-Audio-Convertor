import PyPDF2
#You can use pyttsx3(its a python based library which is used for the text-to-speach) or gTTS(its a google based text-to-speach convertor)
from gtts import gTTS 
pdfFileObj = open("D:/VS_Code/Python/The_Clever_Crow.pdf", "rb")
pdfReader = PyPDF2.PdfReader(pdfFileObj)

mytext = " "

for pnum in range(len(pdfReader.pages)):
    pageFileObj = pdfReader.pages[pnum]

    mytext += pageFileObj.extract_text()
print(mytext)
pdfFileObj.close()

lang1 = {
    "1": "en",    # English
    "2": "fr",    # French
    "3": "es",    # Spanish
    "4": "de",    # German
    "5": "zh-CN", # Chinese (Mandarin, simplified)
    "6": "ja",    # Japanese
    "7": "ko",    # Korean
    "8": "ru",    # Russian
    "9": "it",    # Italian
    "10": "hi",   # Hindi
    "11": "th",   # Thai
    "12": "id",   # Indonesian
    "13": "he",   # Hebrew
    "14": "fi",   # Finnish
    "15": "da",   # Danish
    "16": "ar",   # Arabic
    "17": "pt",   # Portuguese
    "18": "nl"    # Dutch
}
print("Available Languages:")
for key in lang1:
    print(f"{key}: {lang1[key]}")


lang2 = input()

tts = gTTS(text = mytext, lang = lang1[lang2])
tts.save("pdftoaudio.mp3")