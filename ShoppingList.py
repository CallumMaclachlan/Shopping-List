import random

#Meal List
meal = [
['2', 'Bolognese', 'Shepards Pie', 'Alfredo'],
['1', 'Prawn Spaghetti', 'Burgers']
]

#Prices for Ingredients
meat_free_mince = 4.00
dolmio = 2.00
spaghetti = 1.00
cheese = 1.00
mince_meat = 5.00
carrots = 1.00
onions = 1.00
potatoes = 1.00
stock = 1.00
chicken = 5.00
cream = 2.00
garlic = 0.5
broccoli = 1.5
pasta = 1.00
burgers = 4.00
buns = 2.00
prawns = 4.00
soft_cheese = 2.00
parsley = 0.5

#Ingredients for Recipes
bolognese_price = meat_free_mince + spaghetti + dolmio + cheese
bolognese = (f"""Meat Free Mince £{meat_free_mince}
Spaghetti £{spaghetti}
Dolmio Sauce £{dolmio}
Cheese £{cheese}
""")

shepards_pie_price = mince_meat + carrots + onions + potatoes + stock
shepards_pie = (f"""Mince Meat £{mince_meat}
Carrots £{carrots}
Onions £{onions}
Potatoes £{potatoes}
Beef Stock £{stock}
""")

alfredo_price = chicken + cream + garlic + broccoli + pasta + stock + cheese
alfredo = (f"""Chicken £{chicken}
Cream £{cream}
Garlic £{garlic}
Broccoli £{broccoli}
Pasta £{pasta}
Chicken Stock £{stock}
Cheese £{cheese}
""")

burgers_price = burgers + buns + potatoes + cheese
burgers=(f"""Beef Burgers £{burgers}
Burger Buns £{buns}
Potatoes £{potatoes}
Cheese £{cheese}
""")

prawn_price = prawns + spaghetti + soft_cheese + garlic + parsley
prawn=(f"""Prawns £{prawns}
Spaghetti £{spaghetti}
Soft Cheese £{soft_cheese}
Garlic £{garlic}
Parsley £{parsley}
""")

def formula():
  d=7
  list=("Shopping List:\n")
  list_price = (0.00)
  while d != 0 and d >= 0:
    print(f"You have {d} day(s) left to fill.")
    print('How many days do we want to fill?')
    days = input('Days: ')
    print("")
    for time in meal:
      if time[0] == days:
        n=random.choice(time[1:])
        print(n)
        
        if n=='Bolognese':
          d=d-2
          list += bolognese
          list_price = list_price + bolognese_price
          meal[0].remove("Bolognese")
        if n=='Shepards Pie':
          d=d-2
          list += shepards_pie
          list_price = list_price + shepards_pie_price
          meal[0].remove("Shepards Pie")
        if n=='Alfredo':
          d=d-2
          list += alfredo
          list_price = list_price + alfredo_price
          meal[0].remove("Alfredo")
        if n=='Burgers':
          d=d-1
          list += burgers
          list_price = list_price + burgers_price
          meal[1].remove("Burgers")
        if n=='Prawn Spaghetti':
          d=d-1
          list += prawn
          list_price = list_price + prawn_price
          meal[1].remove("Prawn Spaghetti")
  print(list)
  print("Total Price: £" + str(list_price))
formula()

