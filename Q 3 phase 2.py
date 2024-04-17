def get_order():
    print("Enter the dishes you want (Press Enter 2 times if u dont want more dishes):")
    orders = []
    while True:
        order = input("  ")
        if order: 
            orders.append(order)
        else:
            break

    if orders:
        print("Preparing your order:")
        for item in orders:
            print("Preparing your order:", item)
        print("The following orders have been dispatched:")
        for item in orders:
            print(item)
    else:
        print("Sorry, no orders found.")

get_order()
