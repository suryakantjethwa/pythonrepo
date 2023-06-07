import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/suryakantjethwa/Developer/Python/Python Research/iris_csv.csv')

print(data)

print(sns.heatmap(data))

print('1 =========================================================')

print(data.head())

print('2 =========================================================')

print(data.columns)

print('3 =========================================================')

print(data.shape)

print('4 =========================================================')

print(data[10:21])

print('5 =========================================================')

specific_data = data[["sepallength" , "class"]]
print(specific_data.head(10))

print('6 =========================================================')
data.iloc[5]
#it will display records only with species "Iris-setosa".
dataset = data.loc[data['class'] == 'Iris-setosa']
print(dataset)

print('7 =========================================================')
count = data["class"].value_counts()
print(count)




  

#heatm = sns.heatmap(data.corr(),camp = "YlGnBu", linecolor = 'white', linewidths = 1)
#print(heatm)


