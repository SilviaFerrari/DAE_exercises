import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns, warnings
warnings.filterwarnings('ignore')

# load the data from 
data = pd.read_csv("DAE_exercises\Awards_Best_Books\Good_Reads_Book_Awards_Crawl_2023_12_27_11_14.csv")
data.sample(5)

# drop some data colums that we don't need
data.drop(['source_URL','Book Description','About the Author'],axis=1, inplace=True)

# check the data types for each column and check the summary of the numerical columns
data.info()

# summary statistics for numerical columns
# average value, median values standard deviation, minimum, and maximum values 
data.describe()