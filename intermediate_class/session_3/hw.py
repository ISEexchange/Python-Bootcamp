#################################
# In Class Assignment and Homework
#################################

# 1. Write a function that takes in any number of un-named and named parameters.
# 2. Loop through the list of un-named parameters and print the values.
# 3. Loop through the dictionary of named parameters and print out the
#    parameter name and value.

# Let's update the Thermostat class from session 2. You can update your own
# class or use the provided one in the homework solutions.

# 4. Add a class variable to the Thermostat class called MAX_BTU and give it some
#    default value. This class variable is a representation of how large of an
#    AC each thermostat can handle (measured in BTUs). All of the thermostats in
#    your system are the same so they can all share this one constant.
# 5. Add a class method that can allow an administrator to change this max
#    constant. The function definition should look like:
#        def update_max_btu(cls, admin_pasword)
#    Only if the correct admin password is provided can the class variable
#    then be updated.
# 6. Add a static method that wlil return the MAX_BTU value.

# Let's practice inheritance!

# 7. We now need to store more information about the individual AC and heater
#    components.
#    Create three new classes:
#        1. TemperatureChanger
#        2. AirConditioner (inherits from TemperatureChanger)
#        3. HeatingUnit    (inherits from TemperatureChanger)
# 8. TemperatureChanger contains:
#        an instance variable for on/off
#        an instance variable for fanspeed
#        instance methods for setting on/off and fanspeed
# 9. AirConditioner contains:
#        an instance variable for BTU
# 10. HeatingUnit contains:
#        an instance variable for watts
# 11. Update the Thermostat class so that it contains a list or dictionary of
#     TemperatureChanger objects instead of whatever you had before for tracking
#     the ACs and heaters.

# Comprehensions!
# Think about what these are going to produce before running it!

# 12. Whats the value of A in:
#         A = [i for i in range(10, 100, 5)]

# 13. Whats the value of B in:
#         B = [i for i in range(10, 100, 3) if str(i)[0] in ('3','4','5')]

# 14. Whats the value of C in:
#         C = {i for i in [(1,2),(3,4),(5,6),(2,1),'a','b','c']}

# 15. Whats the value of D in:
#         import string
#         D = {i:i.lower() for i in string.letters.upper()}

# 16. Whats the value of E in:
#         E = [i for i in A for j in B if i == j]

# 17. Change the following function so a list comprehension is used
#
#         from string import lowercase, digits
#         str_to_process = 'O329u@T4Gs5-HH643.hf838'
#         allowed_chars = lowercase + digits
#
#         def checker(str_to_process):
#             for c in str_to_process:
#                 if c not in allowed_chars:
#                     return False
#             return True

# 18. If its not already, update checker() from above so that the body
#     is only one line of code
