# A tuple is an immutable list
# immutable means it cannot be changed
# [] - list
# {k:v} - dictionary
# () - tuple

# declaring an empty tuple
empty_tuple = ()

# declaring a tuple with elements inside
my_tuple = ("Fantasy", "Mystery", "Poetry")
print(type(my_tuple))

# several items separated by a comma
my_stuff = "Guitar", "Bass Guitar", "Nintendo Switch"
print(type(my_stuff))

# setting variables on one line is just assigning variables to positions within a tuple
instrument, instrument2, game = "Guitar", "Bass Guitar", "Nintendo Switch"
print(instrument)
print(instrument2)
print(game)

# unpacking a tuple
instrument, instrument2, game = my_stuff
print(instrument)
print(instrument2)
print(game)

# recreating the tuple
more_stuff = instrument, instrument2, game 
print(more_stuff)

# indexing into a tuple
my_tuple = ("Fantasy", "Mystery", "Poetry")
print(my_tuple[1])

# BUT I cannot reassign the value at index 1
# my_tuple[1] = "Adventure" TypeError - Tuple does not support item assignment - immutable

# creating a tuple with one item
single_item_tuple = ("Mega Man",) # we give it the thing in the tuple and the a comma immediately following it
print(single_item_tuple)

# nested structures in our tuple
plot = "Prologue", "Conflict", ["Climax", 'Resolution']
print(plot)
print(plot[2])
# reassigning an item within a list within a tuple
plot[2][1] = "This is the end, my only friend, the end"
print(plot)
# appending to a list within a tuple
plot[2].append("Another thing")
print(plot)

# tuple within a tuple
nested_tuple = ("Foreword", ("Chapter 1", "Chapter 2"), "Epilogue")
print(nested_tuple)
print(nested_tuple[1])
print(nested_tuple[1][1]) # indexes into the nested tuple
# trying to reassign within the nested tuple
# nested_tuple[1][1] = "Chapter 1a" - TypeError

# slice tuples
my_tuple = ("Prologue", "Adventure", "Epilogue")
print(my_tuple[0:2]) # maintains the tuple type
new_tuple = my_tuple[0:2]
print(new_tuple)
print(my_tuple[::2])

# multiple nested tuples
historical_record = ("Medieval Era", ("Knights", "Castles", ("King", "Queen")), "Renaissance Period")
print(historical_record)
print(historical_record[1]) #("Knights", "Castles", ("King", "Queen"))
print(historical_record[1][2]) # ("King", "Queen")
print(historical_record[1][2][0]) # "King"

# dictionaries nested in tuples
enchanted_library = ("Chapter 1", {"Mythical Creatures": ["Dragon", "Unicorn"], "Legendary Places": ("Atlantis", "El Dorado")}, "Chapter 2")
# accessing values in a nested dictionary
mystical_horse = enchanted_library[1]["Mythical Creatures"][1]
print(mystical_horse)

# accessing the tuple in a nested dictionary
sunken_city = enchanted_library[1]["Legendary Places"][0]
print(sunken_city)
# trying to reassign a value in the above tuple
# enchanted_library[1]["Legendary Places"][0] = "California" TypeError

# Modifying Tuples - janky
my_tuple = ("Introduction", "Conclusion")
print(my_tuple)
# my_tuple.append("Epilogue") AttributeError - tuple does not have an append method
# turn the tuple into a list, append, then back to the tuple
my_list = list(my_tuple)
print(my_list)
# appending to the list version of the tuple
my_list.append("Epilogue")
print(my_list)
# converting back to a tuple
my_tuple = tuple(my_list)
print(my_tuple)

# sorting a tuple use sorted()
my_nums = (2, 1, 3, 4, 10, 7, 12, 20, 64, 14)
sorted_nums = sorted(my_nums) #makes a list copy and sorts the contents
print(sorted_nums)
print(my_nums) #my_nums variable remains unchanged
my_nums = tuple(sorted_nums)
print(my_nums)
tuple_names = ("Blake", "Skylar", "Stephen", "Jeremiah")
sorted_names = sorted(tuple_names)
print(sorted_names)
tuple_names = tuple(sorted_names)
print(tuple_names)

# .sort() will throw an AttributeError
my_nums = (2, 1, 3, 4, 10, 7, 12, 20, 64, 14)
# my_nums.sort() AttributeError - tuple object has no attribute sort

# enchanted_library = ("Chapter 1", {"Mythical Creatures": ["Dragon", "Unicorn"], "Legendary Places": ("Atlantis", "El Dorado")}, "Chapter 2")
# print(sorted(enchanted_library)) TypeError cant compare strings to dictionaries
my_nums = [1, 2, "3"]
# print(sorted(my_nums)) TypeError cant compare strings to integers

# Extended Unpacking
# if we have more items in the tuple (or iterable) than we have variables to set
# we can unpack multiple elements to one variable using *
my_tuple = ("Prologue", "Adventure", "Second Adventure", "Climax", "Epilogue")
# regular unpacking
# beginning, cool_part, middle, end = my_tuple
# print(beginning, cool_part, middle, end)
# setting a variable with * to unpack multiple items
beginning, *middle, end = my_tuple
print(beginning)
print(middle)
print(end)
# whichever variable has the * will pick up the slack from the unassigned items

# looples with tuples
# for loop
book_titles = ("Moby Dick", "1984", "The Hobbit")
for book in book_titles:
    print(book)

# while loop
#                 0                  1               2
authors = ("Herman Melville", "George Orwell", "JRR Tolkien") #length == 2
index = 0
while index < len(authors):
    print(authors[index])
    index += 1

# enumerating a tuple
chapters = ("The Lighthouse", "The Ministry of Truth", "The Trial")
# chapters = list(chapters)
for index, chapter in enumerate(chapters):
    print(f"Chapter {index + 1}: {chapter}")
    # if chapters[index] == "The Trial":
    #     chapters[index] = "Something Else" TypeError

# looping through nested tuples
nested_tales = (("The Dawn", "The Noon"), ("The Dusk", "The Night"))
for pair in nested_tales:
    # print(pair)
    for tale in pair:
        print(tale)


print() # empty print to give us some space in the terminal
# unpacking each tuple within a tuple
for tale1, tale2 in nested_tales:
    print(tale1)
    print(tale2)

# looping through nested structures 
# we can check the type of the the nested structures
mixed_collection = ("Poetry", ["Sonnet", "Haiku"], "Prose")
# isinstance(object, type)
for element in mixed_collection:
    if isinstance(element, list):
        print(element)
        for item in element:
            print(f"List item : {item}")
    else:
        print(f"Tuple Element: {element}")

# checking for a nested dictionary
historical_records = ("Ancient", {"Rome": "Republic", "Greece": "Democracy"}, "Medieval")
for element in historical_records:
    # check if the current element is a dictionary
    if isinstance(element, dict):
        # start a second for loop, looping through the key, value pairs
        for key, value in element.items():
            print(f"{key} was a {value}")
    else:
        print(element)

# tuple methods
# tuple.count("thing we're counting")
# counts the number of occurrences for a specific item in the tuple
literary_elements = ("Irony", "Metaphor", "Irony", "Symbolism")
print(literary_elements.count("Irony")) #2

# tuple.index(thing we want position of)
# returns the index of the thing we're searching for
book_chapters = ("Introduction", "Rising Action", "Climax", "Conclusion")
# index of "Climax"
print(book_chapters.index("Rising Action")) # 1 <- index

# for i in range(len(book_chapters)):
#     if book_chapters[i] == "Rising Action":
#         print(i)

# Combining Tuples - Tuple Concatenation
epic = ("Odyssey", "Iliad")
drama = ("Hamlet", "Othello")
literary_union = epic + drama
book1, book2, book3, book4 = literary_union

print(literary_union)

# creating a new tuple with tuples
# maintaining the structure of the original tuples
library = (epic, drama)
book1, book2 = library
print(book1)
print(book2)
print(library)

# membership checks in a tuple
# if something in tuple:
#      do something
if "Odyssey" in literary_union:
    print("Epic tale found!")



    










