from sklearn.neural_network import MLPClassifier
import cPickle as p
import sys

def classify(data,char):
	x=[]
	y=[]
	clf={}
	
	#for all the alphabets in char
	for ch in char:
		print ch
		x=[];y=[]
		#for a alphabet 10 font styles with three different sizes
		for i in range(0,30):
			#x to hold all the features of a letter
			x.append(data[ch][i][0])
			#y to hold responses
			y.append(data[ch][i][1])
		#multi layer perceptron for each character
		clf[ch]=MLPClassifier(solver='sgd', alpha=1e-5,hidden_layer_sizes=(400,10),max_iter=10000000,activation='logistic')
		clf[ch].fit(x,y)
		res=clf[ch].predict(x)
		count=0
		for i in range(len(res)):
			if res[i]==y[i]:
				count+=1
		print float(count)/len(res)
	#to pickle the classifier
	f1=open("Classifier.obj","w")
	p.dump(clf,f1,-1)


def main():
	f=open("FontStyle.obj","rb")
	data=p.load(f)
	char='abcdefghijklmnopqrstuvwxyz'
	classify(data,char)


main()
