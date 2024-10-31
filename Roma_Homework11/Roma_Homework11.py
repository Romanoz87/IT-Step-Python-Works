import requests
def get_products():
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)
    response_data = response.json()
 

    if response.status_code == 200:
        return response.json()
    else:
        return "page not found"

def store_data():
    products = get_products()
    prices = []
    product_category = []
    product_name = []
    product_rate = []
    product_id = []
    id_title = []
    for product in products:
        prices.append({'price': product['price']})
        product_category.append(product['category'])
        product_name.append(product['title'])
        product_rate.append({'Title': product['title'], 'product': product['rating']['rate']})
        product_id.append(product['id'])
        id_title.append({'id': product['id'], 'Title': product['title']})
    
    

# დავალება "ა"-ს ბლოკი ფასების გამოტანა მაქსიმალური და მინ მნიშვნელობებით

    price = [ x['price'] for x in prices  ]
    print("\nExercise A", '='*100)
    print("list of prices: ",price)
    print("Maximum price is: ", max(price))
    print("Minimum price is: ", min(price))
    print("="*100,"\n")

# დავალება "ბ"-ს ბლოკი. კატეგორიების გაფილტვრა და დასორტირება

    categories = sorted(set(product_category))
    print("\nExercise B", '='*100)
    print("sorted categories list: ",categories)
    print("="*100,"\n")

# დავალება "გ"-ს ბლოკი. პროდუქტის აღწერა (title) და id. დაასორტირებულიtitle-ის მიხედვით

    sorted_data = sorted(id_title, key=lambda x: x['Title'])
    print("\nExercise C", '='*100)
    print(f"{'ID':<15}{'Product name'}")
    print("-"*100)
        
    for i in sorted_data:
        print(f"{i['id']:<15}{i['Title']}")

# დავალება "დ"-ს ბლოკი. რეიტინგის მიხედვით დასორტირებული სია
    
    sorted_rating = sorted(product_rate, key=lambda x: x['product'])
    print("\nExercise D", '='*100)
    print(f"{'Rating':<15}{'Name'}")
    print("-"*100)
    for i in sorted_rating:
        print(f"{i['product']:<15}{i['Title']}")

 #=================================================================================   
    
store_data()



