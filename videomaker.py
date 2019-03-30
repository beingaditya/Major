#!/usr/bin/env python
# coding: utf-8

# In[1]:


from moviepy.editor import *
import downloader
import frameGenerator


def clip(line):
    try:
        image = downloader.download_image(line['keyword'])
        if image == "":
            image = "default.jpeg"
    except Exception as e:
        image = "default.jpeg"

    frame = frameGenerator.generateFrame(image, line['sentence'])
    duration = len(line['sentence'])/20
    return ((ImageClip(frame)
            .set_duration(duration)
            .set_pos("center")), duration)


def createVideo(lines, title, audio):
    time = 0

    arr = []

    print("\n\nDownloading " + str(len(lines)) + " Images ...\n")
    for line in lines:
        image, duration = clip(line)
        arr.append(image.set_start(time).crossfadein(1).crossfadeout(1))
        time += duration-1

    video = CompositeVideoClip(arr)
    music = AudioFileClip(audio)
    music = afx.audio_loop(music, duration=video.duration)
    music = afx.audio_fadeout(music, duration=2)
    video = video.set_audio(music)
    video.write_videofile("Videos/" + title + ".mp4", threads=4, fps=30)





