from time import sleep
from random import choice
from math import floor
import argparse
from tkinter import Tk, Label, Message


"""
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------                   FUNCTIONS              ------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
"""

def compute_names(tons):
    triadesMin = [e + '-' for e in tons]
    accordsMin7 = [e + '7' for e in triadesMin]
    accords7 = [e + '7' for e in tons]
    accordsMaj7 = [e + 'Maj7' for e in tons]
    #accordsDemiDim = [e + 'b5' for e in accordsMin7] #Ø
    accordsDemiDim = [e + ' Ø' for e in tons] #Ø
    accordsDim = [e + ' °' for e in tons]
    accordsAugm = [e + ' aug' for e in tons]
    return {'triadesMaj' : tons, 'triadesMin' : triadesMin, 'accordsMin7' : accordsMin7, 'accords7' : accords7,
            'accordsMaj7' : accordsMaj7, 'accordsDemiDim' : accordsDemiDim, 'accordsDim' : accordsDim,
           'accords_augm' : accordsAugm}

def getList(mode : int) -> list:
    """
    Return the list of tones I am gonna work with, according to the following mapping :
    
    1 : only major triads
    2 : only minor triads
    3 : only min7
    4 : only 7
    5 : only maj7
    6 : only demi dim
    7 : only dim
    8 : only augm
    12 : major and minor triads
    34 : min7 and 7
    345 : min7, 7 and maj7
    """
    if mode == 1:
        myList = triadesMaj
    if mode == 2:
        myList = triadesMin
    if mode == 3:
        myList = accordsMin7
    if mode == 4:
        myList = accords7
    if mode == 5:
        myList = accordsMaj7
    if mode == 6:
        myList = accordsDemiDim
    if mode == 7:
        myList = accordsDim
    if mode == 8:
        myList = accordsAugm
    if mode == 12:
        myList = triadesMaj + triadesMin
    if mode == 34:
        myList = accordsMin7 + accords7
    if mode == 345 :
        myList = accordsMin7 + accords7 + accordsMaj7
    return myList

def train(mode : int, dt, nbRepetitions = 2, subtitle=""):
    """ Show the chord to play. One chord every dt seconds. Once all the chords have been played once, another round can begin.
    
    Mode : 
    1 : only major triads
    2 : only minor triads
    3 : only min7
    4 : only 7
    5 : only maj7
    12 : all triads (major and minor)
    34 : min7 and 7
    345 : min7, 7 and maj7"""

    myList = getList(mode)
    listOfChosenElements = []
    n = len(myList)

    for i in range(nbRepetitions * n):
        
        if len(listOfChosenElements) == n:
            listOfChosenElements = []
        
        el = choice(myList)
        
        #Vérification que l'élement n'a pas été choisi dans le dernier cycle. Si oui, on retire un autre élément.
        while el in listOfChosenElements:
            el = choice(myList)
            
        # Ajout de l'élément dans la liste des éléments déjà tirés
        listOfChosenElements.append(el)
        #print(el)
        
        #Affichage
        root = Tk()
        root.attributes('-fullscreen', True)
        root.after(floor(dt * 1000), lambda: root.destroy())
        msg = Message(root, text=el)
        msg.config(font=('times', 100, 'italic bold underline'))
        msg.pack()
        
        # deuxième message optionnel
        msg1 = Message(root, text= subtitle)
        msg1.config(font=('times', 50))
        msg1.pack()
        
        root.mainloop()

"""
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------          INITIALIZING THE VARIABLES        ------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
"""

TONS = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'F#', 'B', 'E', 'A', 'D', 'G']
supl_tons = ['A#', 'D#', 'G#', 'C#', 'Gb']
TONS = TONS + supl_tons
#TONS = supl_tons
dic = compute_names(TONS)
triadesMaj = TONS
triadesMin = dic['triadesMin']
accordsMin7 = dic['accordsMin7']
accords7 = dic['accords7']
accordsMaj7 = dic['accordsMaj7']
accordsDemiDim = dic['accordsDemiDim']
accordsDim = dic['accordsDim']
accordsAugm = dic['accords_augm']

		
"""
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------          GETTING THE ARGUMENTS           ------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
"""

parser = argparse.ArgumentParser()
parser.add_argument('-m',
                    '--mode',
                    action="store",
                    dest="mode",
                    type=int,
                    help="Mode used for the training. For example, 3 is minor 7 chords, and 5 is major7 chords.")
parser.add_argument('-d',
                    '--delta',
                    action="store",
                    dest="delta_t",
                    type=float,
                    help="Time beetween 2 chords. The smaller, the harder the training is.")
parser.add_argument('-n',
                    '--nb_cycles',
                    action="store",
                    dest="nb_cycles",
                    type=int,
                    help="Number of times the list will be browsed.")
					
parser.add_argument('-s',
                    '--sleep_time',
                    action="store",
                    dest="sleep_time",
                    type=int,
					default = 10,
                    help="Number of times the list will be browsed.")

parser.add_argument('-t',
                    '--text',
                    action="store",
                    dest="subtitle",
                    type=str,
					default = "",
                    help="Subtitle to print while training.")

args = parser.parse_args()
mode = args.mode
delta_t = args.delta_t
nb_cycles = args.nb_cycles
sleep_time = args.sleep_time
subtitle = args.subtitle

"""
------------------------------------------------------------------------------------------------------------------------------
------------------------------------------            LAUNCHING TRAINING            ------------------------------------------
------------------------------------------------------------------------------------------------------------------------------
"""

print("\n\n" + "-------------------------------------------------------------------" * 5 + "\n\n")
print(f"You have asked this training :\n\nmode : {mode}     |       delta_t : {delta_t}        |  nb_cycles : {nb_cycles}   \n\n")
sleep(sleep_time)

try:
    train(mode = mode, dt = delta_t, nbRepetitions = nb_cycles, subtitle = subtitle)
except KeyboardInterrupt:
    print("                                                            INTERRUPTION OF TRAINING    ")
finally:
    print("\n\n" + "-------------------------------------------------------------------" * 5 + "\n\n")
