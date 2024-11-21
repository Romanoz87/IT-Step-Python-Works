# დავალება 2 და 3 გაერთიანებული. თავდაპირველად გაუშვით პირველი კოდი, რათა შეიქმნას ფაილები ამ კოდში გასახსნელად



import json, pickle, dill

def open_file(filename):

# open file with Json
    try:
        with open(filename, mode='r', encoding='utf8') as file:
            data = json.load(file)
            print("\nJson format is successful..\n")
            print(data)
    except Exception as error:
        print("File canot pened by json")

# open file with pickle
    try:
        with open(filename, mode='rb') as file:
            data = pickle.load(file)
            print("\nPickle format is successful..\n")
            print(data)
    except Exception as err:
        print('File cannot opened with pickle')

# open file with dill
    try:
        with open(filename, mode='rb') as file:
            data = dill.load(file)
            print("\nDill format is successful..\n")
            print(data)
    except Exception as err:
        print('File cannot opened with dill')



# open_file('new_json.json')

open_file('new_pickle_file.pkl')
# open_file('new_dill_file.dill')