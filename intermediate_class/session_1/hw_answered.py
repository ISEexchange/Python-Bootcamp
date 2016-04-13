#################################
# In Class Assignment and Homework
#################################


# 1. Gimme a dictionary:
#    Given a list of numbers provide a dictionary where the key is the
#    number and the value is that number's occurence in the list

#    GIVEN:
#    the_list = [1,2,3,2,3,2,1,3,3,2,1,3,3,4,4,5,6,7,878,7,6,5,5,7,78]

#    PRODUCE:
#    the_dictionary = {1: 3, 2: 4, 3: 6, 4: 2, 5: 3, 6: 2, 7: 3, 878: 1, 78: 1}

# Answer 1: count manually
the_list = [1,2,3,2,3,2,1,3,3,2,1,3,3,4,4,5,6,7,878,7,6,5,5,7,78]
the_dictionary = {}

for num in the_list:
    # First time num is being added to the dictionary as the key
    if num not in the_dictionary:
        the_dictionary[num] = 1
    # Otherwise its already in there so increment counter
    else:
        the_dictionary[num] = the_dictionary[num] + 1

print '\nQuestion 1 Answer 1'
print the_list
print the_dictionary

# Answer 2: use the count() lists have
the_list = [1,2,3,2,3,2,1,3,3,2,1,3,3,4,4,5,6,7,878,7,6,5,5,7,78]
the_dictionary = {}

for num in the_list:
    if num not in the_dictionary:
        the_dictionary[num] = the_list.count(num)

print '\nQuestion 1 Answer 2'
print the_list
print the_dictionary


# 2. Replace with number:
#    Given a string, replace a group of identical characters with itself and
#    how many times it appeared in that particular group

#    GIVEN:
#    'aaabbbfccccc'

#    PRODUCE:
#    a3b3f1c5

# Answer 1: Update new string on new character

the_string = 'aaabbbfccccc'
new_string = ''

current_counter = 0
last_character = ''

for index, character in enumerate(the_string):
    # Check if current character is the same as the last one
    if character == last_character:
        current_counter += 1
    # We're seeing a new character compared to the last
    if last_character != '' and character != last_character:
        # Add one to account for current character
        current_counter += 1
        new_string += last_character + str(current_counter)
        current_counter = 0
    # Account for last character
    if index == len(the_string) - 1:
        current_counter += 1
        new_string += character + str(current_counter)

    last_character = character

print '\nQuestion 2 Answer 1'
print the_string
print new_string


# Answer 2: Update new string as you go, char by char, and use string indexing
# to update the counters

new_string = ''

current_counter = 0
last_character = ''

for character in the_string:
    # Check if current character is the same as the last one
    if character == last_character:
        new_string = new_string[0:-1] + str(int(new_string[-1])+1)
    elif character != last_character:
        new_string += character + '1'

    last_character = character

print '\nQuestion 2 Answer 2'
print the_string
print new_string
