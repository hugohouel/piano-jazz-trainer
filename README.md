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

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
