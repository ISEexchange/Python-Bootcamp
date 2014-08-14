'''
Function searches through a file and checks for the presence of a specified string.
If there are any occurrences of this string, the function return True, otherwise False.
The function also takes an optional parameter to provide an extract of x lines before and after
the occurrence of the search string in the file.
Additionally the user can also chose to get a paged output to get extract in batches
The function also provides an option to highlight the search string in the extracted text for better readability

Author: Girish Ganeshan
'''

import os

def view_extract_from_file(file_name, search_string, case_sensitive=True, extract_lines=0,isuserinput=False,color_output=False):
    # Implement Function Below
    file_open = open(file_name, 'r')
    # Contains the line number at which the search string was found
    line_num = 0
    # Contains the count of occurrence of the search string
    num_of_lines = 0
    # clear the screen for an enhanced understanding of the output
    # os.system('cls' if os.name == 'nt' else 'clear')
    if (case_sensitive == True):
        print '\nPerforming case sensitive search for the string \'%s\' in file %s' % (search_string,file_name)
    else :
        print '\nPerforming case insensitive search for the string \'%s\' in file %s' % (search_string,file_name)
    for file_line in file_open:
        # Remove trailing blank spaces
        file_line = file_line.rstrip()
        # If case insensitive convert the file and search string to upper case
        if (case_sensitive == False):
            file_line_cs = file_line.upper()
            search_string_cs = search_string.upper()
            string_found = file_line_cs.find(search_string_cs)
        else :
            string_found = file_line.find(search_string)
        # Irrespective of whether search string is found increase the line number counter
        line_num = line_num + 1
        if (string_found != -1):
            # If search string is found increment the number of lines counter
            num_of_lines = num_of_lines + 1
            # a new string to contain the start of extract value
            start_of_extract = line_num - extract_lines
            # if start of extract is negative the program will break.
            if (start_of_extract < 0):
                start_of_extract = 0
            # a variable to contain the end of extract value.
            end_of_extract = line_num + extract_lines
            # counter to determine which lines are printed
            file_extract_counter = 1
            print '\nFound the search string \'%s\' in file %s' % (search_string,file_name)
            if (extract_lines > 0):
                # print file_extract_counter
                print '\n------ You chose to get an extract of %d line before and after the search string --------' % (extract_lines)
                print '\n------------------- Start of Extracted File content #%d -----------------' % (num_of_lines)
            # open the file again to go through specific lines only.
            file_extract = open(file_name, 'r')
            # Loop through a specific set of lines in the file to print the extract
            for file_line_extract in file_extract:
                file_line_extract = file_line_extract.rstrip()
                if ((file_extract_counter >= start_of_extract) and (file_extract_counter <= end_of_extract)):
                    # If color_output is true check if the line is where the match was found, if so highlight it
                    if (color_output == True):
                        # This is where the match was found so highlight it
                        if (file_extract_counter == line_num):
                            print '\033[0;32m%s\033[m' % (file_line_extract)
                        else:
                            print '%s' % (file_line_extract)
                    # For no colored output print as is
                    else:
                        print '%s' % (file_line_extract)
                file_extract_counter = file_extract_counter + 1
            print '\nFile: %s \ncontains: %s \nat line number: %d ' % (file_name,search_string,line_num)
            if (extract_lines > 0):
                # print file_extract_counter
                print '\n------------------- End of Extracted File content #%d -----------------' % (num_of_lines)
            # If user choses to get a page by page ouput then wait for the input before looping further
            if (isuserinput == True):
                print '\nYou chose to fetch paged output, kindly hit enter to get the next extract !!!'
                userinput = raw_input()
                continue

    if (num_of_lines != 0):
        print '\nFound \'%s\' %d time(s) in the file %s \n' % (search_string,num_of_lines,file_name)
        return True
    else:
        print '\nDid not find \'%s\' in the file %s' % (search_string,file_name)
        return False

# clear the screen for an enhanced viewing experience of the output
os.system('cls' if os.name == 'nt' else 'clear')
view_extract_from_file('/home/python_bootcamp/file_manipulation/ISE.BusinessServiceInterface.exe.config','LogLevel',True,0,False)
#view_extract_from_file('/home/python_bootcamp/file_manipulation/ISE.BusinessServiceInterface.exe.config','loglevel',False)
#view_extract_from_file('/home/python_bootcamp/file_manipulation/ISE.BusinessServiceInterface.exe.config','ISE.Library',True,5)
view_extract_from_file('/home/python_bootcamp/file_manipulation/ISE.BusinessServiceInterface.exe.config','add key',False,5,True,True)
#view_extract_from_file('/home/python_bootcamp/file_manipulation/ISE.BusinessServiceInterface.exe.config','Girish')


# Execute Function below
# File Path: '/home/python_bootcamp/file_manipulation/ISE.BusinessServiceInterface.exe.config'
# Ex. Search Strings : 'LogLevel'
#                    : 'ISE.Library'
#                    : 'add key'
