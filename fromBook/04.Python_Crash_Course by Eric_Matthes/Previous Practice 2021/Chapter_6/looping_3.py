fav_languages = {
    "susmita" : "python",
    "sandy" : "c",
    "rudra" : "ruby",
    "sobbo" : "python"
}

print("The following languages are mentioned:")

#print the item only once, don't repeat
for language in set(fav_languages.values()):
    print(language)