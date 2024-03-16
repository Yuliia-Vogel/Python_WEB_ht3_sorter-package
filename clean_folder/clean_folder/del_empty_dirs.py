import os

def remove_empty_folders(path, remove_root=True):
    if not os.path.isdir(path):
        return

    # видалення пустих підпапок папок
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                remove_empty_folders(fullpath)

    # видалення пустих папок
    files = os.listdir(path)
    if len(files) == 0 and remove_root:
        os.rmdir(path)


