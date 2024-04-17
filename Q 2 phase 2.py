def get_name():
    name = input("enter your name: ")
    return name

def get_tshirt(n):
    name = get_name()
    a = input("which brand do you want: ")
    b = input("in which size do you want: ")
    brand = ['peter england', 'puma', 'nike', 'arrow', 'raymond']
    size = ['m', 'l', 'xl', 'xxl']
    brand_found = False
    
    if a in brand and b in size:
        brand_found = True
    
    if brand_found:
        print("Hi", name , ", the brand and size you are looking for is available in our store")
    else:
        print("Hi", name , ", the brand or size or both you are looking for is not available in our store")

get_tshirt('nike')
