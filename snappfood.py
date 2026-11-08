#pizzasize
pizza_size=input("choose your size pizza(small,medium,large):") 
if pizza_size=="small":
        price=200
elif pizza_size=="medium":
      price=300
elif pizza_size=="large":
        price=400
else:
        print("we dont have this size")
#pepperoni
pepperoni=input("do you want pepperoni?(yes,no):")    
if pepperoni=="yes":
 if pizza_size=="small":
        price=price+500
 elif pizza_size=="medium":
      price=price+700
 elif pizza_size=="large":
        price=price+1000