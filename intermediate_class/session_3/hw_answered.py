#################################
# In Class Assignment and Homework
#################################

# 1. Write a function that takes in any number of un-named and named parameters.
# 2. Loop through the list of un-named parameters and print the values.
# 3. Loop through the dictionary of named parameters and print out the
#    parameter name and value.


def some_func(*args, **kwargs):
    """ Loop through input arguments and print values """

    print 'Positional Arguments:'
    for index, arg in enumerate(args, 1):
        print '    Argument #%s is %s' % (index, arg)

    print 'Keyword Arguments:'
    for arg_name, arg_value in kwargs.iteritems():
        print "    Argument '%s' has a value of '%s'" % (arg_name, arg_value)

    print '\n'

some_func(123, 'abc', 'def', some='thing', another=98876)


# Let's update the Thermostat class from session 2. You can update your own
# class or use the provided one in the homework solutions.

# 4. Add a class variable to the Thermostat class called MAX_BTU and give it some
#    default value. This class variable is a representation of how large of an
#    AC each thermostat can handle (measured in BTUs). All of the thermostats in
#    your system are the same so they can all share this one constant.
# 5. Add a class method that can allow an administrator to change this max
#    constant. The function definition should look like:
#        def update_max_btu(cls, new_max, admin_pasword)
#    Only if the correct admin password is provided can the class variable
#    then be updated.
# 6. Add a static method that wlil return the MAX_BTU value.

import random


class Thermostat(object):
    """ Simulate a real life (or not) thermostat """

    # Maximum AC power Thermostats can handle
    MAX_BTU = 22000

    def __init__(self, name):
        self.name              = name
        self.current_temp      = None
        self.degree_type       = 'f'
        self.desired_temp      = None
        self.num_acs           = 3
        self.num_heaters       = 3
        self.detect_people     = False
        self.ac_fan_speeds     = {}
        self.heater_fan_speeds = {}

        self._lower_bound = 65
        self._upper_bound = 85

        self._initialize()

    @classmethod
    def update_max_btu(cls, new_max, admin_password):

        print 'Checking password'
        if str(hash(admin_password)) != '1128553271950899605':
            print 'Error: Incorrect passowrd. Try again.'
            return False
        print 'Valid password. Continuing with update.'

        cls.MAX_BTU = new_max
        print 'New MAX_BTU: %s' % cls.MAX_BTU

        return True

    def _initialize(self):
        """ Set up more complicated initial values """

        print "Starting up '%s' thermostat" % self.name

        # Pick a random number for initial temperature
        self.current_temp = random.randint(self._lower_bound, self._upper_bound)
        self.desired_temp = self.current_temp

        for i in range(self.num_acs):
            self.ac_fan_speeds[i] = 0.50

        for i in range(self.num_heaters):
            self.heater_fan_speeds[i] = 0.50

    def _start_temp_change(self):
        """ Simulate what it takes to lower/increase the temperature """

        # Update the current temperature
        if self.desired_temp != self.current_temp:
            print 'Need to update temperature. Adjusting ACs and heaters.'
            # TODO: Simulate time needed for current_temp to reach desired temp
            self.current_temp = self.desired_temp
            print 'Done. New current temperature is now %s' % self.current_temp

        else:
            print 'Nothing to do. Current temperature matches desired temperature'

    def __str__(self):
        """ Provide a custom string for printing """
        to_print = 'Info about the %s thermostat\n' % self.name
        to_print += '  current_temp: %s %s\n'   % (self.current_temp, self.degree_type)

        to_print += '  degree_type: %s\n'       % self.degree_type
        to_print += '  desired_temp: %s\n'      % self.desired_temp
        to_print += '  num_acs: %s\n'           % self.num_acs
        to_print += '  num_heaters: %s\n'       % self.num_heaters
        to_print += '  detect_people: %s\n'     % self.detect_people
        to_print += '  ac_fan_speeds: %s\n'     % str(self.ac_fan_speeds)
        to_print += '  heater_fan_speeds: %s\n' % str(self.heater_fan_speeds)
        to_print += '\n'

        return to_print

    def turn_desired_temperature_up(self):
        """ Increase the desired temperature by one """

        print 'Current temperature: %s %s' % (self.current_temp, self.degree_type)
        self.desired_temp += 1
        print 'Desired temperature: %s %s' % (self.desired_temp, self.degree_type)

        self._start_temp_change()

    def turn_desired_temperature_down(self):
        """ Decrease the desired temperature by one """

        print 'Current temperature: %s %s' % (self.current_temp, self.degree_type)
        self.desired_temp -= 1
        print 'Desired temperature: %s %s' % (self.desired_temp, self.degree_type)

        self._start_temp_change()

    def set_desired_temperature(self, input_desired_temp):
        """ Set the desired temperature to a specific value """
        self.desired_temp = input_desired_temp
        self._start_temp_change()

    def add_AC(self):
        """ Add an AC to be managed by this thermostat """

        print 'Adding an AC to %s' % self.name
        self.num_acs += 1

        # Don't forget to set speed for new AC
        # TODO: combine self.num_acs and self.ac_fan_speeds
        self.ac_fan_speeds[self.num_acs-1] = 0.50

    def add_heater(self):
        """ Add a heater to be managed by this thermostat """

        print 'Adding a heater to %s' % self.name
        self.num_heaters += 1

        # Don't forget to set speed for new heater
        # TODO: combine self.num_heaters and self.heater_fan_speeds
        self.heater_fan_speeds[self.num_heaters-1] = 0.50

    def remove_AC(self):
        """ Remove an AC from being managed by this thermostat """

        print 'Removing an AC from %s' % self.name
        # First check if there is anything to remove
        if self.num_acs < 1:
            print 'Nothing to remove'
            return False

        # Don't forget to remove AC from self.ac_fan_speeds
        # TODO: combine self.num_acs and self.ac_fan_speeds
        self.ac_fan_speeds.pop(self.num_acs-1)

        # Now decrement the counter
        self.num_acs -= 1

    def remove_heater(self):
        """ Remove a heater from being managed by this thermostat """

        print 'Removing a heater from %s' % self.name
        # First check if there is anything to remove
        if self.num_heaters < 1:
            print 'Nothing to remove'
            return False

        # Don't forget to remove AC from self.heater_fan_speeds
        # TODO: combine self.num_heaters and self.heater_fan_speeds
        self.heater_fan_speeds.pop(self.num_heaters-1)

        # Now decrement the counter
        self.num_heaters -= 1

    def turn_on_auto_temp(self):
        """ Turn on auto temp which will change the temperature
            based on number of people present
        """
        print 'Turning on auto temp'
        self.detect_people = True

    def turn_off_auto_temp(self):
        """ Turn off auto temperature management """
        print 'Turning off auto temp'
        self.detect_people = False

    def display_current_temp(self):
        """ Print out the current termperature """
        print 'Current Temperature: %s' % self.current_temp

    def ac_heater_info(self):
        """ Print out the AC and heater info """

        print 'AC Info'
        for ac, speed in self.ac_fan_speeds.iteritems():
            print 'AC %s has fan speed of %s' % (ac, speed)

        print 'Heater Info'
        for heater, speed in self.heater_fan_speeds.iteritems():
            print 'Heater %s has fan speed of %s' % (heater, speed)


print '############################################################'
print 'Current MAX_BTU (printed via class not instance): ', Thermostat.MAX_BTU

print '\nUpdating MAX_BTU via class'
Thermostat.update_max_btu(17500, 'something')
print 'Current MAX_BTU (printed via class not instance): ', Thermostat.MAX_BTU

print '\nUpdating MAX_BTU via instance'
thermo_1 = Thermostat('Max BTU Tester')
thermo_1.update_max_btu(12000, 'something')
print 'Current MAX_BTU (printed via instance not class): ', thermo_1.MAX_BTU
print 'Current MAX_BTU (printed via class not instance): ', Thermostat.MAX_BTU
print '############################################################\n\n'


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
