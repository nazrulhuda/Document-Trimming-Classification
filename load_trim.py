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


classifer_pickle = 'trim.pkl'




def do():
        #load dataset
        
        
        
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
        pred = target_names[clf_.predict(str_vector)[0]]
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
        pred = target_names[clf_.predict(str_vector)[0]]
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
        pred = target_names[clf_.predict(str_vector)[0]]
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
        pred = target_names[clf_.predict(str_vector)[0]]
        # use calibrated cv to calculate probabilities
        prob = model.predict_proba(str_vector)
        prob = max(prob[0])
        print(pred, prob)
        print("that was for solar")


################3



      




        

do()