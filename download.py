
from pytube import YouTube
import os
import io
from youtube_search import YoutubeSearch

# Define the scopes required for accessing YouTube data
path = input('path to folder where you want the mp3 files: ')


def get_link(query):
    results = YoutubeSearch(query, max_results=1).to_dict()
    if results:
        video_id = results[0]['id']
        video_link = f'https://www.youtube.com/watch?v={video_id}'
        return video_link
    else:
        return None

def get_mp3(link):
    try:
        yt = YouTube(link)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download(path)
        mp3_file = audio_file.split('.')[0] + '.mp3'
        os.rename(audio_file, mp3_file)
        print('MP3 download completed successfully!')
    except Exception as e:
        print('An error occurred:', str(e))

def get_all():
    with open('songs.txt', 'r') as file:
        for line in file:
            song = line.strip()
            get_mp3(get_link(song))