import re
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.calibration import CalibratedClassifierCV
from sklearn.datasets import load_files
import fitz
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
#####for the whole one
X_train = None
X_test = None
y_train = None
y_test = None
vectorizer = None
target_names = None

def data_cleaning(text):
    """
    Method to perform data cleaning
    Removes punctuations and numbers from text

    Parameters
    ----------
    text : str
        The full corpus in the pdf/jpg.

    Returns
    -------
    str
        The cleaned text with punctuations and numbers removed from text.

    """
    punc = '''!()[]{};:'",<>./?@#$%^&*_~\\'''
    text = text.translate(str.maketrans("","", punc))
    return re.sub(r' \d\d*', "", text.lower())

# one glabal variable to define 'clf.pkl'

classifer_pickle = 'trim.pkl'




def do():
        #load dataset
        dataset = load_files('/home/tirzok/dataset',
                             encoding="ISO-8859-1" , shuffle=True)
        
        #clean data
        for index, data in enumerate(dataset.data):
            dataset.data[index] = data_cleaning(data)
        
        target_names = dataset.target_names
        print(target_names)
        
        print("entered 1")
        X_train, X_test, y_train, y_test = \
        train_test_split(dataset.data, dataset.target, test_size=0.3,
                         random_state=42, stratify=dataset.target)
        print("entered 2")
        vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.7,
                                          min_df=1, stop_words="english",
                                          lowercase=True, ngram_range=(1,3))
        print("entered 3")
        X_train = vectorizer.fit_transform(X_train)
        print("entered 4")
        X_test = vectorizer.transform(X_test)
        print("entered 5")




        from sklearn.linear_model import SGDClassifier
        from sklearn.model_selection import GridSearchCV
        tuned_parameters = {
                            'loss': ['hinge'],
                            'penalty': ['l2','l1'],
                            'alpha': [10 ** x for x in range(-6, 1)]
                           }
        clf = SGDClassifier(alpha=0.0001, max_iter=100, penalty='l2',
                            class_weight="balanced")
        clf = GridSearchCV(clf, tuned_parameters, cv=5)
        clf.fit(X_train, y_train)

        pred = clf.predict(X_test)
        score = metrics.accuracy_score(y_test, pred)
        print("accuracy:   %0.3f" % score)

        model = CalibratedClassifierCV(clf)
        model.fit(X_train, y_train)

        print("classification report:")
        print(metrics.classification_report(y_test, pred,
                                            target_names=target_names))
        
        


        data = {'clf': clf, 'model': model, 'X_train':X_train,
                'y_train':y_train, 'target_names':target_names, 'vectorizer':vectorizer}


            
        with open(classifer_pickle, 'wb') as file2:
            pickle.dump(data, file2)
            
        
        
################3



        with open("/home/shanto/Downloads/sdsd/test/dataset/important/013122 Bank Statement_page1.txt", 'r') as file:            
            text=file.read()
        

        #with fitz.open("/home/shanto/Downloads/sdsd/important/03_KT_W2_2020_page1.pdf") as doc:            
           # text = ""
           # for page in doc:
             #   text += page.get_text()


                

        
        string = text
        with open(classifer_pickle, 'rb') as file:
            clf = pickle.load(file)
        clf_ = clf['clf']
        model = clf['model']
        target_names=clf['target_names']
        vectorizer=clf['vectorizer']
        string = data_cleaning(text)
        str_vector = vectorizer.transform([string])
        pred = dataset.target_names[clf_.predict(str_vector)[0]]
        # use calibrated cv to calculate probabilities
        prob = model.predict_proba(str_vector)
        prob = max(prob[0])
        print(pred, prob)
        print("that was for bank statement")

################3



        with open("/home/shanto/Downloads/sdsd/test/dataset/important/08_KT_1620_HOA_Bill_20220430_page1.txt", 'r') as file:            
            text=file.read()
        

        #with fitz.open("/home/shanto/Downloads/sdsd/important/03_KT_W2_2020_page1.pdf") as doc:            
           # text = ""
           # for page in doc:
             #   text += page.get_text()


                

        
        string = text
        with open(classifer_pickle, 'rb') as file:
            clf = pickle.load(file)
        clf_ = clf['clf']
        model = clf['model']
        target_names=clf['target_names']
        vectorizer=clf['vectorizer']
        string = data_cleaning(text)
        str_vector = vectorizer.transform([string])
        pred = dataset.target_names[clf_.predict(str_vector)[0]]
        # use calibrated cv to calculate probabilities
        prob = model.predict_proba(str_vector)
        prob = max(prob[0])
        print(pred, prob)
        print("that was for HOA")

################3



        with open("/home/shanto/Downloads/sdsd/test/dataset/important/1040__tax_return_20210912130606_page1.txt", 'r') as file:            
            text=file.read()
        

        #with fitz.open("/home/shanto/Downloads/sdsd/important/03_KT_W2_2020_page1.pdf") as doc:            
           # text = ""
           # for page in doc:
             #   text += page.get_text()


                

        
        string = text
        with open(classifer_pickle, 'rb') as file:
            clf = pickle.load(file)
        clf_ = clf['clf']
        model = clf['model']
        target_names=clf['target_names']
        vectorizer=clf['vectorizer']
        string = data_cleaning(text)
        str_vector = vectorizer.transform([string])
        pred = dataset.target_names[clf_.predict(str_vector)[0]]
        # use calibrated cv to calculate probabilities
        prob = model.predict_proba(str_vector)
        prob = max(prob[0])
        print(pred, prob)
        print("that was for tax returns")

################3



        with open("/home/shanto/Downloads/sdsd/test/dataset/important/10_KT_Solar_Lease_4073_page1.txt", 'r') as file:            
            text=file.read()
        

        #with fitz.open("/home/shanto/Downloads/sdsd/important/03_KT_W2_2020_page1.pdf") as doc:            
           # text = ""
           # for page in doc:
             #   text += page.get_text()


                

        
        string = text
        with open(classifer_pickle, 'rb') as file:
            clf = pickle.load(file)
        clf_ = clf['clf']
        model = clf['model']
        target_names=clf['target_names']
        vectorizer=clf['vectorizer']
        string = data_cleaning(text)
        str_vector = vectorizer.transform([string])
        pred = dataset.target_names[clf_.predict(str_vector)[0]]
        # use calibrated cv to calculate probabilities
        prob = model.predict_proba(str_vector)
        prob = max(prob[0])
        print(pred, prob)
        print("that was for solar")


################3



      




        

do()