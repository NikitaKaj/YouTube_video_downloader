from pytube import YouTube
import os

while True:
    link = input("Enter URL: ")
    video = YouTube(link)
    stream = video.streams.filter(file_extension='mp4')
    stream = video.streams.get_highest_resolution()
    print("Скачивание началось!")
    stream.download(output_path=f"C:\\Users\\{os.getlogin()}\\Desktop")
    print("Скачивание завершено!")