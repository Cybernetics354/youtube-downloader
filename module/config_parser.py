import json

class Tasks:
    def __init__(self, data) -> None:
        self.output_type = data["output_type"]
        self.playlist = data["playlists"]
        self.videos = data["videos"]
    
    def output_type(self) -> str:
        return self.output_type
    
    def playlist(self) -> list:
        return self.playlist

    def videos(self) -> list:
        return self.videos

class Config:
    def __init__(self, fileName: str) -> None:
        self.fileName = fileName
        self.data = json.load(open(fileName))        
        self.parsed = []

        for a in self.data["tasks"]:
            self.parsed.append(Tasks(data=a))

    def tasks(self) -> list[Tasks]:
        return self.parsed
        
