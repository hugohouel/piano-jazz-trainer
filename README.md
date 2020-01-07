# Piano Jazz Trainer

This piano jazz software allow the player to learn and memorize
* chords
* rootless chords 
* the 7 major modes 
* all intervals

Via command line, the player chooses what he want to practise among the 4 categories, and precise a time interval, d. 
Every d seconds, the program displays on the screen the symbol of the figure he has to play. 
Once the player gets confortable with d, he can then try with 0.9 * d, and so on, until he reaches a very quick response.

Rootless Chords : (called voicings) of 2, 3 or 4 notes

Modes Ionian, Dorian, Phrygian, Lydian, Mixolydian, Eolian and in all tonalities

## Getting Started

Clone the repository. Run the train.py file with your python3 interpreter, using the command line to pass 3 required arguments
* --mode or -m : describes what subject you want to train on (see the table below)
* --delta or -d : a number of seconds separating 2 displayed chords, modes, or intervals to play. The smaller, the more difficult
* --nb_cycles or -n : number of times you want to repeat the training

### Prerequisites

To make sure you have all the dependencies required in this project, go at the root and run

```
pip install -r requirements.txt
```

## Contributing

If you're a piano jazz player and feel like contributing, that's great! Contact me to discuss feature enriching / fix.

## Acknowledgments

I started this project in April 2019 to help me learn & memorize jazz chords and voicings. Hope it can help you too!
