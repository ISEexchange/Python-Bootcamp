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
