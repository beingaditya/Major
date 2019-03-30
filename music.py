import requests
import os, random


def sentiments(text):
    sentDoc = requests.post(url="http://text-processing.com/api/sentiment/", data={"text": text})
    return sentDoc.json()['label']


def getRelevantSong(text):
    sentiment = sentiments(text)

    if sentiment == 'pos':
        return "music/positive/" + random.choice(os.listdir(os.curdir + "/music/positive/"))

    if sentiment == 'neg':
        return "music/negative/" + random.choice(os.listdir(os.curdir + "/music/negative/"))

    return "music/neutral/" + random.choice(os.listdir(os.curdir + "/music/neutral/"))


if __name__ == '__main__':
    print(getRelevantSong("nothing"))
