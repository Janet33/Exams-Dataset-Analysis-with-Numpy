# Import the pandas library
# import libraries

import pandas as pd
# load data
exam_grades = pd.read_csv('exam_grades.csv')

# convert data to a pandas dataframe, fcreatimg dataframe
exam_grades = pd.DataFrame(exam_grades)
exam_grades

# shape of data
exam_grades.shape

#descriptive statistics
exam_grades.describe()

# How many rows and columns are in the dataset?
# number of rows and columns
exam_grades.info()   #we have 50 rows and 3 columns  #N.B: Grade has 45 entries meaning there are missing values

# How many unique student IDs are in the dataset?
# number of unique student IDs
exam_grades['student_id'].value_counts()  #we have 10 student unique IDs, each having written 5 exams

# number of unique student IDs
exam_grades['student_id'].nunique() #we have 10 unique student IDs

# What is the list of unique student IDs in the dataset?
# list of unique student IDs
list(exam_grades.student_id.unique())

# How many missing grades are there across all exams in the dataset? Remember that a missing value would be represented as NaN in python.
# check if there are any missing values in any column
exam_grades.isnull().sum()   #there are 5 missing grades across all exams in the dataset

# number of missing values in general
exam_grades['grade'].isnull().value_counts()    #we have 5 missing values

# Let’s say: The dataset represents a gradebook, containing students’ exam grades in a particular class. 
# The protocol is that when a student doesn’t make up an exam they missed, their missing grade needs to be replaced with a zero at the end of the term. 
# If you noticed any missing exam grades in the dataset, replace them with zeros, to reflect the class protocol. Make sure to finish this before proceeding.

# fill NaNs with zero
exam_grades['grade'].fillna(0, inplace=True)
exam_grades

# How many exam grades are passing (i.e. greater than or equal to 70)?
# displaying students that had exams grades greater than or equal to 70 in specific exams
exam_grades.loc[exam_grades['grade'] >= 70]  

# number of exams grades greater than or equal to 70
len(exam_grades.loc[exam_grades['grade'] >= 70])  #42 exam grades were greater or equal to 70

# What is the mean grade for exam 1, 2, 3, 4 & 5?
# group by exam column and find grades mean 
exam_grades.groupby('exam')['grade'].mean()  #the mean grade for each exam after missing values have been replaced with 0

# means when found on grades with missing values
original_data = pd.read_csv('exam_grades.csv')
original_data
original_data.groupby('exam')['grade'].mean()

# groupby exam number and display keys
exam_grades.groupby('exam').groups.keys()

# Import the pyplot module in matplotlib’s library and give it the alias of plt, to keep things short and sweet.
# To visualize the distribution of the exam grades, create a histogram.

plt.hist(exam_grades, bins=15, alpha=0.5,
         histtype='stepfilled');
plt.xlabel('Exam grade')
plt.ylabel('Frequency')
plt.title('Distribution of Exam Grades')

plt.show()
