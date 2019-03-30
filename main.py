import os
import shutil
import videomaker
import digestor
import music
from bs4 import BeautifulSoup
import requests

def renewDirectories():
    directory = [os.getcwd() + "\\Downloaded Images\\", os.getcwd() + "\\Images\\Final\\", os.getcwd() + "\\Images\\Text\\"]

    for folder in directory:
        shutil.rmtree(folder)
        os.mkdir(folder)


def getUserInput():
    response = input("Select input mode:\n1.Plain Text\n2.Article url\n")
    if response.isdigit():
        response = int(response)
        if response == 1:
            title = input("Enter title of the video\n")
            print("Enter Text (Press Ctrl + D to stop):\n")
            text = ""

            while True:
                try:
                    line = input()
                except EOFError:
                    break
                text += line

            startWorking(text, title)
        elif response == 2:
            title = input("Enter title of the video\n")
            url = input("Input Article url\n")
            text = getRelevantText(url)
            print(text)
            startWorking(text, title)
    else:
        print("Input is invalid. Please enter a valid input!")
        getUserInput()

def startWorking(text, title):
    print("\n\n\nWork in Progress ...\n\n")
    lines = digestor.getSummary(text)
    if not len(lines) > 0:
        print("***No valid content found***")
        return

    song = music.getRelevantSong(text)
    videomaker.createVideo(lines, title, song)
    
def getRelevantText(url):
    reply = requests.get(url)
    bsoup = BeautifulSoup(reply.content, "html.parser")

    sentences = [p.get_text() for p in bsoup.find_all("p", text=True)]

    scrapedText = ""
    for line in sentences:
        word = line.replace(u'\xa0', u' ')
        scrapedText += word + " "

    return scrapedText
    
renewDirectories()
getUserInput()

