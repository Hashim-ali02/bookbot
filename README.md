# BookBot 📚

A Python-based text analysis tool that reads books and generates detailed statistical reports about word and character usage.
Overview

BookBot is a command-line application that analyzes text files (particularly books) and provides comprehensive statistics including:

    Total word count
    Character frequency analysis (sorted by occurrence)
    Formatted report generation

Features

    Word Counting: Accurately counts the total number of words in any text file
    Character Analysis: Tracks frequency of each alphabetical character
    Smart Sorting: Orders character statistics from most to least frequent
    Clean Output: Generates a beautifully formatted report with clear sections
    File Processing: Handles large text files efficiently

Project Structure

    bookbot/
    ├── main.py          # Main application entry point
    ├── stats.py         # Statistical analysis functions
    ├── books/           # Directory containing text files to analyze
    │   └── frankenstein.txt
    └── README.md        # This file

Sample Output

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
============= END ===============

How It Works

    Text Processing: Reads the specified text file and processes its contents
    Word Analysis: Counts total words using string manipulation techniques
    Character Frequency: Analyzes each character and tracks occurrence counts
    Data Sorting: Converts character data to a sortable format and orders by frequency
    Report Generation: Formats and displays the results in a clean, readable format

Technical Implementation

    Uses Python's built-in string methods for text processing
    Implements custom sorting functions for dictionary-based data structures
    Filters non-alphabetical characters using .isalpha() method
    Modular design with separate statistics and main modules

Usage

Run the application from the command line:

python3 main.py

The program will automatically analyze the default book file and display the statistical report.
Requirements

    Python 3.x
    Text file(s) to analyze (placed in the books/ directory)

Learning Objectives

This project demonstrates:

    File I/O operations in Python
    String manipulation and text processing
    Dictionary data structures and operations
    List sorting with custom key functions
    Modular programming and function organization
    Data analysis and reporting techniques

Future Enhancements

Potential improvements could include:

    Command-line arguments for specifying different files
    Support for multiple file formats
    Additional statistical metrics (sentence count, paragraph analysis)
    Export functionality (CSV, JSON output)
    Graphical visualization of character frequency

BookBot is my first [Boot.dev](https://www.boot.dev) project! This project was built as part of the Boot.dev Python course, focusing on practical application of core programming concepts.
