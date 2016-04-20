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


import string


def preprocessor(str_to_process, num_for_process=7):
    """ Verify and sort the input string"""

    if len(str_to_process) < num_for_process:
        print 'String input must be at least as long as number input'
        return False

    allowed_chars = string.lowercase + string.digits
    for c in str_to_process:
        if c not in allowed_chars:
            print ("'%s' is not an allowed character. Only lowercase and digits "
                "are allowed" % c)
            return False

    sorted_str = ''.join(sorted(str_to_process))

    return sorted_str


# 5. Create a function called processor that takes in one required argument:
#        a. a string parameter named str_to_process

# 6. In the body of processor, do the following:
#        a. convert the string into a list in reverse order

# 7. The last thing in the processor function should be it returning the list

def processor(str_to_process):
    """ Generate a list from string in reverse order """

    str_list = list(str_to_process)
    str_list.reverse()
    return str_list

# 8. Create a function called postprocessor that takes in one required argument:
#        a. a list parameter named list_to_process

# 9. In the body of postprocessor, do the following:
#        a. verify that list_to_process is a list. Return False if it
#           doesn't meet this requirement.
#        b. write list_to_process to a file one list element per line

def postprocessor(list_to_process):
    """ Write list to file """

    if type(list_to_process) != list:
        print 'Input argument must be a list'
        return False

    file_handle = open('newfile.txt', 'w')

    for element in list_to_process:
        file_handle.write(element + '\n')

    file_handle.close()

    return True

# 10. Write a function called wrapper, that takes in three aruments:
#         a. a required function parameter named proc
#         b. an optional function parameter named preproc
#         b. an optional function parameter named postproc

# 11. In the body of wrapper, call the three input functions in order (pre,
#     proc, post) if they were supplied. Add prints to show flow.

# 12. When calling the functions inside of wrapper, provide some valid
#     parameters to those functions

def wrapper(proc, preproc=None, postproc=None):
    """ Call the supplied functions in order """

    str_to_process = ''

    if preproc is not None:
        pre_arg_1 = 'lasjhdf87873r3lkjd'
        pre_arg_2 = 9
        print ('Calling pre-processor with two arguments: %s and %s'
            % (pre_arg_1, pre_arg_2))
        str_to_process = preproc(pre_arg_1, pre_arg_2)

    if str_to_process is False:
        print 'Error encountered'
        return False

    print 'Calling processor with argument: %s' % str_to_process
    list_to_process = proc(str_to_process)

    post_return = None
    if postproc is not None:
        print 'Calling post-processor with argument: %s' % list_to_process
        post_return = postproc(list_to_process)

    if post_return is False:
        print 'Error encountered'
        return False

    return True

print wrapper(processor, preprocessor, postprocessor)
