import PIL
from PIL import ExifTags
from PIL import Image as PILImage
from PIL.ExifTags import TAGS
from pillow_heif import register_heif_opener


class Image:
    def __init__(self, filename):
        self.filename = filename
        register_heif_opener()
        self.GetExifOffset()

    def GetExifOffset(self):
        self.offset_key = None
        for key, value in TAGS.items():
            if value == "ExifOffset":
                self.offset_key = key
                break

    def get_exif_ifd(self, exif):
        info = exif.get_ifd(self.offset_key)
        return {TAGS.get(key, key): value for key, value in info.items()}

    def get_creation_date(self):
        try:
            image = PILImage.open(self.filename)
            exifdata = image.getexif()
            ifd_info = self.get_exif_ifd(exifdata)
            creation_date_time = ifd_info.get("DateTimeOriginal")

            if creation_date_time:
                return creation_date_time.split(" ")[0].replace(":", "-")
        except:
            return "0000-00-00"

        return "0000-00-00"
