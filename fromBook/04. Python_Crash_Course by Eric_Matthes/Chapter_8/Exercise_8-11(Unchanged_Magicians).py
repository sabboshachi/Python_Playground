

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
def show_magician(list_1,list_2):
    print("Original list")
    print(list_1)
    #for name in list_1:
        #print(name.title())
    print("Copied List: ")
    print(list_2)
    #for name in list_2:
        #print(name.title())

the_great_magicians = []
magicians_name(magician)
make_great(magician)
#print(the_great_magicians)

new_the_great_magicians = the_great_magicians.copy()
show_magician(magician,new_the_great_magicians)