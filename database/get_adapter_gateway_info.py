#C:\Python26
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Author:       <NAME>
# Created Date: <DATE>
# Description:  <DESCRIPTION>
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------


"""
INSTRUCTIONS:
    1. Add a print function to the AdapterInfo class which should print the
       five values in the class
    2. Create a function called 'get_all_adapters_gateway_info' which does not
       take in any arguments.
    3. Print an introductory sentence inside this function
    4. Login to OAT's IORS database using get_data_from_mssql_db() and these
       connection parameters:
           server_port = DC-SQL01\SQM1,59897
           database    = iors_gts_oat_gts01
           user        = iors_gts_oat_gts01
           password    = iors_gts_oat_gts01
    5. Pass this query into get_data_from_mssql_db():
           SELECT * FROM iors_gts_oat_gts01.dbo.adapter_instance_config
           WHERE property_name in ('node', 'port', 'backupNode', 'backupPort');
    6. Make sure to save the data get_data_from_mssql_db returns in a variable.
    7. Create an object of type AdapterInfo and properly assign the values from
       the database into this new object. Make sure you create a new object for
       each adapter from the database. You should have 9 adapters/objects.
	8. Store each adapter_id, node and port in a dictionary
		- Key: adapter_id
		- Value: AdapterInfo object
    9. Print the adapter's details using the print function you created
    10. Return the dictionary
"""

# Import required modules here:



# Use this class to store the adapter's information
class AdapterInfo():
    """Class to contain adapter details for easy storage and access"""
    def __init__(self):
        self.adapter_id           = ''
        self.primary_gateway_node = ''
        self.primary_gateway_port = ''
        self.backup_gateway_node  = ''
        self.backup_gateway_port  = ''

    # Print function for this class goes here
    def print_info(self):
        # Add code here. Remove this pass statement!
        pass


def get_data_from_mssql_db(server_port, database, user, password, query):
    """This is a help function to make it easy to retrieve data from database"""
    print ('Connecting to:\n    server   = %s\n    database = %s\n    '
        'user     = %s\n    password = %s\n' % (server_port, database, user, password))
    conn = pyodbc.connect(driver='{SQL Server}',
        server=server_port, database=database, uid=user, pwd=password) 
    cursor = conn.cursor()

    print 'Executing query:\n    %s' % (query)
    cursor.execute(query)

    return cursor.fetchall()


# get_all_adapters_gateway_info() goes here:



# Call your function inside here:
if __name__ == '__main__':
    pass # Replace this with your function call
