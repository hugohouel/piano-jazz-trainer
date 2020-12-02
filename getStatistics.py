

from os import listdir

ACC = 'Accords à 4 sons en position fondamentale'
ARM = 'Armure'
ITE = 'Intervalles'
MOD = 'Modes'
VOI = 'Voicings'
TRI = 'Triades'
CAD = '251'


CATEGORIES = [VOI, TRI, ITE,
              MOD, ARM, ACC,
              CAD]


def getCategoryOfFile(fileName: str) -> str:
    global ACC, ARM, ITE, MOD, VOI, TRI, CAD

    if fileName.startswith('v_'):
        return VOI
    elif fileName.startswith('t_'):
        return TRI
    elif fileName.startswith('acc'):
        return ACC
    elif fileName.startswith('251'):
        return CAD
    elif fileName.startswith('arm'):
        return ARM
    elif fileName.startswith('i_'):
        return ITE
    elif fileName.startswith('modes'):
        return MOD
    else:
        return ''


def getTimeParameterForFile(filename: str) -> str:
    with open(filename, 'r') as infile:
        stringFile = infile.read()
        splitLine = stringFile.split(' ')
        ind = splitLine.index('--delta')
        return splitLine[ind + 1]


def getListOfAllScripts():
    return [e for e in listdir('.') if e.endswith('.bat')]


if __name__ == "__main__":

    simpleLine = "\n" + "-" * 422 + "\n"
    allScripts = getListOfAllScripts()

    for cat in CATEGORIES:
        print(simpleLine + '\n          *  {}  * \n'.format(cat))
        for fileName in allScripts:
            if getCategoryOfFile(fileName) == cat:
                timeParameter = getTimeParameterForFile(fileName)
                print('\n {} has time parameter     {}'.format(fileName, timeParameter))

    print(simpleLine)