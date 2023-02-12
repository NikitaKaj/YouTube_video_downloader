from pytube import YouTube
import os

while True:

    link = input("Enter URL: ")
    video = YouTube(link)
    
    choose = int(input("\n1 - video\n2 - audio\nВведите: "))
    print()
    if choose == 1:
        second_choose = int(input("1 - 1080p\n2 - 720p\nВведите: "))
        print()
        if second_choose == 1:
            stream = video.streams.filter(type="video", res="1080p")
        elif second_choose == 2:
            stream = video.streams.filter(type="video", res="720p")
    else:
        stream = video.streams.filter(type="audio")
    
    for i in range(len(stream)):
        print(i+1,"- ", stream[i])

    vnum = int(input("\nВведите номер нужного: "))
    print("Скачивание началось!")
    stream[vnum].download(output_path=f"C:\\Users\\{os.getlogin()}\\Desktop")
    print("Скачивание завершено!")

