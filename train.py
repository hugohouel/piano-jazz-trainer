from time import sleep
from random import choice
from math import floor
import argparse
from tkinter import Tk, Label, Message

TONES = [
    'C', 'F', 'Bb',
    'Eb', 'Ab', 'Db',
    'F#', 'B', 'E',
    'A', 'D', 'G',
    'A#', 'D#', 'G#',
    'C#', 'Gb'
]

MAJOR_MODES_NAMES = [
    'Ionian', 'Dorian', 'Phrygian',
    'Lydian', 'Mixolydian', 'Eolian',
    'Locrian'
]

INTERVALS = [
    'minor 2th', 'major 2th', 'minor 3rd',
    'major 3rd', '4th', 'triton',
    '5th', 'minor 6th', ' major 6th',
    'minor 7th', 'major 7th'
]


def name_to_content(name: str):
    mapping_name_content = {
        'minor_major_7': [e + ' mM7' for e in TONES],
        'major_triads': TONES,
        'minor_triads': [e + '-' for e in TONES],
        'minor_7': [e + '-7' for e in TONES],
        '7': [e + '7' for e in TONES],
        'major_7': [e + 'Maj7' for e in TONES],
        'semi_diminished': [e + ' Ø' for e in TONES],
        'diminished': [e + ' °' for e in TONES],
        'augmented': [e + ' aug' for e in TONES],
        'major_modes': [tone + ' ' + m for tone in TONES for m in MAJOR_MODES_NAMES],
        'intervals': [interval + '\n of \n ' + tone for interval in INTERVALS for tone in TONES],
        'triton': ['Triton of \n ' + e for e in TONES],
        '4th': ['4th of \n ' + e for e in TONES],
        'minor_6th': ['minor 6th of \n ' + e for e in TONES],
        'major_6th': ['major 6th of \n ' + e for e in TONES],
        '9th': ['9th of \n ' + e for e in TONES],
        '11th': ['11th of \n ' + e for e in TONES],
        '13th': ['13th of \n ' + e for e in TONES],
        '7_b9_b13': [e + '7 b9 b13' for e in TONES]
    }

    return mapping_name_content[name]


def mode_to_name(var_mode: int) -> list:

    mapping_mode_name = {
        '0': 'minor_major_7',
        '1': 'major_triads',
        '2': 'minor_triads',
        '3': 'minor_7',
        '4': '7',
        '5': 'major_7',
        '6': 'semi_diminished',
        '7': 'diminished',
        '8': 'augmented',
        '9': 'major_modes',
        '10': 'intervals',
        '11': 'triton',
        '12': '4th',
        '13': 'minor_6th',
        '14': 'major_6th',
        '15': '9th',
        '16': '11th',
        '17': '13th',
        '18': '7_b9_b13'
    }

    return mapping_mode_name[str(var_mode)]


def train(mode: int, dt, nb_repetitions=2, subtitle=""):
    """ Display chords every dt seconds. Once all the chords have been played once, another round can begin."""

    my_list = name_to_content(mode_to_name(mode))
    elements_already_chosen = []
    n = len(my_list)

    for i in range(nb_repetitions * n):

        if len(elements_already_chosen) == n:
            elements_already_chosen = []

        el = choice(my_list)

        # Check that the element has not been played already in the current cycle.
        while el in elements_already_chosen:
            el = choice(my_list)

        # Update list of already played elements
        elements_already_chosen.append(el)

        # Display
        root = Tk()
        root.attributes('-fullscreen', True)
        root.after(floor(dt * 1000), lambda: root.destroy())
        msg = Message(root, text=el)
        msg.config(font=('times', 100, 'italic bold underline'))
        msg.pack()

        # Optional message
        msg1 = Message(root, text=subtitle)
        msg1.config(font=('times', 50))
        msg1.pack()

        root.mainloop()


if __name__ == "__main__":

    # Parse arguments

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
                        default=10,
                        help="Number of times the list will be browsed.")

    parser.add_argument('-t',
                        '--text',
                        action="store",
                        dest="subtitle",
                        type=str,
                        default="",
                        help="Subtitle to print while training.")

    args = parser.parse_args()
    mode = args.mode
    delta_t = args.delta_t
    nb_cycles = args.nb_cycles
    sleep_time = args.sleep_time
    subtitle = args.subtitle

    # Launch training

    print("\n\n" + "-------------------------------------------------------------------" * 5 + "\n\n")
    print(f"You have asked this training :\n\nmode : {mode}     |       delta_t : {delta_t}        |  nb_cycles : {nb_cycles}   \n\n")
    sleep(sleep_time)

    try:
        train(mode=mode, dt=delta_t, nb_repetitions=nb_cycles, subtitle=subtitle)
    except KeyboardInterrupt:
        print("                                                            INTERRUPTION OF TRAINING    ")
    finally:
        print("\n\n" + "-------------------------------------------------------------------" * 5 + "\n\n")
