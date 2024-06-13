def has_valid_price(dics):
    try:
        prc = dics["price"]
        if(type(prc) == float):
            return True
        if(type(prc) == int):
            if(prc >= 0):
                return True
            else:
                return False
        else:
            return False
        # if type(prc) == "float" or type(prc) == "int":
        #     return True
        # else:
        #     return False
    except:
        return False

print(has_valid_price({"product":"Milk", "price":1.50}))
print(has_valid_price({"product":"Cheese", "price":-1}))
print(has_valid_price({"product":"Eggs", "price":0}))
print(has_valid_price({"product":"Cereals"}))
print(has_valid_price(None))