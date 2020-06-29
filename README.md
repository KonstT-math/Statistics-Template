# Statistics-Template
A statistics template in python (pandas, scipy, matplotlib)


The stats_template.py script is for manipulating data in the form of a csv file. 

In particular, the important part is the 'data_by_classes' function which is used to split a testing variable into classes;
by creating a dataframe from a csv file filled with data, we are able to extract test data from particular groups of a categorical variable
in order to perform descriptive and inferencial statistics. The function 'data_by_classes' is in a general form and can be used for any csv file.

loads data from a csv file, stores them in a dataframe type

works out some descriptive statistics

performs normality test

performs hypothesis testing (up to now, Kruskal-Wallis and ANOVA depending on results from normality test)

works out the box plot for the data to be tested


