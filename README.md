# Making a Classification to trim unimportant pages from a document

To make the dataset, we need an xlxs file that contains the file name and the important pages. We download it from **Downloading.py** and edit the xlxs file according to our needs with **editingxlxs.py**

In **splitting.py** we split the document pages in folders named **important page** and **non importanage pages**.

In **create.py** we extract text from the documents and make the dataset.

Then in **train.py** we preprocess the dataset and make a ML algorithm and train it.

After the training, we can predict if a page is important or non important. We didnt show the trimming code here, we just predicted if a document is important or not. After that we can easity trim the unimportant ages.
