from module.video_download import Downloader
from module.config_parser import *

_dl = Downloader()

conf = Config("config.json")
for a in conf.tasks():
    # PLaylist first
    _dl.playlistDownloadBatch(a.playlist, mode=a.output_type)

    # Videos then
    _dl.batchVideoDownload(a.videos, mode=a.output_type)
