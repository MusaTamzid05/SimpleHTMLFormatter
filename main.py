import argparse
from lib.formatter import FileFormatter
from lib.formatter import DirFormatter
from lib.formatter import IndentSpacer
import os

def get_tagname_from(line):
    tag_name = line.strip().strip("<").strip(">").split()[0]
    return tag_name

def is_start_tag(line):
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



def get_tag_range(html_lines, start_index):
    tag_name = get_tagname_from(line=html_lines[start_index])
    start_tag = "<" + tag_name  + ">"
    end_tag = "</" + tag_name + ">"

    current_index = start_index + 1 
    ignore_end_tag = 0


    for line in html_lines[start_index + 1:]:
        line = line.strip()


        if ("<" + tag_name ) in line:
            tag = "<" + get_tagname_from(line=line) + ">"

            if start_tag == tag:
                ignore_end_tag += 1

        elif end_tag == line:
            if ignore_end_tag > 0:
                ignore_end_tag -= 1
            else:
                return current_index

        current_index += 1

    return None





def main():
    parser = argparse.ArgumentParser("html parser")
    parser.add_argument("--path", dest="path", type=str, required=True, help="Path to the target file/dir")
    args = parser.parse_args()

    formatter = None

    if os.path.isdir(args.path):
        formatter = DirFormatter(path=args.path)
    else:
        formatter = FileFormatter(path=args.path)

    formatter.format()


if __name__ == "__main__":
    main()
    '''
    with open("test.html") as f:
        lines = f.readlines()
        indenter = IndentSpacer(lines=lines)
        new_html = indenter.add_indent()
        print(new_html)
    '''




