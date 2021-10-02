import re
import tarfile

fh = open("file.txt")
ff = open('file2.txt', "w")
text = fh.readlines()
ff.write(str(len(text))+'\n')

for i in range(1, len(text), 2):
    ff.write(text[i])
count = 0

for subtext in text:
    i = 0
    while i < len(subtext):
        numb = ''
        while subtext[i].isdigit():
            numb = numb + subtext[i]
            i += 1
        if numb != '':
            count += int(numb)
        i += 1

ff.write(str(count))


