from sklearn.neural_network import MLPClassifier
import cPickle as p

f=open("OCRDataset.obj",'rb')
data=p.load(f)
x=[]
y=[]
for i in range(780):
	x.append(data[i][0])
	y.append(data[i][1])
clf=MLPClassifier(solver='sgd', alpha=1e-5,hidden_layer_sizes=(400,10),max_iter=10000000,activation='logistic')
clf.fit(x,y)
res=clf.predict(x)
count=0
for i in range(780):
	if res[i]==y[i]:
		count+=1
print float(count)/780
f=open("OCRNetwork.obj",'w')
p.dump(clf,f,-1)
