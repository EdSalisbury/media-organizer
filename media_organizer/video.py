import ffmpeg


class Video:
    def __init__(self, filename):
        self.filename = filename

    def get_creation_date(self):
        data = ffmpeg.probe(self.filename)["streams"]
        creation_date_time = data[0].get("tags").get("creation_time")
        if creation_date_time:
            return creation_date_time.split("T")[0]
        return "0000-00-00"
