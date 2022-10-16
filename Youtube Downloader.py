from pytube import YouTube

while True:
    link = input("Enter URL: ")
    video = YouTube(link)
    stream = video.streams.filter(file_extension='mp4')
    stream = video.streams.get_highest_resolution()
    print("Скачивание началось!")
    stream.download(output_path="C:\\Users\\Nikita\\Desktop")
    print("Скачивание завершено!")