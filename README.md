# Spell-Correction

The project is for the submission of Homework Assignment 1 of COMP 8730 - Natural Language Processing and Understanding of University of Windsor. 

The aim of the project was to implement a system of spell correction and calculating its success_at_k. 
For that purpose, Wordnet is used as a dictionary which is invoked by NLTK library and Birkbeck was used as a corpus which has the list of 809 misspelt words along with the correct words. 

The project is implemented in Python language using Google Colab. The best and recommeded way to run it is also using Google Colab. 
The required modules/libraries are 
- Multiprocessing
- Numpy
- OS
- NLTK
- RE
- PyTrec_Eval
- JSON

Out of these, only PyTrec_eval needs to be installed using pip, rest of the libraries are included by default in Google Colab.

The easiest way to run this code is to open the "main.ipynb" in Google Colab and upload the rest of the files in the session. 
There is different function for each of the files.
- main.ipynb - main code of the project
- dictionary.py - Utilizes the NLTK library to list out required words of English language
- birkbeck.py - Takes birkbeck.txt as an input and creates a python dictionary of misspelt and correct words
- mindist.py - Calculates the Edit distance of given word with all the words of provided dictionary using multiprocessing
- successatk.py - Returns the value of success at k

The file "birkbeck.txt" was copied from the https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/0643 which has the orignial filename as FAWTHROP1DAT.643

The success_at_k is evaluated for different subsets of dictionary that includes
- Words with the same initials
- Words with the same length as the correct words
- Words with the same initials and the same lenght as the correct words
