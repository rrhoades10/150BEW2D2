# a set is an ordered collection of elements that can contain NO duplicates
# unordered - it has no indexes
# [] - list
# {k:v} - dictionary
# () - tuple
# {"Krillin"} - set - squiggly braces without k,v pairs

# Declaring a set
party_guests = {"Alice", "Bob", "Charlie"}
print(party_guests)
print(type(party_guests))

# Declaring an empty set
# {} <- reserved for dictionaries
# set()
empty_set = set()
print(empty_set)

# has no duplicates
ticket_numbers = {1, 2, 3, 4, 5, 5, 5, 5, 5}
print(ticket_numbers) # removes all by one 5

# removing duplicates from a list
ticket_numbers = [1, 2, 3, 3, 4, 4, 4, 5, 5, 6]
set_numbers = set(ticket_numbers)
print(set_numbers)
ticket_numbers = list(set_numbers)
print(ticket_numbers)

# set() - tuple or list to set
# tuple() - set or list to tuple
# list - set or tuple to list
tuple_guests = ("Alice", "Bob", "Charlies")
set_party = set(tuple_guests)
print(set_party)

# unique name party 
dict_guests = {
    "name1": "Alice",
    "name2": "Bob",
    "name3": "Alice"
}

print(dict_guests.values())
unique_name_party = set(dict_guests.values())
print(unique_name_party)

# sets are unordered so we cannot index into them
party_guests = {"Alice", "Bob", "Charlie"}
# print(party_guests[1]) TypeError - set object is not subscriptable

numbers = {10, 1, 4, 2, 3, 19, 17, 5}
sorted_nums = sorted(numbers)
print(sorted_nums)
numbers = set(sorted_nums)
print(numbers)

# Looping through sets
party_guests = {"Sydney", "Swathy", "Blake", "Jeremiah", "Stephen"}
for guest in party_guests:
    print(f"{guest} LOVES to party!")

# membership checks in sets
# if something in our_set:
#    do something

party_guests = {"Sydney", "Swathy", "Blake", "Jeremiah", "Stephen", "Jessica"}

if "Jessica" in party_guests:
    print("Jessica also LOVES to party")
else:
    print("Maybe Jessica loves to party, but she wasn't at this party.")

print(len(party_guests))

for thing, thing2 in enumerate(party_guests):
    print(thing, thing2)

# SET METHODS
# set.add(thing we're adding to the set)
# trying to apped to a set
party_guests = {"Sydney", "Swathy", "Blake", "Jeremiah", "Stephen", "Jessica"}
# party_guests.append("Anthony") set has not attribute appen
party_guests.add("Anthony")
print(party_guests)

# if we try to add something that already exists the duplicate is removed
party_guests.add("Anthony")
print(party_guests)

# set.update(iterable)
party_guests = {"Sydney", "Swathy", "Blake", "Jeremiah", "Stephen", "Jessica"}
party_guests.update({"Skylar", "Vanady"})
print(party_guests)
# update takes in lists and tuples as well
# then converts them to the set
# list
party_guests.update(["Ryan", "Jessica"])
print(party_guests)
# tuple
party_guests.update(("Anthony", "Anthony", "Stephen"))
print(party_guests)

# sets are mutable, the contents of a set are not
# we cant index into sets to change the contents once they've been declared

# removing from sets
# set.remove("whatever we're removing")
# throws an error if the element doesnt exist
print(party_guests)
party_guests.remove("Ryan") # if element does not exist we get a KeyError
print(party_guests)

# set.discard("whatever we're discarding")
# does throw an error if the element doesnt exist within the set
party_guests.discard("Gertrude") #Gertrude doesnt exist, but no errors

# any immutable type can live within a set
# any of the rules for a dictionary key applies to what can live in sets
list_set = {(1,2,3), (1,2,3), 5, 6, 7}
print(list_set)

# set.pop() - removes and returns a random item from the set
lost_friend = party_guests.pop()
print(lost_friend)
print(party_guests)

# set.clear() - wipes the whole set
# party is over, everyone must leave
party_guests.clear()
print(party_guests)

# set methods for finding similarities and differences between two sets
# set1.union(set2)
# combines two sets into one - removing any duplicate elements
# the order does not matter - which set is calling the method and which set is being called upon
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}
gathering = set1.union(set2)
print(gathering)

# set1.intersection(set2)
# return the similarities between two sets
# order doesn't matter
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}
mutuals = set1.intersection(set2)
print(mutuals)

# set1.difference(set2)
# order matters, what is in the first set that isnt in the second set
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}
exclusive_friends = set1.difference(set2)
print(exclusive_friends)

# set1.symmetric_difference(set2)
# returns items from either set that arent in both
# order doesn't matter
unique_friends = set1.symmetric_difference(set2)
print(unique_friends)

# enumerate
guests = {"Alice", "Bob", "Charlie"}
for index, guest in enumerate(guests):
    print(f"Welcome, guest #{index + 1}...{guest}")

# set comprehension
# adding to a set within a set
# squaring each number from 0 to 6
# list comprehension
#               transform for loop in whatever we're looping through
squared_nums = [num**2 for num in range(6)]
print(squared_nums)
squared_set = {num**2 for num in range(6)}
print(squared_set)

# square each number from a list - remove duplicate squares
nums = [1, 2, 2, 4, 10, 10, 16, 11, 5, 3, 5, 9]
#              transform for loop in whatever we're looping through condition
squared_set = {num**2 for num in nums if num % 2 == 0} # only square the even
print(squared_set)

# regular for loop adding to a set
squared_set = set()
for num in nums:
    if num % 2 == 0:
        squared_set.add(num**2)







