from logtype_helper import LogType
from country_exceptions import CountryExceptions
from ip_exceptions import IPExceptions

### USAGE ###
"""
1. Import the ExceptionsAsCode class into your detections
    from exceptions import ExceptionsAsCode

2. Initialize the class of the helper for your use case
    Ex. Country Exceptions
    COUNTRY_EXCEPTIONS = ExceptionsAsCode().country_exceptions()

3. Retrieve the lookup you want to use. They are stored as dictionaries or sets
    EMPLOYEE_EXCEPTIONS = github_helper.get_fulltime_employee_exceptions()
"""

class ExceptionsAsCode:
    def __init__(self):
        pass

    def logtype(self):
        # Returns the AWSHelper object
        """Functions
        get_service_accounts()  # Returns a set of service accounts
        get_employee_exceptions  # Returns a dictionary of prod account ids
            Key: Email || Value: IP
        """
        return LogType()

    def country_exceptions(self):
        # Returns the CountryExceptionHelper object
        """Functions
        get_fulltime_employee_exceptions()   # Returns a dictionary of exceptions for employees in unallowed countries
            Key: Okta name || Value: Country
        get_country_allowlist()     # Returns a set of allowed countries
        """
        return CountryExceptions()

    def ip_exceptions(self):
        # Returns the IPExceptions object
        """Functions
        get_office_ips()    # Returns a set of known office IPs
        """
        return IPExceptions()