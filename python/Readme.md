# Introduction
This folder contains a collection of six Python scripts and a supporting .txt file. Each script serves a unique purpose, 
showcasing various functionalities and applications of Python programming. Below is a brief description of each script:

## interval.py
This Python program calculates the maximum and minimum intervals from a list of spaces provided by the user.
A space is defined as a pair of start and end points, and the program finds the space or spaces with the longest
and shortest lengths based on these intervals.

## matrixMax.py
This is a Random Matrix Generator with Maximum Element Finder. A Python program which generates a random matrix based 
on user input and then calculates and displays the maximum element in the matrix.

## matrixOnes.py
An Identity Matrix Generator with Error Handling. This Python script generates and displays an identity matrix.
An identity matrix is a square matrix where all diagonal elements are '1's, and all other elements are '0's. The 
user specifies the number of '1's in the matrix.

## root.py
A Digital Root Calculator with Iterated Summing. This program calculates the digital root of a given integer using 
iterative digit summing. The digital root is the repeated sum of the digits of a number until a single-digit result
is obtained.

## statistics.py
A Letter Appearance Statistics Program. This Python script reads the contents of a text file, calculates the appearance 
statistics for each letter, and displays the results in ascending order by count.

## store.py
This is a record store application. Program Name: Best Metal Albums Store.
Description: This Python program manages a list of the best metal albums. It allows users to add, search, display, and 
delete albums from a list stored in the 'store.txt' file. The program provides a simple menu-based interface for interacting 
with the album records.

Usage:
    - Run the program from the command line with: python store.py
    - Follow the on-screen menu to select options for adding, searching, displaying, or deleting albums.
    - The program reads from and writes to the 'store.txt' file to persist the album data.

Functions:
    - delete_album(recordList, keyword): Deletes an album from the list based on a keyword and updates 'store.txt'.

Additionally, the 'store.tx't file is used by some of the scripts to read from and write data to, ensuring data persistence across sessions.
