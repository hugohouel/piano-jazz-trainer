# Piano Jazz Trainer

This piano jazz software allow the player to learn and memorize :
* chords
* rootless chords 
* the 7 major modes 
* all intervals

Via command line, the player chooses what he wants to practise among the 4 categories, and precise a time interval, d. 
Every d seconds, the program displays on the screen the symbol of the figure he has to play. 
Once the player gets confortable with d, he can then try with 0.9 * d, and so on, until he is able to play the right thing very quick.

## Getting Started

Clone the repository. Run the train.py file with your python3 interpreter, using the command line to pass 3 required arguments
* --mode or -m (int): describes what subject you want to train on (see the table below)
* --delta or -d (positive float): a number of seconds separating 2 displayed chords, modes, or intervals to play. The smaller, the more difficult
* --nb_cycles or -n (int): number of times you want to repeat the training

You also have at your disposal 2 optional arguments :
* --sleep_time or -s (positive float): defining, in seconds, the time before the training begins (10s by default, to let you the time to get ready)
* --text or -t (string): add some text on the screen

### Table for the mode

Here is the corresponding table between the mode and the chords to play on the keyboard.
* 0 : min Maj7 chords
* 1 : major triads
* 2 : minor triads
* 3 : min7
* 4 : 7
* 5 : maj7
* 6 : semi-diminished or min7b5
* 7 : diminished triads
* 8 : augmented triads
* 9 : major modes : Ionian, Dorian, Phrygian, Lydian, Mixolydian, Eolian and Locrian
* 10 : all intervals
* 11 : tritons
* 12 : 4th
* 13 : 6th min
* 14 : 6th maj
* 15 : 9th
* 16 : 11th
* 17 : 13th

### Example
To run the training, the user would for example type :
```
python train.py --mode 1 --delta 2 --nb_cycles 1
```
This would provide a training of major triads. The user would be displayed all 12 major triads once and would have to play one every 2 seconds.

## Prerequisites

To make sure you have all the dependencies required in this project, run

```
pip install -r requirements.txt
```

## Contributing

If you're a piano jazz player and feel like contributing, that's great! Contact me to discuss feature enriching / fix. Any comment on my code is more than welcomed.

## Acknowledgments

I started this project in April 2019 to help me learn & memorize jazz chords and voicings. Hope it can help you too!

## TO DO
* script to update my time paramter quickly
* agregation score tool - get a dashboard on my performances (the time parameters I am able to perform the programs with)
* docker package - to deploy easily
* mobile/web version - to have access everywhere
