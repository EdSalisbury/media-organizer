import magic


def get_file_type(file):
    file = file.lower()
    if file.endswith(".mov"):
        return "movie"
    if file.endswith(".jpg"):
        return "image"
    if file.endswith(".jpeg"):
        return "image"
    if file.endswith(".tiff"):
        return "image"
    if file.endswith(".heic"):
        return "image"
    if file.endswith(".png"):
        return "image"

    return magic.from_file(file)
