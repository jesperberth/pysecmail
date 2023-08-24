import extract_msg
import re
import glob
import shutil
import csv

msgDir = "messages"
doneDir = "done"
outputFile = "output/iplist.txt"
msgfiles = []
iparray = []
resultip = []

def readFiles():
    for file in glob.glob(msgDir+"/*.msg"):
        msgfiles.append(file)

def writeOutput():
    with open(outputFile, "w") as write_file:
        for line in resultip:
            write_file.write(" ".join(line) + "\n")
    write_file.close()

def moveFile(f):
    shutil.move(f, doneDir)

def readExistingFile():
    with open(outputFile, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in data:
            print(row)
            iparray.append(row)
    csvfile.close()

def getIp(f):
    msg = extract_msg.Message(f)
    msg_body = msg.body
    reg = re.compile('[0-9]+(?:\.[0-9]{1,3}){3}')
    ip = re.findall( reg, msg_body )
    iparray.append(ip)
    moveFile(f)

def remDuplicate():
    [resultip.append(x) for x in iparray if x not in resultip]

def main():
    readFiles()

    numberfiles = len(msgfiles)
    str_numberfiles = str(numberfiles)
    print("Reading " + str_numberfiles + " Msg files")

    for file in msgfiles:
        getIp(file)

    readExistingFile()
    remDuplicate()
    writeOutput()

if __name__ == "__main__":
    main()
