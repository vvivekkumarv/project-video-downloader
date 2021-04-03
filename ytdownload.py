from pytube import YouTube

videos=open("sample.txt",'r')

for i in videos:
    yt=YouTube(i)
    try:
        dw=yt.streams.first()
        dw.download("D:\PROGRAMMING\PYTHON\PYTHON PROJECTS\project-video downloader")
        print("downloaded",i)
    except:
        print("download failed",i)
