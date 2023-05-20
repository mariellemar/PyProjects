print("Try to survive the first day in a zombie apocalipse!")

colour = input("colour: ")
adj1 = input("adjective: ")
name = input("name: ")
city = input("city: ")
adj2 = input("adjective 2: ")
location = input ("location: ")
number = input("number: ")
bodyPart = input("body part: ")
obj1 = input("object: ")
animal = input ("animal: ")
     
decision = input("run, hide or fight? ")
if (decision == "hide"):
    fate = f"found cover, but it wasn't long untill the zombies found {name}.\n You DIED!"
elif (decision =="run"):
    fate = f"sadly, what {name} didn't see coming was the overflowing pack of zombies behind them. \nYou DIED!"
elif (decision == "fight"):
    obj2 = input("object 2: ")

    fate = f"bravely, took the {obj1} in hand advanced towards the unware zombies. What {name} didn't expect was \
to be cut short by a rain of fiery... {obj2}? Oh well, that barbecued the zombies so who cares? You SURVIVED!"

madLib = f"It was a {adj1} day and the sky was a dark shade of {colour}. {name} woke up to the {city} News alerting \
of a {adj2} spreading virus that made people want to eat whatever {bodyPart} was near. Even {animal}'s {bodyPart}. \
{name} took a {obj1} and went for the {location}. In there, more than {number} zombies layed, almost like awating \
for {name}. Seeing them, {name} decided to {decision} and {fate}"

print(madLib)