Message = ("Welcome to JB's Trip Generator. Let me help you find your trip.")
print(Message)

import random

destionations_options = ["Las vegas", "New York", "Washington DC"]
transportation_options= ["Rental car","uber","bus"]
entertainment_options = ["Night Club","Live show", "museum"]
restaurant_options = ["Tao","outback", "STK"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def destination_picker():
    random_dest = random_item_picker(destionations_options)
    user_choice = input(f'We have randomly selected {random_dest} for your trip, enter "yes" to keep it or "no" to see another:')
    user_decision = True
    while user_decision == True:
        if user_choice == "yes":
            print(f'enjoy your trip to {random_dest}')
            return random_dest
        elif user_choice == "no":
            random_dest = random_item_picker(destionations_options)
            user_choice = input(f'We have randomly selected another option, how does {random_dest} sound for your trip, enter "yes" to keep it or "no" to see another:')
confirmed_destination = destination_picker()


def transportation_picker():
    random_trans = random_item_picker(transportation_options)
    user_choice = input(f'For your transportation, we have selected {random_trans} for you to get around. Please enter yes or no to keep:')
    user_decision = True
    while user_decision == True:
        if user_choice =="yes":
            print(f'Great Choice picking the {random_trans}')
            return random_trans
        elif user_choice == "no":
            random_trans = random_item_picker(transportation_options)
            user_choice = input(f'how about {random_trans}? "yes" or "no:"')
confirmed_transportation = transportation_picker()


def entertainment_picker():
    random_enter = random_item_picker(entertainment_options)
    user_choice = input(f'For entertainment, we have selected {random_enter}. Does that sound fun? please enter "yes" or "no:"')
    user_decision = True
    while user_decision == True:
        if user_choice == "yes":
            print(f'Awesome, you are gonna have a great time at the {random_enter}.')
            return random_enter
        elif user_choice == "no":
            random_enter = random_item_picker(entertainment_options)
            user_choice = input(f'what about {random_enter}? "yes" or "no:"')
confirmed_entertainment = entertainment_picker()

def restaurant_picker():
    random_rest = random_item_picker(restaurant_options)
    user_choice = input(f'We have selected {random_rest} for you to eat at. Does that sound good? "yes" or "no:"')
    user_decision = True
    while user_decision == True: 
        if user_choice =="yes":
            print(f'Good Choice, you will love it at {random_rest}.')
            return random_rest
        elif user_choice == "no":
            random_enter = random_item_picker(restaurant_options)
            user_choice = input(f'ok, how about {random_enter}? "yes" or "no:"')
confirmed_resturaunt = restaurant_picker()

print(f'Thank you for confirming your trip, you will go to {confirmed_destination} by {confirmed_transportation}. While there you will have a great time at the {confirmed_entertainment} and finish your night eating out at {confirmed_resturaunt}.')