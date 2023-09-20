
'''
    Below is a dictionary consisting of details of 1 restaurant fetched from Yelp.
'''

restaurant_1 = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "state": "CA",
    "address": "375 Valencia St",
    "zip_code": "94113",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}


def explore_data():
    # 1.1 TODO: Print the URL of the website of Four Barrel Coffee.
    print(restaurant_1['url'])
    # 1.2 TODO: Print the latitude and longitude of Four Barrel Coffee, using one print statement.
    print(restaurant_1['latitude'], restaurant_1['longitude'])
    # 1.3 TODO: Print the complete address of the Four Barrel Coffee, formatted as a string - 
    # it should include the address, city, state and the zip code, with commas between them e.g.:
    # "375 Valencia St, San Francisco, CA, 94113"
    print(f'{restaurant_1["address"]}, {restaurant_1["city"]}, {restaurant_1["state"]}, {restaurant_1["zip_code"]}')


def favorite_restaurant():
    # Let's ask the user for some information about their favorite restaurant

    # 2.1 TODO: Create an empty dictionary in a variable called `favorite_restaurant`
    favorite_restaurant = {}
    # 2.2 TODO: Ask the user for the restaurant `name`, `address`, and their `favorite_dish`
    # Add all three of these as key value pairs in your new dictionary, ala:
    #    favorite_restaurant  = {
    #        "name": "Subway",
    #        "address" : "116th & Broadway, NY 10016",
    #        "favorite_dish" : "Chicken BLT Sandwich"
    #    }
    favorite_restaurant['name'] = input('What is the name of the resturant? ')
    favorite_restaurant['address'] = input('What is the address of the resturant? ')
    favorite_restaurant['favorite_dish'] = input('What is your favorite dish? ')

    # 2.3 TODO: Print out your dictionary to make sure it populated correctly
    print(favorite_restaurant)

    # Oh no, the restaurant stopped serving the user's favorite dish!
    # 2.4 TODO: Remove the `favorite_dish` key/value pair from the dictionary
    favorite_restaurant.pop('favorite_dish')

    # 2.5 TODO: Print out the dictionary again. This time, the dictionary 
    # should only contain a 'name' and 'address' for that restaurant
    print(favorite_restaurant)

    # Looks like the restaurant is going through a lot of changes-- they moved!
    # 2.6 TODO: Update the address of the user's favorite restaurant to "116th & Broadway, NY 10016"
    favorite_restaurant['address'] = "116th & Broadway, NY 10016"

    # 2.7 TODO: Print out the restaurant's new address by printing the dictionary's value 
    # for the key `address`
    restaurant_address = favorite_restaurant['address']
    print(restaurant_address)


def clean_print():
    # It's hard to read the contents of a dictionary when we print the whole thing out.

    # 3.1 TODO: Instead, loop through each item-pair in the `restaurant_1` dictionary
    # and print out each key and value on their own line, ala:
    #      `name: Four Barrel Coffee
    #       url: https://www.yelp.com/biz/four-barrel-coffee-san-francisco`
    # etc etc
    for key, value in restaurant_1.items():
        print(f'{key}: {value}')
