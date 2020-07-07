
# a python (pandas, scipy, matplotlib) tutorial - template

# a statistics tutorial in python
# loads data from a csv file, stores them in a dataframe type
# works out some descriptive statistics
# performs normality test
# performs hypothesis testing (up to now, Kruskal-Wallis and ANOVA and post hoc tests)
# works out the box plot for the data to be tested
# the data by classes function is used to split a testing variable into classes

# imports..
import pandas as pd
import scipy.stats as stats
from scipy.stats import kruskal, f_oneway

import matplotlib.pyplot as plt  
#% matplotlib inline 


# ------------------------------------------------------

# splits the test variable x into groups (in terms of the factor variable y)
def data_by_classes(data, ny, nx):
	
	yName = data.columns[ny]
	y = data[yName]
	yy = y.unique()

	print("\n\nGroups: \n")
	for i in range(len(yy)):
		print("{} - {}\n".format(i,yy[i]))
	print("\n")

	# extract the categories from y, along with 
	# companion values for all other variables:
	Y=[]
	for i in range(len(yy)):
		Y.append(data[data[yName] == yy[i]])

	xName = data.columns[nx]

	# extract the test variable values from each category
	X=[]
	for i in range(len(yy)):
		X.append(Y[i][xName])

	return X


# Hypothesis testing:
def hypo_test(data, nx, X):

	xName = data.columns[nx]
	x = data[xName]

	# Shapiro-Wilk for normality testing
	print("Shapiro-Wilk normality test:")
	s, pSW = stats.shapiro(x)
	print("P-value:",pSW)

	if pSW < 0.05:
		print("Kruskal Wallis H-test:")
		H, pval = kruskal(*X)
		print("H-statistic:", H)
		print("P-Value:", pval)

		if pval < 0.05:
			print("Reject NULL hypothesis - Significant differences exist between groups.")
			
			# post-hoc for Kruskal-Wallis:
			if (len(X)>2):
				print("\nPost-hoc:\n")
				for i in range(len(X)):
					for j in range(i+1,len(X)):
						print("\nKruskal Wallis H-test:")
						H, pval = kruskal(X[i],X[j])
						print("H-statistic:", H)
						print("P-Value:", pval)
						if pval<0.05:
							print("Reject NULL hypothesis - Significant differences exist between groups: ( {} , {} )".format(i,j))

		else:
			print("Accept NULL hypothesis - No significant difference between groups.")

	else:
		print("One-way ANOVA test:")
		F, pval = f_oneway(*X)
		print("F-statistic:", F)
		print("P-Value:", pval)

		if pval < 0.05:
			print("Reject NULL hypothesis - Significant differences exist between groups.")

			# post-hoc for One-way Anova:
			if (len(X)>2):
				print("\nPost-hoc:\n")
				for i in range(len(X)):
					for j in range(i+1,len(X)):
						print("\nOne-way Anova test:")
						F, pval = f_oneway(X[i],X[j])
						print("F-statistic:", F)
						print("P-Value:", pval)
						if pval<0.05:
							print("Reject NULL hypothesis - Significant differences exist between groups: ( {} , {} )".format(i,j))

		else:
			print("Accept NULL hypothesis - No significant difference between groups.")
		
				 


# ------------------------------------------------------

# Load dataset
#path_file = "/path/tofile"
path_file = "iris.csv"
# if the csv file has no column names, one may use the following way to set them:
# for iris.csv:
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

df = pd.read_csv(path_file, names=names)

# or..
#path_file = input("Select file: ")
#df = pd.read_csv(path_file)

# shape of dataframe (if needed)
#print(df.shape)


# ------------------------------------------------------
# descriptive statistics:
print(df.describe())

# ------------------------------------------------------
# inferential statistics:

print("\n---------")
print("We will perform a Shapiro-Wilk test for a testing variable.\nThen, we perform a Kruskal-Wallis or a one-way ANOVA test,\ndepending on the test variable's distribution.\nPost-hoc tests will follow if necessary.")
print("\n---------")

flag = 0

while (flag == 0):
	# one test variable in each run:
	nx = int(input("Enter the index of the testing variable:"))
	ny = int(input("Enter the index of the factor variable:"))

	Xdata = data_by_classes(df, ny, nx)
	hypo_test(df, nx, Xdata)
	
	df.boxplot(by =df.columns[ny], column =[df.columns[nx]], grid = False) 

	plt.show()

	print("\n---------")
	q = input("Type (y) if you want to conduct more testing.")
	print("\n---------")
	if (q != 'y'):
		flag = 1




