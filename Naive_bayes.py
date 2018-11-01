"""
the naive bayes classifier is tarined with 80 percent of the dataset provided along with the project
and the testing phase of the classifier is carried out using the remaining 20 perecent of the dataset
so The division is 80 is to 20


before processing the given dataset for classification we can actually use the pre processing step in which
we can remove the commonly used words like an, the, but. By getting the common words out of the scene the
learning rate and accuracy of the classifier can be boosted. so this preprocessing step is included in the program
"""

import os     
import codecs     
import math

class Bayes_Classifier:

    def TRAIN_Bayes_classifier(node, Train_80, category):
        #initialising
        counts = {}
        total = 0
        dir_cur = Train_80 + category
        files = os.listdir(dir_cur)
        
        #reading each file from the list of files
        for i in files:
            f = codecs.open(dir_cur + '/' + i, 'r', 'iso8859-1')
            #iterating over the file and going through each line
            for line in f:
                words = line.split()
                #reading each token and checking if it is space or
                # if the token or the word is in the breakwords
                for word in words:
                    word = word.strip('\'".,?:-')
                    word = word.lower()
                    if word != '' and not word in node.breakwords:
                        node.words.setdefault(word, 0)
                        node.words[word] += 1
                        counts.setdefault(word, 0)
                        counts[word] += 1
                        total += 1
            f.close()
        return(counts, total)     
    #the testing phase of the trained classifier
    def TEST_Bayes_classifier(node, testing):

        correct = 0
        total = 0
        cat = os.listdir(testing)
        cat = [filename for filename in cat if
                      os.path.isdir(testing + filename)]
        
        for i in cat:
            print(".", end="")
            (catCorrect, catTotal) = node.CATEGORY_TESTER(
                testing + i + '/', i)
            correct += catCorrect
            total += catTotal
        print("\n\nAccuracy is  %f%%  (%i number of test instances)\n\n" %
              ((float(correct) / total) * 100, total))               

    #the Classifier       
    def CLASSIFIER(node, filename):
        results = {}
        for i in node.categories:
            results[i] = 0
        f = codecs.open(filename, 'r', 'iso8859-1')
        for line in f:
            tokens = line.split()
            for token in tokens:
                #print(token)
                token = token.strip('\'".,?:-').lower()
                if token in node.words:
                    for category in node.categories:
                        if node.prob[category][token] == 0:
                            print("%s %s" % (category, token))
                        results[category] += math.log(node.prob[category][token])
        f.close()
        results = list(results.items())
        results.sort(key=lambda tuple: tuple[1], reverse = True)
        return results[0][0]

    def CATEGORY_TESTER(node, directory, category):
        files = os.listdir(directory)
        total = 0
        correct = 0
        for file in files:
            total += 1
            result = node.CLASSIFIER(directory + file)
            if result == category:
                correct += 1
        return (correct, total)

    def __init__(node, Train_80, breakwordlist):
               
        node.words = {}
        node.prob = {}
        node.guesses = {}
        node.breakwords = {}
        
        f = open(breakwordlist)
        for line in f:
            node.breakwords[line.strip()] = 1
        f.close()
        categories = os.listdir(Train_80)
        node.categories = [filename for filename in categories
                           if os.path.isdir(Train_80 + filename)]
        for category in node.categories:
            print('    ' + category)
            (node.prob[category],
             node.guesses[category]) = node.TRAIN_Bayes_classifier(Train_80, category)

        toDelete = []
        for word in node.words:
            if node.words[word] < 3:

                toDelete.append(word)
        for word in toDelete:
            del node.words[word]
        vocabLength = len(node.words)
        print("Calculating the probability using the naive bayes approach:")
        for category in node.categories:
            print('    ' + category)
            denominator = node.guesses[category] + vocabLength
            for word in node.words:
                if word in node.prob[category]:
                    count = node.prob[category][word]
                else:
                    count = 1
                node.prob[category][word] = (float(count + 1)
                                             / denominator)
        print ("Completed the Training \n\n")
                    
#Main directory is the place wgere the code is 
Main=os.getcwd()+"/20_newsgroups"

#the training directory 
Train_80 = Main + "/20_newsgroups_train/"
#the testing directory
Test_20 = Main + "/20_newsgroups_test/"


#          training
print(" with breaklist 0 ")
bayesian_classification_0 = Bayes_Classifier(Train_80,  "breakwords0.txt")
print("\n\n with breaklist 25 ")
bayesian_classification_25 = Bayes_Classifier(Train_80,  "breakwords25.txt")





#           testing         
print("with 0 breakwords classification...")
bayesian_classification_0.TEST_Bayes_classifier(Test_20)
print("with 25 breakwords classification...")
bayesian_classification_25.TEST_Bayes_classifier(Test_20)

