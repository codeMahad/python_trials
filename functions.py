def my_details(name,country,city):
    print(name+" " "from"+"  "+country+"  "+city)
my_details("mahad","Uganda","Kampala")
my_details("hakim","Sudan","Khartum")
my_details("Hajarah","Ghana","Accra")
#Am trying out the FOR loop
my_players=["Kobe","Giannis","Damian"]
for x in my_players:
    print (my_players[1]+" "+"Bucks")
    my_players.append("Curry")
    print (my_players)
    break
#Inter-play of the "For loop" with IF, elif and else 
fruits = ["apple", "banana", "cherry"]
others=["mango","berries","guava"]
#The continue statement
for x in fruits:
  if x == "banana":
    continue
  print(x)
  #Nesting the loop
  for x in fruits:
     for y in others:
        print (x, y)
        if y == "guava":
           x.append("pawpaw")
           y.append("grape")
        else:
           print (x, y)
           break