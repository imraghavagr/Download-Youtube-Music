from pytube import YouTube
import os

# paste all the urls you want to download in links.txt file

#open the input file  by creating a file obejct
songs_urls = open('links.txt','r')

#read all the lines of links.txt file and store them inside a list, here, 'urls'
urls = songs_urls.readlines()

#type of each url will be a string
#print(type(urls[0]))


# url input from urls list
for url in urls:

    yt = YouTube(url)


    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    destination = '/home/raghav/Music/bhajans'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")
