#დავალება 1 და 3 გაერთიანებული ამ პროგრამის გაშვების შემდეგ შეიქმნება ფაილები მეორე პროგრამაში გასახსნელად.

import json
import pickle
import dill

def save_data(data):

# save data with json
    try:     
        with open('new_json.json', mode='w') as file:
            json.dump(data, file)
        print(f"Data successfully saved in json format")
        
    except (TypeError, OverflowError) as err:
        print("JSON failed")

# save data with pickle        
        try:       
            with open('new_pickle_file.pkl', mode='wb') as file:
                pickle.dump(data, file)
            print(f"Data successfully saved in pickle format")
            
        except (pickle.PicklingError, AttributeError) as err:
            print(f"Pickle failed")

# save data with Dill         
            try:
                with open('new_dill_file.dill', mode='wb') as file:
                    dill.dump(data, file)
                print(f"Data successfully saved as dill")
                
            except Exception as err:
                print(f"Dill failed")


num_in_power = lambda x: x ** 2

list1 = ({'name':'Roma', 'Last_name': 'Berdzenishvili', 'age': 36},
         {'name':'Giorgi', 'Last_name': 'Davitashvili', 'age': 30},
         {'name':'Davit', 'Last_name': 'Akhobadze', 'age': 26},
         {'name':'Eka', 'Last_name': 'Dvali', 'age': 22},
         {'name':'Lasha', 'Last_name': 'Beraia', 'age': 50})

data = { 'a', True, 33, (12, 45, False) }

# save_data(num_in_power)

# save_data(data)
save_data(list1)