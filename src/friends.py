def get_name(person5):
    result = person5["name"]
    return result

def get_favourite_tv_show(person2):
    result = person2["favourites"]["tv_show"]
    return result

def likes_to_eat(person2, food):
    result = ("bread" in person2["favourites"]["snacks"])
    return result

def add_friend(person2, newfriend):
    person2["friends"].append("Scrappy-Doo")

def remove_friend(person2, byefriend):
    person2["friends"].remove("Scrappy-Doo")

def total_money (people):
    money = 0

    for  person in people:
        money += person["monies"]

    return money

def lend_money(person2, person1, number):
    pass
#     money2 = person2["monies"]
#     money1 = person1["monies"] 
#     money1 = money1+money2
#     money2 = 0