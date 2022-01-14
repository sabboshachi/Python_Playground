favourite_language = {
    "jen" : ["python", "ruby"],
    "sarah" : ["c"],
    "edward" : ["ruby", "go"],
    'phil' : ["python", 'java'],
    "sandy" : ["python", "c"]
}

for name, languages in favourite_language.items():
   if len(languages) > 1:
       print("\n" + name.title() + "'s favourite languages are : ")
       for language in languages:
           print(language.title())
   else:
       print("\n" + name.title() + "'s favourite languages is : ")
       for language in languages:
           print(language.title())