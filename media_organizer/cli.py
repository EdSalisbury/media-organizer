import argparse

parser = argparse.ArgumentParser(description="Organize media")
parser.add_argument("source_dir")

args = parser.parse_args()
print(args.source_dir)
