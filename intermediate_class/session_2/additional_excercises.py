# 1. Create a function named preprocessor that takes in 2 arguments:
#        a. a string parameter named str_to_process
#        b. a number parameter named num_for_process

# 2. num_for_process is optional and has a default value of 7

# 3. Inside the body of preprocessor perform the following
#        a. verify that the string parameter is at least num_for_process
#           characters long. Return False if it doesn't meet this requirement.
#        b. verify that str_to_process only has lowercase letters and/or
#           digits. Return False if it doesn't meet this requirement.
#        c. sort the characters in the string, numbers first
#               So 'rf8b132ac' becomes '1238abcfr'

# 4. The last thing in the preprocessor function should be it returning the
#    transformed string


# 5. Create a function called processor that takes in one required argument:
#        a. a string parameter named str_to_process

# 6. In the body of processor, do the following:
#        a. convert the string into a list in reverse order

# 7. The last thing in the processor function should be it returning the list


# 8. Create a function called postprocessor that takes in one required argument:
#        a. a list parameter named list_to_process

# 9. In the body of postprocessor, do the following:
#        a. verify that list_to_process is a list. Return False if it
#           doesn't meet this requirement.
#        b. write list_to_process to a file one list element per line


# 10. Write a function called wrapper, that takes in three aruments:
#         a. a required function parameter named proc
#         b. an optional function parameter named preproc
#         b. an optional function parameter named postproc

# 11. In the body of wrapper, call the three input functions in order (pre,
#     proc, post) if they were supplied. Add prints to show flow.

# 12. When calling the functions inside of wrapper, provide some valid
#     parameters to those functions
