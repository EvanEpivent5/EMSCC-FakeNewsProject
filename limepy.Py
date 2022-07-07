import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import feature_extraction, linear_model, model_selection, preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.utils import shuffle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy
from lime import lime_tabular
import string
import nltk
from nltk.corpus import stopwords
import random
from sklearn.naive_bayes import MultinomialNB

# Data Preprocessing

def preprocessing(fake=pd.read_csv("True.csv"),true=pd.read_csv("True.csv")):
    fake['target'] = 'fake'
    true['target'] = 'true'
    data = pd.concat([fake, true]).reset_index(drop = True)
    data.drop(["date"],axis=1,inplace=True)
    data.drop(["title"],axis=1,inplace=True)
    data['text'] = data['text'].apply(lambda x: x.lower())

    def punctuation_removal(text):
        all_list = [char for char in text if char not in string.punctuation]
        clean_str = ''.join(all_list)
        return clean_str

    data['text'] = data['text'].apply(punctuation_removal)
    nltk.download('stopwords')
    stop = stopwords.words('english')
    data['text'] = data['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    #print('data lenght = ',len(data))
    print('lenfake = ',lenfake)
    print('lentrue = ',lentrue)

    return(data,lenfake,lentrue)

def dataproc(data,nbfake,nbtrue,lenfake,lentrue):
    #print(data)
    if nbfake>=(lenfake-1):
        print('Not enough fake news in dataset')
    if nbtrue>=(lentrue-1):
        print('Not enough true news in dataset')
    print(len(data))
    a=random.sample(range(0, lenfake), nbfake)
    b=random.sample(range(lenfake+1, len(data)-1), nbtrue)
    #print(b)
    print(' b = ',b)
    d=data.iloc[a][:]
    print(" a = ", a)

    print("data = ",data)
    e=data.iloc[b][:]
    
    data2=pd.concat([d,e], axis=0)

    X_train,X_test,y_train,y_test = train_test_split(data2['text'],data2.target,test_size=0.2,random_state=42)

    return(X_train,X_test,y_train,y_test)


def vecto(X_train,X_test):
    
    X_t=pd.concat([X_train,X_test])
    #print('X_t = ',X_t.shape)
    ltotal=len(X_t)
    #print(X_t)
    vectorizer = TfidfVectorizer(lowercase=False)
    v = vectorizer.fit_transform(X_t)

    features=vectorizer.get_feature_names_out()
    ltrain=len(X_train)
    vtrain=v[0:ltrain][:]
    vtest=v[ltrain:][:]
    vtrain=scipy.sparse.csr_matrix.toarray(vtrain)
    vtest=scipy.sparse.csr_matrix.toarray(vtest)

    return(vtrain,vtest,vectorizer,features)
    
def classifLogReg(vtrain,vtest,y_train,y_test):
    mo=LogisticRegression()
    mo.fit(vtrain,y_train)
    m=mo.predict(vtest)
    m=np.array(m)
    y_test=np.array(y_test)
    #print(y_test)
    #print(m)

    #print("accuracy: {}%".format(round(accuracy_score(y_test, m)*100,2)))
    return(round(accuracy_score(y_test, m)*100,2))

def classifNaiveBayes(vtrain,y_train,vectorizer,X_test,features):
    mo=MultinomialNB()
    mo.fit(vtrain,y_train)

    i=X_test.index
    j=i[1]

    o=pd.Series(X_test[j])
    o=vectorizer.transform(o)
    o=scipy.sparse.csr_matrix.toarray(o)
    o=o[0]

    explainer = lime_tabular.LimeTabularExplainer(vtrain,mode="classification",categorical_features=features,feature_names=features)
    exp=explainer.explain_instance(data_row=o,predict_fn=mo.predict_proba, num_features=20) #labels=features
    exp.as_pyplot_figure()
    from matplotlib import pyplot as plt
    plt.tight_layout()
    exp.show_in_notebook()
    return(j,exp)

def limenaivebayes(nbfake,nbtrue):
    data,lenfake,lentrue=preprocessing()
    
    x1=dataproc(data,nbfake,nbtrue,lenfake,lentrue)
    X_train=x1[0]
    X_test=x1[1]
    y_train=x1[2]
    y_test=x1[3]
    vtrain,vtest,vectorizer,features=vecto(X_train,X_test)
    #classifNaiveBayes(vtrain,y_train,vectorizer,X_test,features)
    j,exp=classifNaiveBayes(vtrain,y_train,vectorizer,X_test,features)
    #print('Texte classé = ',X_test[j])

    outputs = open("outputs.txt", "w")
    outputs.write("Texte classé = ")
    outputs.write(X_test[j])
    #outputs.write(exp)
    outputs.write("/n")
    outputs.close()
    



