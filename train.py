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

MAJOR_TONES = [
    'C', 'F', 'Bb',
    'Eb', 'Ab', 'Db',
    'Gb', 'F#', 'G',
    'D', 'A', 'E',
    'B'
]

MINOR_TONES = [
    'A', 'D', 'G',
    'C', 'F', 'Bb',
    'Eb', 'D#', 'E',
    'B', 'F#', 'C#',
    'G#'
]

MAJOR_MODES_NAMES = [
    'Ionian', 'Dorian', 'Phrygian',
    'Lydian', 'Mixolydian', 'Eolian',
    'Locrian'
]

INTERVALS = [
    'b9', '9th', 'min 3rd',
    'Maj 3rd', '11th', 'b5',
    '5th', 'b13', ' 13th',
    'min 7th', 'Maj 7th'
    ]


def name_to_content(name: str):
    mapping_name_content = {

        # Intervalles, modes et armures
        'major_tones': MAJOR_TONES,
        'minor_tones': [t + '-' for t in MINOR_TONES],
        'major_modes': [tone + ' ' + m for tone in TONES for m in MAJOR_MODES_NAMES],
        'all_intervals': [interval + '\n of \n ' + tone for interval in INTERVALS for tone in TONES],
        'triton': ['b5 of \n ' + e for e in TONES],
        '11th': ['11th of \n ' + e for e in TONES],
        '9th': ['9th of \n ' + e for e in TONES],
        '11th': ['11th of \n ' + e for e in TONES],
        '13th': ['13th of \n ' + e for e in TONES],
        'minor_13th': ['b13 of \n ' + e for e in TONES],
        'all_13th': ['13th of \n ' + e for e in TONES] + ['b13 of \n ' + e for e in TONES],

        # Triades
        'major_triads': TONES,
        'minor_triads': [e + '-' for e in TONES],
        'diminished': [e + ' °' for e in TONES],
        'augmented': [e + ' aug' for e in TONES],

        # Accords non altérés
        'minor_major_7': [e + ' mM7' for e in TONES],
        'minor_7': [e + '-7' for e in TONES],
        '7': [e + '7' for e in TONES],
        'major_7': [e + 'Maj7' for e in TONES],
        'semi_diminished': [e + ' Ø' for e in TONES],
        'minor_6_chord': [e + '-6' for e in TONES],
        'sus': [e + ' sus' for e in TONES],
        'phryg': [e + ' Phryg' for e in TONES],
        'min11': [e + ' min11' for e in TONES],

        # Accords altérés
        '7_b9': [e + '7 b9' for e in TONES],
        '7_#9': [e + '7 #9' for e in TONES],
        '7_#11': [e + '7 #11' for e in TONES],
        '7_b13': [e + '7 b13' for e in TONES],
        '7_b9_b13': [e + '7 b9 b13' for e in TONES],
        'major7_#11': [e + ' Maj7 #11' for e in TONES],
        'major7_#5': [e + ' Maj7 #5' for e in TONES]
    }

    return mapping_name_content[name]


def mode_to_name(var_mode: int) -> list:

    mapping_mode_name = {
        # Intervalles, modes et armures
        '9': 'major_modes',
        '10': 'all_intervals',
        '11': 'triton',
        '12': '11th',
        '13': 'minor_13th',
        '15': 'major_tones',
        '16': 'minor_tones',
        '17': '13th',
        '19': 'all_13th',

        # Triades
        '1': 'major_triads',
        '2': 'minor_triads',
        '7': 'diminished',
        '8': 'augmented',

        # Accords non altérés
        '0': 'minor_major_7',
        '3': 'minor_7',
        '4': '7',
        '5': 'major_7',
        '6': 'semi_diminished',
        '14': 'minor_6_chord',
        '21': 'sus',
        '27': 'phryg',
        '28': 'min11',

        # Accords altérés
        '24': '7_b9',
        '20': '7_#9',
        '25': '7_#11',
        '26': '7_b13',
        '18': '7_b9_b13',

        '22': 'major7_#11',
        '23': 'major7_#5'
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
                        help="Sleep time before launching training.")

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

    double_line = "\n\n" + "-" * 422 + "\n\n"

    print(double_line)
    print(f"You have asked this training :\n\nmode : {mode_to_name(mode)}     |"
          f"       delta_t : {delta_t}        |"
          f"       nb_cycles : {nb_cycles}   \n\n")

    sleep(sleep_time)

    try:
        train(mode=mode, dt=delta_t, nb_repetitions=nb_cycles, subtitle=subtitle)
    except KeyboardInterrupt:
        print("                                                            INTERRUPTION OF TRAINING    ")
    finally:
        print(double_line)
