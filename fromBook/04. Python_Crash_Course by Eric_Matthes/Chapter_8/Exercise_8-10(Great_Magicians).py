

def magicians_name(magicians):
    print("The name of the magicians are: ")
    for name in magicians:
        print(name.title())

def make_great(great_magicians):
   for name in great_magicians:
       great_name = "The Great " + name.title() + "!"
       the_great_magicians.append(great_name)

   print("The Great Names are: ")
   for final_name in the_great_magicians:
       print(final_name)


magician = ["sandy", "rudra", "gulum"]
the_great_magicians = []
magicians_name(magician)
make_great(magician)

