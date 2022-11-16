from os.path import exists
from create_csv import create_scv 
from data_writter import data_writing_scv 
from data_writter import data_writing_txt 


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    create_scv()


data_writing_scv()
data_writing_txt()

