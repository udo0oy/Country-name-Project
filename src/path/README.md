# learning-from-data

We are making an algorithom using python.we have unsorted and mispelled country names in [google spreadsheet](https://docs.google.com/spreadsheets/d/1VcBcujda5q5zEpeAdUhCVqk-cYs7Vl_U_Xaq6Hh9ySg/edit?usp=sharing).
we will use levenshtein algorithom  so that we can have a correct set of data where all country names are reasonably correct and summarized as one country and respective count

## Getting Started
####Metaphone
[Metaphone] (https://en.wikipedia.org/wiki/Metaphone#Metaphone_3) is a phonetic algorithm, published by Lawrence Philips in 1990, for indexing words by their English pronunciation.[1] It fundamentally improves on the Soundex algorithm by using information about variations and inconsistencies in English spelling and pronunciation to produce a more accurate encoding, which does a better job of matching words and names which sound similar. As with Soundex, similar-sounding words should share the same keys. Metaphone is available as a built-in operator in a number of systems.

The original author later produced a new version of the algorithm, which he named Double Metaphone. Contrary to the original algorithm whose application is limited to English only, this version takes into account spelling peculiarities of a number of other languages. In 2009 Lawrence Philips released a third version, called Metaphone 3, which achieves an accuracy of approximately 99% for English words, non-English words familiar to Americans, and first names and family names commonly found in the United States, having been developed according to modern engineering standards against a test harness of prepared correct encodings.

####Levenshtein distance
In information theory, linguistics and computer science, the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other. It is named after the Soviet mathematician Vladimir Levenshtein, who considered this distance in 1965.
### Prerequisites

```
python v3
Gspread

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
