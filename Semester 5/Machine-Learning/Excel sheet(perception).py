#Training....

#load data(excel sheet)
import pandas as pd
excel_file=pd.read_csv("/content/irisexcel.csv")
x=excel_file[["sepal_length","sepal_width","petal_length","petal_width"]]
y=excel_file["species"]


#load model(perceptron)
from sklearn.linear_model import Perceptron
model=Perceptron()

#fit data into model
model.fit(x,y)


#Testing.........
op=model.predict([[1.2,1.3,1.6,6.7]])
print(op)
