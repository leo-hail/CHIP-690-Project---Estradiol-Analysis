import pandas as pd 

es1 = pd.read_csv("estradiol 2004_2014.csv")

# encoding for utf 8 csv file before merging
encodings = ['utf-8']

for encoding in encodings:
    try:
        es1 = pd.read_csv("estradiol 2004_2014.csv", encoding = encoding)
        break # Stop if successful
    except Exception as e:
        error_message = str(e)

es2 = pd.read_csv("estradiol 2015_2025.csv")

encodings = ['uft-8']

for encoding in encodings:
    try:
        es1 = pd.read_csv("estradiol 2015_2025.csv", encoding = encoding)
        break # Stop if successful
    except Exception as e:
        error_message = str(e)

project = pd.concat([es1, es2], ignore_index = True)
columns_to_drop = ['Literature Reference', 'Compounded Flag',
                   'Report Source', 'Manufacturer Control Number',
                   'Reported to Manufacturer?', 'Concomitant Product Names',
                   'Reporter Type', "Sender"]

project = project.drop(columns = columns_to_drop)

project = project[~project['Suspect Product Active Ingredients'].str.contains('-', na = False)]
print(len(project))

project.to_csv("estradiol_database.csv", index = False)
