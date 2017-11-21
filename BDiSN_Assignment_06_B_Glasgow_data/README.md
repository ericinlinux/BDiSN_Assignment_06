# Part B: Glascow research on smoking habits in teenagers

The second part of the assignment comprises the run of a contagion model over a data set of teenagers and smoking habits.

All the data was taken from [Description 'Teenage Friends and Lifestyle Study' data](https://www.stats.ox.ac.uk/~snijders/siena/Glasgow_data.htm).

This folder contains the data and the Python code for the data set provided at http://tinyurl.com/hunndyg

----


## The matrix of friendships

We have three matrices with the question about the relations in 3 different years.

The data are valued; code 1 stands for "best friend", code 2 for "just a friend", and code 0 for "no friend".
Code 10 indicates structural absence of the tie, i.e., at least one of the involved students was not yet part of the
school cohort, or had already left the school cohort at the given time point.

For this work, we will make the following changes:

* code 1 = 0.9
* code 2 = 0.5
* code 10 = 0
* code 0 = 0.1

## The information about smoking habits

Tobacco use has the scores 1 (non), 2 (occasional) and 3 (regular, i.e. more than once per week). So for this pattern
the values are initialized with values 0.1, 0.5 and 0.9 respectively.

The idea of this code is to simulate the opinion change over time according to the initial values and the network
provided by the data set.

## The assignment

The document for the assignment is [here](Assignment06v2.pdf).
