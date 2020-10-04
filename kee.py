from os import listdir
from os import mkdir, rmdir


class FileExplorer:
    def __init__(self, path):
        self.path = path
        try:
            self.directory = listdir(self.path)
        except:
            self.directory = listdir('/')
    def update_directory(self, new_directory):
        try:
            self.directory = listdir(new_directory)
        except FileNotFoundError:
            self.directory = listdir('/')


