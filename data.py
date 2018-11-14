name_key = "name"
address_key = "address"

# Coordinates in int
x_coordinate_key = "x_coordinate"
y_coordinate_key = "y_coordinate"

# Telephone number in string
tel_key = "tel"

# Time written in 24hr format, in string
opening_time_key = "opening_time"
closing_time_key = "closing_time"

# In int
no_of_stores_key = "no_of_stores"
seating_capacity_key = "seating_capacity"
# In float
average_price_key = "average_price"

# In float, out of 5
rating_key = "rating"

# List of popular food in the canteen
popular_food_key = "popular_food"


#Vegetarian food stall list key
vegetarian_foodstall_key = "vegetarian_foodstall"

# List of stores that have halal food
halal_foodstall_key = "halal_foodstall"

# A list of the keys in the each canteen's dictionary
keys = [name_key,address_key,x_coordinate_key,y_coordinate_key,tel_key,opening_time_key,closing_time_key,
        no_of_stores_key,seating_capacity_key,average_price_key,rating_key,popular_food_key,halal_foodstall_key,
        vegetarian_foodstall_key]

# Creates an empty dictionary with key-value pairs with each Value a None object
# Using dict.fromkeys() function. Takes in a list of keys
def createEmptyCanteen(list_of_keys):

    # Console debugging
    print("createEmptyCanteen() function called")

    # Creates an empty dictionary with key-value pairs
    # Each Value is None object type
    empty_dictionary = dict.fromkeys(list_of_keys)

    return empty_dictionary


# A nested dictionary of canteens
canteen_dictionary = {1:{name_key:"canteen 1", address_key:"21 NANYANG CIRCLE, SINGAPORE 639778, HALL 1",
                         x_coordinate_key:448.0,y_coordinate_key:240.0,
                         tel_key:"6334 3033", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:9,
                         seating_capacity_key:310,average_price_key:5.50,rating_key:4.9,
                         popular_food_key:["Chicken Rice", "Mee Rebus"],
                         halal_foodstall_key:["halal 1 of can 1", "halal 2 of can 1"],
                         vegetarian_foodstall_key:["veg 1 of can 1","veg 2 of can 1"]
                         },
                      2:{name_key:"canteen 2", address_key:"35 Students Walk Singapore 639548",
                         x_coordinate_key:491.0,y_coordinate_key:325.0,
                         tel_key:"6334 3033", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:10,
                         seating_capacity_key:446,average_price_key:4.50,rating_key:4.3,
                         popular_food_key:["Ban Mian", "Japanese"],
                         halal_foodstall_key:["halal 1 of can 2", "halal 2 of can 2"],
                         vegetarian_foodstall_key:["veg 1 of can 2","veg 2 of can 2"]
                         },
                      3:{name_key:"canteen 9", address_key:"50 Nanyang Avenue Singapore 639798",
                         x_coordinate_key:634.0,y_coordinate_key:484.0,
                         tel_key:"9692 3456", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:9,
                         seating_capacity_key:293,average_price_key:4.20,rating_key:4.5,
                         popular_food_key:["Western", "Japanese"],
                         halal_foodstall_key:["halal 1 of can 9", "halal 2 of can 9"],
                         vegetarian_foodstall_key:["veg 1 of can 9","veg 2 of can 9"]
                         },
                      4:{name_key:"canteen 11", address_key:"20 Nanyang Avenue Singapore 639809",
                         x_coordinate_key:757.0,y_coordinate_key:545.00,
                         tel_key:"9786 6726", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:6,
                         seating_capacity_key:210,average_price_key:4.10,rating_key:4.1,
                         popular_food_key:["Korean", "Indian"],
                         halal_foodstall_key:["halal 1 of can 11", "halal 2 of can 11"],
                         vegetarian_foodstall_key:["veg 1 of can 11","veg 2 of can 11"]
                         },
                      5:{name_key:"canteen 13", address_key:"32 Nanyang Cresent Singapore 637658",
                         x_coordinate_key:450.0,y_coordinate_key:630.0,
                         tel_key:"9851 0908", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:8,
                         seating_capacity_key:210,average_price_key:4.30,rating_key:4.8,
                         popular_food_key:["Mixed Veg Rice", "Roasted Duck Rice"],
                         halal_foodstall_key:["halal 1 of can 13", "halal 2 of can 13"],
                         vegetarian_foodstall_key:["veg 1 of can 13","veg 2 of can 13"]
                         },
                      6:{name_key:"canteen 14", address_key:"34 Nanyang Crescent Singapore 637634",
                         x_coordinate_key:536.0,y_coordinate_key:623.0,
                         tel_key:"8112 7239", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:6,
                         seating_capacity_key:270,average_price_key:4.40,rating_key:4.2,
                         popular_food_key:["Korean", "Roasted Duck Rice"],
                         halal_foodstall_key:["halal 1 of can 14", "halal 2 of can 14"],
                         vegetarian_foodstall_key:["veg 1 of can 14","veg 2 of can 14"]
                         },
                      7:{name_key:"canteen 16", address_key:"50 Nanyang Walk Singapore 639929",
                         x_coordinate_key:401.0,y_coordinate_key:572.0,
                         tel_key:"9450 5893", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:5,
                         seating_capacity_key:340,average_price_key:4.60,rating_key:4.6,
                         popular_food_key:["Western", "Hotplate"],
                         halal_foodstall_key:["halal 1 of can 16", "halal 2 of can 16"],
                         vegetarian_foodstall_key:["veg 1 of can 16","veg 2 of can 16"]
                         },
                      8:{name_key:"ananda kitchen", address_key:"60 Nanyang Crescent Blk 19A #01-02 Singapore 636957",
                         x_coordinate_key:782.0,y_coordinate_key:439.0,
                         tel_key:"1234 5678", opening_time_key:"12 00",closing_time_key:"22 30",no_of_stores_key:1,
                         seating_capacity_key:90,average_price_key:6.60,rating_key:4.3,
                         popular_food_key:["Prata", "Milo Dinosaur"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["vegeterian soup","tomato salad"]
                         },
                      9:{name_key:"Foodgle Food Court", address_key:"38 Nanyang Crescent Blk 23, #051 - 058 Singapore 636866",
                         x_coordinate_key:657.0,y_coordinate_key:612.0,
                         tel_key:"8296 3633", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:9,
                         seating_capacity_key:440,average_price_key:5.10,rating_key:4.4,
                         popular_food_key:["Mala", "Western"],
                         halal_foodstall_key:["halal 1 of foodgle", "halal 2 of foodgle"],
                         vegetarian_foodstall_key:["veg 1 of foodgle","veg 2 of foodgle"]
                         },
                      10:{name_key:"North Hill Food Court", address_key:"60 Nanyang Crescent Blk 21A, 02-02 Singapore 636957",
                         x_coordinate_key:800.0,y_coordinate_key:455.0,
                         tel_key:"8508 0232", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:8,
                         seating_capacity_key:440,average_price_key:5.20,rating_key:4.7,
                         popular_food_key:["Mala", "Western"],
                         halal_foodstall_key:["halal 1 of NH", "halal 2 of NH"],
                         vegetarian_foodstall_key:["veg 1 of NH","veg 2 of NH"]
                         },
                      11:{name_key:"Pioneer Food Court", address_key:"162 Nanyang Cresent Singapore 637033",
                         x_coordinate_key:518.0,y_coordinate_key:123.0,
                         tel_key:"2345 6789", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:12,
                         seating_capacity_key:408,average_price_key:5.30,rating_key:3.9,
                         popular_food_key:["Bak Kuh Teh", "Nasi Lemak"],
                         halal_foodstall_key:["halal 1 of pioneer", "halal 2 of pioneer"],
                         vegetarian_foodstall_key:["veg 1 of pioneer","veg 2 of pioneer"]
                         },
                      12:{name_key:"Quad Cafe", address_key:"60 Nanyang Drive SBS-B1N-10 Singapore 637551",
                         x_coordinate_key:150.0,y_coordinate_key:417.0,
                         tel_key:"9876 5432", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:8,
                         seating_capacity_key:500,average_price_key:5.80,rating_key:3.8,
                         popular_food_key:["Western", "Economic Bee Hoon"],
                         halal_foodstall_key:["halal 1 of quad", "halal 2 of quad"],
                         vegetarian_foodstall_key:["veg 1 of quad","veg 2 of quad"]
                         },
                      13:{name_key:"Bakery Cuisine", address_key:"50 Nanyang Avenue NS3-01-20 Singapore 639798",
                         x_coordinate_key:288.0,y_coordinate_key:461.0,
                         tel_key:"8765 4321", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:1,
                         seating_capacity_key:0,average_price_key:3.60,rating_key:4.2,
                         popular_food_key:["Pancake", "Tiramisu"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["veg bun 1","veg bun 2"]
                         },
                      14:{name_key:"Each a Cup", address_key:"50 Nanyang Avenue NS3-01-21 Singapore 639798",
                         x_coordinate_key:290.0,y_coordinate_key:463.0,
                         tel_key:"9182 9307", opening_time_key:"09 00",closing_time_key:"21 00",no_of_stores_key:1,
                         seating_capacity_key:0,average_price_key:3.00,rating_key:4.1,
                         popular_food_key:["Green Milk Tea", "Tropical Fruit Tea"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Fruit tea","Oolong Tea"]
                         },
                      15:{name_key:"Grande Cibo", address_key:"North Spine Plaza 50 Nanyang Avenue NS3-01-23 Singapore 639798",
                         x_coordinate_key:260.0,y_coordinate_key:472.0,
                         tel_key:"4321 8765", opening_time_key:"11 00",closing_time_key:"20 00",no_of_stores_key:1,
                         seating_capacity_key:48,average_price_key:6.00,rating_key:4.0,
                         popular_food_key:["Cabonara Pasta", "Hawaiian Pizza"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Tomato Pizza","Veg Pasta"]
                         },
                      16:{name_key:"KFC", address_key:"North Spine Plaza 76 Nanyang Drive N2.1-01-04 Singapore 637331",
                         x_coordinate_key:257.0,y_coordinate_key:497.0,
                         tel_key:" 6762 6124", opening_time_key:"07 30",closing_time_key:"23 00",no_of_stores_key:1,
                         seating_capacity_key:999,average_price_key:5.00,rating_key:4.3,
                         popular_food_key:["Teriyaki chicken burger", "Zinger Burger"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Corn Cup","Veg Burger"]
                         },
                      17:{name_key:"Long John Silvers", address_key:"North Spine Plaza 76 Nanyang Drive N2.1-01-05 Singapore 637331",
                         x_coordinate_key:257.0,y_coordinate_key:480.0,
                         tel_key:"6314 0181", opening_time_key:"07 30",closing_time_key:"22 00",no_of_stores_key:1,
                         seating_capacity_key:999,average_price_key:4.00,rating_key:4.4,
                         popular_food_key:["Fish Burger", "Mud Cake Pie"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Veggie Cup","Veg Burger"]
                         },
                      18:{name_key:"MacDonalds'", address_key:"North Spine Plaza 76 Nanyang Drive N2.1-01-08 Singapore 637331",
                         x_coordinate_key:257.0,y_coordinate_key:469.0,
                         tel_key:"6792 9917", opening_time_key:"07 30",closing_time_key:"23 00",no_of_stores_key:1,
                         seating_capacity_key:999,average_price_key:6.00,rating_key:4.5,
                         popular_food_key:["Samurai Beef Burger", "Mac Wings"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Veg Crunch","Apple Pie"]
                         },
                      19:{name_key:"Mr. Bean", address_key:"North Spine Plaza 50 Nanyang Avenue NS3-01-16 Singapore 639798",
                         x_coordinate_key:273.0,y_coordinate_key:468.0,
                         tel_key:"2341 5623", opening_time_key:"07 30",closing_time_key:"22 30",no_of_stores_key:1,
                         seating_capacity_key:0,average_price_key:3.00,rating_key:4.1,
                         popular_food_key:["Soy Bean Milk", "Matcha Soy Bean Milk Tea"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Soy Bean pancake","Red Bean pancake"]
                         },
                      20:{name_key:"North Spine Food Court", address_key:"North Spine Plaza 76 Nanyang Drive NS2.1-02-03/01A Singapore 637331",
                         x_coordinate_key:253.0,y_coordinate_key:473.0,
                         tel_key:" 6465 8588", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:19,
                         seating_capacity_key:1838,average_price_key:4.00,rating_key:3.9,
                         popular_food_key:["Ban Mian", "Hot Plate"],
                         halal_foodstall_key:["halal 1 of NS", "halal 2 of NS"],
                         vegetarian_foodstall_key:["Veg 1 of NS","Veg 2 of NS"]
                         },
                      21:{name_key:"Paik's Bibim", address_key:"North Spine Plaza 50 Nanyang Avenue NS3-01-15 Singapore 639798",
                         x_coordinate_key:273.0,y_coordinate_key:462.0,
                         tel_key:"6262 0567", opening_time_key:"10 00",closing_time_key:"21 00",no_of_stores_key:1,
                         seating_capacity_key:40,average_price_key:7.00,rating_key:4.5,
                         popular_food_key:["Beek Bibim", "Chicken Bibim"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Veg Bibim 1","Veg Bibim 2"]
                         },
                      22:{name_key:"Peach Garden Chinese Restaurant", address_key:"North Spine Plaza 76 Nanyang Drive N2.1-02-01B Singapore 637331",
                         x_coordinate_key:255.0,y_coordinate_key:493.0,
                         tel_key:" 6219 9398", opening_time_key:"11 00",closing_time_key:"20 30",no_of_stores_key:1,
                         seating_capacity_key:180,average_price_key:15.00,rating_key:4.6,
                         popular_food_key:["Yang Zhou Fried Rice", "Xiao Long Bao"],
                         halal_foodstall_key:[],
                         vegetarian_foodstall_key:["Veg Tofu Pot","Stir Fried Baby Kailan"]
                         },
                      23:{name_key:"Pen & Inc", address_key:"North Spine Plaza 76 Nanyang Drive NS2.1-01-01 Singapore 637331",
                         x_coordinate_key:262.0,y_coordinate_key:483.0,
                         tel_key:"6314 0158", opening_time_key:"11 00",closing_time_key:"23 00",no_of_stores_key:1,
                         seating_capacity_key:144,average_price_key:9.00,rating_key:3.7,
                         popular_food_key:["Chicken Consomme", "Chuncky Salad"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Wild Mushroom Soup","Heirloom Soup"]
                         },
                      24:{name_key:"Pizza Hut Express", address_key:"North Spine Plaza 76 Nanyang Drive N2.1-01-04 Singapore 637331",
                         x_coordinate_key:258.0,y_coordinate_key:492.0,
                         tel_key:"6762 6124", opening_time_key:"11 00",closing_time_key:"22 00",no_of_stores_key:1,
                         seating_capacity_key:999,average_price_key:6.8,rating_key:4.5,
                         popular_food_key:["Hawaiian Ham Pizza", "Teriyaki Chicken Pizza"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Veggie Lover","The Four Cheese"]
                         },
                      25:{name_key:"Starbuck Coffee", address_key:"North Spine Plaza 76 Nanyang Drive N2.1-01-06 Singapore 637331",
                         x_coordinate_key:252.0 ,y_coordinate_key:477.0,
                         tel_key:"6910 1245", opening_time_key:"07 00",closing_time_key:"22 00",no_of_stores_key:1,
                         seating_capacity_key:999,average_price_key:5.3,rating_key:4.7,
                         popular_food_key:["Vanilla Latte", "Passion Fruit Tropica Tea"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Black Americano","Soy Latte"]
                         },
                      26:{name_key:"Subway", address_key:"North Spine Plaza 76 Nanyang Drive N2.1-01-07 Singapore 637331",
                         x_coordinate_key:252.0,y_coordinate_key:475.0,
                         tel_key:"6462 5238", opening_time_key:"08 00",closing_time_key:"21 00",no_of_stores_key:1,
                         seating_capacity_key:999,average_price_key:4.7,rating_key:4.8,
                         popular_food_key:["Chicken Bacon Ranch", "Egg Mayo"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Egg Mayo","Veggie Pattie"]
                         },
                      27:{name_key:"The House Steamboat Restaurant", address_key:"North Spine Plaza 50 Nanyang Avenue NS3-01-24 Singapore 639798",
                         x_coordinate_key:270.0,y_coordinate_key:439.0,
                         tel_key:"8821 3302", opening_time_key:"09 00",closing_time_key:"21 00",no_of_stores_key:1,
                         seating_capacity_key:34,average_price_key:6.2,rating_key:4.1,
                         popular_food_key:["Yellow Braised Chicken", "Sichuan hot pot"],
                         halal_foodstall_key:[],
                         vegetarian_foodstall_key:["Veg Hotpot 1","Veg Hotpot 2"]
                         },
                      28:{name_key:"The Sandwich Guys", address_key:"North Spine Plaza 50 Nanyang Avenue NS3-01-22 Singapore 639798",
                         x_coordinate_key:272.0,y_coordinate_key:442.0,
                         tel_key:"9099 1412", opening_time_key:"10 00",closing_time_key:"20 00",no_of_stores_key:1,
                         seating_capacity_key:0,average_price_key:5.4,rating_key:4.7,
                         popular_food_key:["Barbeque Pulled Pork", "Peri Peri Chicken"],
                         halal_foodstall_key:[],
                         vegetarian_foodstall_key:["Roasted Eggplant and Cheese","The MLT (Veg)"]
                         },
                      29:{name_key:"The Soup Spoon", address_key:"50 Nanyang Avenue NS3-01-14 Singapore 639798",
                         x_coordinate_key:283.0,y_coordinate_key:468.0,
                         tel_key:"6268 7566", opening_time_key:"10 00",closing_time_key:"20 00",no_of_stores_key:1,
                         seating_capacity_key:104,average_price_key:6.3,rating_key:4.9,
                         popular_food_key:["Velvety Mushroom Stroganoff", "Boston Clam Chowder"],
                         halal_foodstall_key:["halal certified"],
                         vegetarian_foodstall_key:["Roasted Pumpkin","Meatless Minestrone"]
                         },
                      30:{name_key:"Koufu", address_key:"50 Nanyang Avenue SS3-B4 Singapore 639798",
                         x_coordinate_key:170.0,y_coordinate_key:210.0,
                         tel_key:"6790 0355", opening_time_key:"07 00",closing_time_key:"21 00",no_of_stores_key:15,
                         seating_capacity_key:1050,average_price_key:4.2,rating_key:4.9,
                         popular_food_key:["Chicken Rice", "Japanese"],
                         halal_foodstall_key:["Yong Tau Foo", "Fish Soup & Ban Mian"],
                         vegetarian_foodstall_key:["Veg Mixed Rice","Veg 2 of Koufu"]
                         }}
