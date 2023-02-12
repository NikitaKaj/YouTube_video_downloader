from pytube import YouTube
import os

while True:
    i = 0
    vnum = 0
    resolution_1440p = False
    resolution_1440p_text = "None"
    resolution_2160p = False
    resolution_2160p_text = "None"
    resolution_4320p = False
    resolution_4320p_text = "None"

    # Получение видео
    link = input("Enter URL: ")
    video = YouTube(link)
    
    # Инициализация
    stream = video.streams.filter(res="1440p")
    if len(stream) >= 1:
        resolution_1440p = True
        resolution_1440p_text = "1440p"
    
    stream = video.streams.filter(res="2160p")
    if len(stream) >= 1:
        resolution_2160p = True
        resolution_2160p_text = "2160p"

    stream = video.streams.filter(res="4320p")
    if len(stream) >= 1:
        resolution_4320p = True
        resolution_4320p_text = "4320p"
    
    choose = int(input("\n1 - video\n2 - audio\nВведите: "))
    print()
    if choose == 1:
        second_choose = int(input(f"1 - 720p\n2 - 1080p\n3 - {resolution_1440p_text}\n4 - {resolution_2160p_text}\n5 - {resolution_4320p_text}\n6 - Со звуком\n7 - Показать все\nВведите: "))
        print()
        if second_choose == 1:
            stream = video.streams.filter(type="video", res="720p")
        elif second_choose == 2:
            stream = video.streams.filter(type="video", res="1080p")
        elif second_choose == 3 and resolution_1440p == True:
            stream = video.streams.filter(type="video", res="1440p")
        elif second_choose == 4 and resolution_2160p == True:
            stream = video.streams.filter(type="video", res="2160p")
        elif second_choose == 5 and resolution_4320p == True:
            stream = video.streams.filter(type="video", res="4320p")
        elif second_choose == 6:
            stream = video.streams.filter(type="video", progressive=True)
        elif second_choose == 7:
            stream = video.streams.filter(type="video")
        else:
            print()
            continue
    elif choose == 2:
        stream = video.streams.filter(type="audio")
    
    for i in range(len(stream)):
        print(i+1,"- ", stream[i])

    vnum = input("\nВыберите или напишите Q чтобы выйти: ")
    if vnum == "Q" or vnum == "q":
        print()
        continue
    else:
        print("Скачивание началось!")
        stream[int(vnum)-1].download(output_path=f"C:\\Users\\{os.getlogin()}\\Desktop")
        print("Скачивание завершено!")