'''1. დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. შედეგი დაბეჭდეთ ეკრანზე.

2. დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.

'''
import concurrent.futures

def find_odd_numbers(start, end):
    
    return [num for num in range(start, end + 1) if num % 2 != 0]

    
    

def find_even_numbers(start, end):
    
    return [num for num in range(start, end + 1) if num % 2 != 1]

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(find_odd_numbers, 30, 50)
    print(f1.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(find_even_numbers, 30, 50)
    print(f1.result())


    
