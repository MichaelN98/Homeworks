import re
import fileinput

def remove_numbers():
    for line in fileinput.input('file.txt'):
        re.sub("\d+", "", line)

    with open("file.txt", 'w') as filedata:
        file.datalines = filedata.()




