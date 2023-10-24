products_input = input().split(" ")
searched_products = input().split(" ")

stock_dict = {}

for product in range(0, len(products_input),2):
    key = products_input[product]
    value = int(products_input[product + 1])

    stock_dict[key] = value

for s in searched_products:
    if s in stock_dict.keys():
        print(f"We have {stock_dict[s]} of {s} left")
    else:
        print(f"Sorry, we don't have {s}")
