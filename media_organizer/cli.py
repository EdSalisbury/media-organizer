import argparse
import os
import shutil
from datetime import datetime

import file as fileutil
import image
import video

parser = argparse.ArgumentParser(description="Organize media")
parser.add_argument("-m", "--move", action="store_true")
parser.add_argument("source_dir")
parser.add_argument("dest_dir")

args = parser.parse_args()

files = list()
for (dir_path, _, file_names) in os.walk(args.source_dir):
    for filename in file_names:
        files.append(os.path.join(dir_path, filename))

for file in files:
    print(f"Getting creation date for {file}")
    type = fileutil.get_file_type(file)
    print(f"Filetype for {file}: {type}")
    creation_date = "0000-00-00"
    if "image" in type:
        img = image.Image(file)
        creation_date = img.get_creation_date()
    elif "movie" in type:
        vid = video.Video(file)
        creation_date = vid.get_creation_date()

    if creation_date == "0000-00-00":
        creation_date = os.stat(file).st_birthtime
        time = datetime.fromtimestamp(creation_date)
        creation_date = time.strftime("%Y-%m-%d")

    dest_dir = os.path.join(args.dest_dir, creation_date)

    if not os.path.exists(dest_dir):
        print(f"Creating {dest_dir}")
        os.makedirs(dest_dir)

    basedir, filename = os.path.split(file)
    dest_file = os.path.join(dest_dir, filename)

    while os.path.exists(dest_file):
        base, ext = os.path.splitext(filename)
        base += "_"
        filename = f"{base}{ext}"
        dest_file = os.path.join(dest_dir, filename)

    if args.move:
        print(f"Moving {file} to {dest_file}")
        shutil.move(file, dest_file)
    else:
        print(f"Copying {file} to {dest_file}")
        shutil.copy2(file, dest_file)
