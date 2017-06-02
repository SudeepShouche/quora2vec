#quora2vec
#code using machine learning to identify if two questions are similar

#import dependencies
import spacy
import requests
import json
from scipy import spatial
import random
from sklearn.metrics import roc_curve, auc, log_loss
from unidecode import unidecode
from sklearn.linear_model import LogisticRegression
import numpy as np
import csv
import re


#Input file
input_csv_file_path="input.csv"
json_file_path="input_json.json"
output_csv_file_path="output.csv"


#Read CSV File
def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)

#Convert csv data into json and write it
def write_json(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(data))

            
class readData(object):
    def __init__(self):
        pass
    def getJSON(self,is_first_pass=False):
        if is_first_pass:
            print "Creating json data"
            read_csv(input_csv_file_path, json_file_path, "pretty")
        data = open(json_file_path,"rb").read()
        dicta = json.loads(data)
        questions_row = []
        print "Reading json data"
        for doc in dicta:
            questions_text = doc.get("questions_text","")
            questions_row.append(questions_text)
        print "Finished reading json data"
        return questions_row
