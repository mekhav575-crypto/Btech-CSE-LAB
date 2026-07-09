#Training....

#load data(our own data)
x=[[1,1],[3,6],[24,45],[28,35]]
y=["boy","girl","girl","boy"]


#load model(perceptron)
from sklearn.linear_model import Perceptron
model=Perceptron()

#fit data into model
model.fit(x,y)


#Testing.........
op=model.predict([[5,9]])
print(op)
