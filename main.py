import os

with open("rapgod.txt","r") as file:
    lines = file.readlines()


stream = os.popen("espeak-ng \"{}\" --ipa -q".format(lines[1].replace("\"","")))
output = stream.readlines()
for line in output:
    print(line)