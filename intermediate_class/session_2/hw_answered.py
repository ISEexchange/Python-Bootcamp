#################################
# In Class Assignment and Homework
#################################

# Thermostat

# Create a Thermostat class to simulate a real life (or not) thermostat.
# Some internal data members your class should have:
#     current temperature
#     degree type (F or C)
#     user's desired temperature
#     number of attached air conditioners
#     number of attached heaters
#     people detector enabled
#     AC fan speeds
#     heater fan speeds
# Some internal methods your class should have:
#     turn desired temperature up
#     turn desired temperatur down
#     set desired temperature
#     add an AC
#     add a heater
#     remove an AC
#     remove a heater
#     auto temp calculation based on people
#     current temperature display
#     AC and heater count display

# Now use the above class in a building climate control system.
# Instantiate at least three thermostat objects, one per room/floor in a
# building. Each thermostat is responsible for controlling the temperature
# of that room/floor. After instantiating the objects, call all of their
# functions in some way. Add print statements inside of your class methods
# so that they describe what it is doing.

# BONUS:
# Create a command line interface for your building climate control system!
# Allow a user to start up your script and then see thermostat details along
# with a menu. Maybe something like:
#
# ************************************************************************
#                WELCOME TO THE INTERNATIONAL SPACE STATION
#                    CLIMATE CONTROL MANAGEMENT CONSOLE
# ************************************************************************
#
# Tranquility Module:
#     Current Temperature: 75 degrees F
#     Humidity Level: 22 %
#     AC #1: Off
#     AC #2: On
#     AC #1 Fan Speed: 0
#     AC #2 Fan Speed: 30 %
#     Number of Inhabitants: 1
#
# Awesome Science Module:
#     Current Temperature: 65 degrees F
#     Humidity Level: 7 %
#     ...
#
# What action would you like to take? (enter number or q to exit)
#     1. Change desired temperature for a module
#     2. Add AC to module
#     ...
#
# 1
#
# OK, Which module would you like to change the desired temperature for?
#     1. Tranquility Module
#     2. Awesome Science Module
#
# 2
#
# OK, The current desired temperature is 75 degrees F. What is the new
# desired temperature?
#
# 78
#
# OK, Spinning up a heater for you now.
#
# What action would you like to take? (enter number or q to exit)
#     1. Change desired temperature for a module
#     2. Add AC to module
#     ...


import random


class Thermostat(object):
    """ Simulate a real life (or not) thermostat """

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


if __name__ == "__main__":

    print """
        ************************************************************************
                        WELCOME TO THE INTERNATIONAL SPACE STATION
                            CLIMATE CONTROL MANAGEMENT CONSOLE
        ************************************************************************
    """

    tranquility = Thermostat('Tranquility Module')
    awesome     = Thermostat('Awesome Science Module')
    plant       = Thermostat('Plant Growth Module')

    print ''

    print tranquility
    print awesome
    print plant

    print '\n\nRemove / Add ACs and heaters\n\n'
    tranquility.add_AC()
    awesome.add_heater()
    plant.remove_AC()

    print '\n'
    print tranquility
    print awesome
    print plant

    print '\n\nChange the desired temperature\n\n'
    tranquility.turn_desired_temperature_up()
    awesome.turn_desired_temperature_down()
    awesome.turn_desired_temperature_down()
    awesome.turn_desired_temperature_down()
    awesome.turn_desired_temperature_down()
    plant.set_desired_temperature(98)

    print '\n'
    print tranquility
    print awesome
    print plant

    tranquility.ac_heater_info()
