import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        '--file',
                        action="store",
                        dest="file",
                        type=str,
                        help="Script to be updated")

    parser.add_argument('-t',
                        '--time',
                        action="store",
                        dest="time",
                        type=str,
                        help="New time parameter")

    args = parser.parse_args()
    file = args.file
    time = args.time


    def getNewContent(filename: str, newTime: str) -> str:
        "return a string containing the new script content."
        with open(filename, 'r') as infile:
            stringFile = infile.read()

            splitLine = stringFile.split(' ')
            ind = splitLine.index('--delta')
            splitLine[ind + 1] = newTime
            return ' '.join(splitLine)


    def writeNewContent(filename: str, newContent: str):
        "Write the specified content into the file"
        with open(filename, 'w') as infile:
            infile.write(newContent)


    nc = getNewContent(filename=file, newTime=time)
    writeNewContent(filename=file, newContent=nc)