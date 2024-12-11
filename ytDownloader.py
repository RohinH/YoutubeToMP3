from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("TITLE ", yt.title)
print("View: ",yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('C:/Users/rohin/OneDrive/Documents/simpleProjectsVid')


#put r at start istead of %