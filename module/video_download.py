from pytube.streams import Stream
from module.converter import AudioConverter
from pytube import Playlist, YouTube
from progress.bar import Bar

class Downloader:
    def __init__(self) -> None:
        pass
    
    def _base_download(self, video: YouTube, mode: str, playlistName: str = None):
        def onProgressCallback(stream: Stream, file_handle, bytes_remaining):
            percent = ((stream.filesize - bytes_remaining) / stream.filesize) * 100;
            info = (video.title[:25] + '..') if len(video.title) > 25 else video.title
            bar = Bar(info, max=100)
            bar.next(n=int(percent))

            if(int(percent) >= 100):
                bar.finish()
        
        video.register_on_progress_callback(onProgressCallback)
        
        path = "output"

        if(playlistName != None):
            path = "output/"+playlistName

        if mode == "mp3":
            video.streams.get_audio_only().download(output_path="cache")
        
        if mode == "vid_high":
            video.streams.get_highest_resolution().download(output_path=path)
                
        if mode == "vid_low":
            video.streams.get_lowest_resolution().download(output_path=path)

    def videoDownload(self, video_url: str, mode: str):
        video = YouTube(video_url)
        self._base_download(video=video, mode=mode)

    def batchVideoDownload(self, urls: list, mode: str):
        for url in urls:
            self.videoDownload(video_url=url, mode=mode)

        if mode == "mp3":
            AudioConverter().convert_to_mp3()
        
    def playlistDownload(self, playlist_url: str, mode: str) -> str:
        _playlist = Playlist(playlist_url)

        for e in _playlist.videos:
            self._base_download(video=e, mode=mode, playlistName=_playlist.title)
        
        print("Download " + _playlist.title + " Finished")

        if mode == "mp3":
            AudioConverter().convert_to_mp3(subdir=_playlist.title)

    def playlistDownloadBatch(self, playlist_urls: list, mode: str):
        for pls in playlist_urls:
            self.playlistDownload(playlist_url=pls, mode=mode)
    
    