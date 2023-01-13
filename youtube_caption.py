import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import os

def get_captions(youtube_link):
    video_id = youtube_link.split("?v=")[1]
    try:
        captions = YouTubeTranscriptApi.get_transcript(video_id)
    except:
        print("Error: Invalid youtube link or captions not available.")
        return
    caption_text = ""
    for caption in captions:
        caption_text += caption['text'] + ' '
    return caption_text

youtube_link = input("Enter a YouTube link: ")
captions = get_captions(youtube_link)
if captions:
    with open("captions.txt", "w") as file:
        file.write(captions)
        print("Captions saved in captions.txt")
