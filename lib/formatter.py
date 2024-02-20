from bs4 import BeautifulSoup
import os

class IndentSpacer:
    def __init__(self, lines, spaces="   "):
        start_index = 0

        if "doctype" in lines[start_index].lower():
            start_index += 1



        self.start_line = lines[start_index]
        self.end_line = lines[len(lines) - 1]
        self.lines = lines[start_index + 1:len(lines) - 1]
        self.spaces = spaces


    def add_indent(self):
        line_index = 0

        while line_index < len(self.lines):
            if self._is_start_tag(line=self.lines[line_index]) == False:
                line_index += 1
                continue

            line = self.lines[line_index].strip()
            tagname = self._get_tagname_from(line=line)

            if len(tagname) == 1:
                line_index += 1
                continue
            
            end_index  = self._get_tag_range(start_index=line_index)

            if end_index is None:
                line_index += 1
                continue

            for j_index in range(line_index, end_index + 1):
                self.lines[j_index] = "   " + self.lines[j_index]

            line_index += 1


        new_html = "".join(self.lines)
        return "".join([self.start_line, new_html, self.end_line])


    def _is_start_tag(self, line):
        flag = True

        if "<" not in line:
            flag = False
            return flag

        if "/>" in line:
            flag = False
            return flag

        if "</" in line:
            flag = False
            return flag



        return flag

    def _get_tagname_from(self, line):
        tag_name = line.strip().strip("<").strip(">").split()[0]
        return tag_name


    def _get_tag_range(self, start_index):

        tag_name = self._get_tagname_from(line=self.lines[start_index])
        start_tag = "<" + tag_name  + ">"
        end_tag = "</" + tag_name + ">"

        current_index = start_index + 1 
        ignore_end_tag = 0


        for line in self.lines[start_index + 1:]:
            line = line.strip()


            if ("<" + tag_name ) in line:
                tag = "<" + self._get_tagname_from(line=line) + ">"

                if start_tag == tag:
                    ignore_end_tag += 1

            elif end_tag == line:
                if ignore_end_tag > 0:
                    ignore_end_tag -= 1
                else:
                    return current_index

            current_index += 1

        return None




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

        lines = new_html.split("\n")
        lines = [line + "\n" for line in lines]


        spacer = IndentSpacer(lines=lines)
        new_html = spacer.add_indent()

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
        

