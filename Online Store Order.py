#customer information
def process_customer_info(name,email,**kwargs):
    print(f"Processing customer info for {name}")
    print(f"Email : {email}")
    print("additional information:")

    for k,v in kwargs.items():
        print(f"{k}:{v}")

#item purchage
def process_order_item(*args):
    print("Processing order items:")

    for item in args:
        print(f'{item}')

#calculate item amount
def calculate_total_item(*args):
    total = 0

    for arg in args:
        if isinstance(arg, (int, float)):
            total = total + arg
        else:
            print(f"Invalid item price: {arg}")

    return total 

#process complete order and given receipt
def process_order(customer_info, *items, **kwargs):
    print("Order processing initiated")
    process_customer_info(**customer_info)
    process_order_item(*items)

    item_price = kwargs.get("item_price",())
    total_amount = calculate_total_item(*item_price)
    
    print(f"Total_amount : ${total_amount}")
    print("Order processing complete")


    print("--Receipt---")
    print(f"Customer :{customer_info}")

#input data
customer_info = {
    'name':'arjun',
    'email':'arjun@gmail.com',
    'phone':8005792198
}
items = ('pen','book','bag')

order_details = {
    'address':'uday nagar',
    'item_price':(12.43,654,766)
}

process_order(customer_info,*items, **order_details)