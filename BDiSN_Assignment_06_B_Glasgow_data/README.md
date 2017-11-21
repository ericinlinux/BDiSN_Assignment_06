# Part B: Glascow research on smoking habits in teenagers

The second part of the assignment comprises the run of a contagion model over a data set of teenagers and smoking habits.

All the data was taken from [Description 'Teenage Friends and Lifestyle Study' data](https://www.stats.ox.ac.uk/~snijders/siena/Glasgow_data.htm).

This folder contains the data and the Python code for the data set provided at http://tinyurl.com/hunndyg

----

The purpose of this assignment is to understand how you can model the dynamics of the edges in a social network using the homophily principle. For that,   you will have a data set provided and a modeling template based on functions   coded in Python that will run the model and relate it to the given data    set. (Blankendaal et al, 2016) developed a temporal-causal model for the homophily and more-becomes-more principle combined and tested it using simulations and the same data set you have to use in this assignment, but using the opinion about alcohol drink, instead of tobacco.

Homophily is a principle coined in social sciences that claims that people that share similar traits/opinions/emotions have a higher change of getting a stronger connection. The principle is also known as ‘birds of a feather flock together’. The homophily principle can be used to address the strength of the connections in many situations. People with similar political positions tend to be in clusters, as some studies have shown (Conover, 2011; Aral,   
2012), and this can be extended to social-economic status, educational level   and other traits, besides opinions, feelings and sentiments.

In the data set used, data was collected from 160 students in a window of 3 years. The participants were interviewed once per year, with 3 data points in total. The challenge is to create a model that tries to approximate the evolution over time of both the states and the connections as shown in the data. Remember that in such cases Dt  and the speed   factors h   
should  have    values  that    provide a   good    relation    to  the experiment. So  in  this    assignment, 
you have    to  be  sensitive   to  this    constraint  and try to  use the best    values  trying  to  fit the 
model   as  best    as  possible.       


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
