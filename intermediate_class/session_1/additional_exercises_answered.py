# 1. Initialize an empty list, list_1
list_1 = []

# 2. Initialize another list with 3 strings in it, list_2
list_2 = ['a', 'b', 'c']

# 3. Create a third list, list_3, that has all of list_2's items 4 times. Use
#    list multiplication
list_3 = list_2 * 4

# 4. Using a for loop, copy over list_3's items into list_1
for i in list_3:
    list_1.append(i)

# 5. Verify that list_1's length is equal to list_3 and that list_3's length
#    is exactly 4 times list_2's length. Use len().
#        a. Use if/else
#        b. Use assert
if len(list_1) == len(list_3):
    print 'list_1 == list_3'
else:
    print 'list_1 != list_3'

assert len(list_1) == len(list_3)

if len(list_3) == len(list_2) * 4:
    print 'list_3 == list_2 * 4'
else:
    print 'list_3 != list_2 * 4'

assert len(list_3) == len(list_2)*4

# 6. Use the count function that lists have to verify that each list_3 string
#    appears 4 times
#        a. Use one if with 3 clauses connected by and
#        b. Use one assert with 3 clauses connected by and
if list_3.count('a') == 4 and list_3.count('b') == 4 and list_3.count('c') == 4:
    print "list_3 has 4 a's, 4 b's and 4 c's"
else:
    print "list_3 does not have 4 a's, 4 b's and 4 c's"

assert list_3.count('a') == 4 and list_3.count('b') == 4 and list_3.count('c') == 4

# 7. Print every item in list_3 so that the output looks like the below (use
#    enumerate). First line of output should be for # 1 not # 0. Do this in
#    two lines of code.
#        List 3 Item # 1: <>
#        List 3 Item # 2: <>
#        List 3 Item # 3: <>
for i, element in enumerate(list_3, 1):
    print 'List 3 Item # %s: %s' % (i, element)


# 8. Initialize an empty dictionary, dict_1
dict_1 = {}

# 9. Populate dict_1 with 3 key-value pairs. Values can be anything, but keys:
#        a. the first key should be an int
#        b. the second key should be a string
#        c. the third key should be a tuple of anything
dict_1[1] = 'v1'
dict_1['2'] = 'v2'
dict_1[(3, 't')] = 'v3'

# 10. Store the keys in a new variable, dict_1_keys
dict_1_keys = dict_1.keys()

# 11. Store the values in a new variable, dict_1_vals
dict_1_vals = dict_1.values()

# 12. Zip dict_1_keys and dict_1_vals into a new varible, dict_1_zipped, using
#     the built in zip() function
dict_1_zipped = zip(dict_1_keys, dict_1_vals)

# 13. Create a new dictionary, dict_2, out of dict_1_zipped using dict()
dict_2 = dict(dict_1_zipped)

# 14. Verify that dict_1 and dict_2 are identical using ==
assert dict_1 == dict_2

# 15. Print every key-value pair in dict_1 so that the output looks like the
#     below. Use enumerate and the dictionary's iteritems() or items(). Do
#     this in two lines of code.
#         Dictionary 1 Pair # 0: Key = <>, Value = <>
#         Dictionary 1 Pair # 1: Key = <>, Value = <>
#         Dictionary 1 Pair # 2: Key = <>, Value = <>
for i, (k, v) in enumerate(dict_1.iteritems()):
    print 'Dictionary 1 Pair %s: Key = %s, Value = %s' % (i, k, v)


# 16. Assign variables a, b and c to values 1, 2 and 3 in one line using
#     a. no symbols other than commas and one equal sign
#     b. tuple unpacking
#     c. list unpacking
a, b, c = 1, 2, 3
a, b, c = (1, 2, 3)
a, b, c = [1, 2, 3]


# 17. Create a list of words (space separated) from the below string. Use a
#     function that strings have. Save the list in a variable called words.
#         some_string = "the big brown fox jumped over the canyon?!"
some_string = "the big brown fox jumped over the... canyon?!"
words = some_string.split()
print words

# 18. Modify the list so that the first letter in the first word is uppercase.
words[0] = words[0].capitalize()
print words

# 19. Modify the list so that the last word is all uppercase.
words[-1] = words[-1].upper()

# 20. Use the string module to see if any words contain any punctuation
#     characters. If a word contains any punctuation character remove it and save
#     the result in a new list called clean_words.
import string
for w in words:
    pass
