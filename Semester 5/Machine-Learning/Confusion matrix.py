#Training....

#load data(excel sheet)
import pandas as pd
excel_file=pd.read_csv("/content/irisexcel.csv")
x=excel_file[["sepal_length","sepal_width","petal_length","petal_width"]]
y=excel_file["species"]

######cross validation
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)

#load model(perceptron)
from sklearn.linear_model import Perceptron
model=Perceptron()

#fit data into model
model.fit(xtrain,ytrain)

#######validation test
op=model.predict(xtest)
from sklearn.metrics import accuracy_score
score=accuracy_score(ytest,op)
print("Accuracy=",score*199)

#Testing.........
op2=model.predict([[1.2,1.3,1.6,6.7]])
print(op2)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(ytest,op)
print(cm)


cmd= ConfusionMatrixDisplay(confusion_matrix=cm,

                              display_labels=model.classes_)
cmd.plot()
