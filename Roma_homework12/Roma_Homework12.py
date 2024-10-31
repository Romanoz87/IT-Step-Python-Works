import os
import json
from pprint import pp


chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

dict = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]


def create_file(path, file):                                     # ფაილის შექმნა თუ ის არ არსებობს
  path += '.json' 

  try:
    with open(path, mode='x', encoding='utf-8'):
      ...
  except FileExistsError:
    print(f"File alredy exists...")
    print("Continue...\n")

  return path
#================================================

def read_file(path):                                            # ფაილის წაკითხვა
  with open(path, mode='r', encoding='utf-8') as file:
    pp(json.loads(file.read()))
#=============================================

def write_data(path, chess_players):                            # მონაცემების ჩაწერა ფაილში chess_players სიიდან
  with open(path, mode='w', encoding='utf-8') as file:
    file.write(json.dumps(chess_players, indent = 2))
    
#=====================================================
    

def update_content(path, dict):                                     # სიისთვის ახალი ლექსიკონების დამატება dict ლისტიდან
    for str in dict:
        chess_players.append(str)
   
    with open(path, mode= 'w', encoding = 'utf-8') as file:
        file.write(json.dumps(chess_players, indent = 2))
        pp(chess_players)

#=============================================================

path = create_file("jsons", "data")

write_data(path, chess_players)

read_file(path)
print("\n", "#"*100, "\n")
update_content(path, dict)
