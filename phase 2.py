def get_name():
    name = input("enter your name:")
    return name

def get_tshirt(n):
    name = get_name()
    a = input("which brand do you want:")
    brand = ['peter england', 'puma', 'nike', 'raymond','arrow']
    brand_found = False
    for i in brand:
        if i == a:
            brand_found = True
            break
    
    if brand_found:
        print("Hi", name , ",the brand you are looking for is available in our store")
    else:
        print("Hi", name , ",the brand you are looking for is not available in our store")

get_tshirt('nike')
