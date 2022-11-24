from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import ffmpeg

utc = ZoneInfo("UTC")
localtz = ZoneInfo("America/Denver")


class Video:
    def __init__(self, filename):
        self.filename = filename

    def get_creation_date(self):
        print(f"Probing {self.filename}")
        data = ffmpeg.probe(self.filename)["streams"]
        creation_date_time = data[0].get("tags").get("creation_time")
        if creation_date_time:
            creation_date_time = creation_date_time.replace(".000000", "")
            new_timestamp = datetime.strptime(creation_date_time, "%Y-%m-%dT%H:%M:%SZ")
            utctime = new_timestamp.replace(tzinfo=utc)
            localtime = utctime.astimezone(localtz)
            return localtime.strftime("%Y-%m-%d")
        return "0000-00-00"
