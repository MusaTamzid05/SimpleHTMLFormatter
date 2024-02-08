from bs4 import BeautifulSoup
import os

class FileFormatter:
    def __init__(self, path):
        self.path = path

    def format(self):
        text = None

        with open(self.path) as f:
            lines = f.readlines()
            text = "".join(lines)

        soup = BeautifulSoup(text, "html5lib")
        new_html = soup.prettify()

        os.remove(self.path)

        with open(self.path, "w") as f:
            f.write(new_html)

        print(f"{self.path} formatted")



        



class DirFormatter:
    def __init__(self, path):
        self.path = path


    def format(self):
        filenames = os.listdir(self.path)

        for filename in filenames:
            file_path = os.path.join(self.path, filename)

            formatter = FileFormatter(path=file_path)
            formatter.format()
        

