import argparse
import os

import image
import magic
import video

parser = argparse.ArgumentParser(description="Organize media")
parser.add_argument("source_dir")

args = parser.parse_args()

files = list()
for (dir_path, _, file_names) in os.walk(args.source_dir):
    for filename in file_names:
        files.append(os.path.join(dir_path, filename))

for file in files:
    print("file: " + file)
    type = magic.from_file(file)
    creation_date = "0000-00-00"
    if "image" in type or "Image" in type:
        img = image.Image(file)
        creation_date = img.get_creation_date()
    elif "movie" in type:
        vid = video.Video(file)
        creation_date = vid.get_creation_date()

    print("creation date: " + creation_date)
