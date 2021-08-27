from moviepy.editor import *
from os import *

class AudioConverter:
    def __init__(self) -> None:
        pass

    def convert_to_mp3(self, subdir: str = "Converted"):
        vid_list = listdir("cache")
        try:
            os.mkdir("output")
            print("Create output folder")
        except:
            pass

        try:
            os.mkdir("output/"+subdir)
        except:
            print("Directory "+subdir+" already Exist")


        for e in vid_list:
            base =  os.path.basename("cache/"+e)
            audio = AudioFileClip("cache/"+e)

            audio.write_audiofile("output/"+subdir+"/"+os.path.splitext(base)[0]+".mp3")
            audio.close()
        
        self.remove_cache()

    def remove_cache(self):
        dir = 'cache'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))