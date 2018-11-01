NAME: saichand bandarupalli
CWID: 10803926
 
Programming language: python 3.6
running: open the naive_bayes.py file in IDE
Train and test data: sorted data folder holds the train and the test data
For classification: copy the test and train instances you want to compare into the 20_newsgroups folder

code structure:
Bayes classifier class->
for training, testing and category tester, and two other functions for creating an
instance and for Classifying function to calculate the Naive_bayes_probability for classifying
Then performs classification for all the classes that are present in the 20_newsgroups. The classification 
is also based on three different cases, we have defined some breakwords in respective breakwords$.txt files. 
These are the words that are common in most of the articles and the code computes accuracy of classification by removing these breakwords. 
At first we perform classification without any breakwords then with 25 breakwords and then with 175 breakwords. 


For these different breakwords classification we defined different classes as basyesian_classification_0, 
basyesian_classification_25, basyesian_classification_175 and trained them. 
Using these trained models of classes we check for the accuracy by testing them on the Testing_Data_Set.

The algorithm uses Naive-Bayes classifier to classify in all of the above approaches.
 
 