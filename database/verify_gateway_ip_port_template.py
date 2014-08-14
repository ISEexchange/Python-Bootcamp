#!/usr/bin/python
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Author:       <NAME>
# Created Date: <DATE>
# Description:  <DESCRIPTION>
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


"""
INSTRUCTIONS:
    1. Create a function called 'verify_gateway_ip_port' that takes in
       three arguments: gateway_ip, gateway_port, gateway_name
    2. gateway_name is an optional argument and should have a default
       value of None
    3. Print an introductory sentence
    4. Login to OAT's CMDB database
    5. Execute this query and get the data using a cursor dictionary:
           SELECT P.ProcessName, H.OSHostName, G.Port
           FROM CMDB.Process P, CMDB.ProcessState PS, CMDB.GatewayConnectInfo G, CMDB.HostInfo H
           WHERE P.IsActive=1 and P.IsDeleted=0 and P.HostID!=0 and
           P.ProcessName like "Gateway-%" and PS.ProcessNameID=P.ProcessNameID and
           PS.ProcessNameID=G.ProcessNameID and H.HostID=P.HostID
           order by P.ProcessName;
    6. Based on what this query returns, figure out if the passed in function arguments
       are valid. So your code should be able to answer these questions:
           Are ip 'tc-oat99' and port '12345' valid gateway values
           Are ip 'tc-oat99' and port '12345' the correct values for Gateway-99_001
    7. Print a statement for each returned row
    8. Return True or False
"""

# Import required modules here:
import sys
# This will allow you to use a predefined database login function
sys.path.append("/home/bautcar/SVN_TestAutomation/RobotFramework/GtsEnvConfig")
from GtsEnvConfig import GtsEnvConfig


# Function goes here:


# Call your function inside here:
if __name__ == '__main__':
    pass # Replace this with your function call
