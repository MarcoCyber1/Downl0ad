from pytube import YouTube



print("1.mp3")

print("2.mp4")

you = input("Choose the format!: ")



if you == "1":

    

    try:  

     url = input("Enter Your audio URL: ")

     video = YouTube(url)

     stream = video.streams.filter(only_audio=True).first()

     stream.download(filename=f"{video.title}.mp3")

     print("successfull")

    except:

      print("error !")

else:

     def Download(link):

         youtubeObject = YouTube(link)

         youtubeObject = youtubeObject.streams.get_highest_resolution()

         try:

            youtubeObject.download()

         except:

            print("error !")

         print("successfully")



     link = input("Enter the YouTube video URL: ")

     Download(link)

