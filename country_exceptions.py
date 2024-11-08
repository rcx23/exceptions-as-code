class CountryExceptions:
    def __init__(self):
        pass
        
    def get_fulltime_employee_exceptions(self):
        # Returns a dictionary of exceptions for employees in foreign countries
        # Used for travel or known work in another country.
        # Key: Username || Value: Country
        exceptions = {
            "JohnDoe"           : "India",
            "JeffRoss"          : "South Korea",
            "MaryPoppins"       : "Netherlands",
        }

        return exceptions
    
    def get_country_allowlist(self):
        # Returns a set of exceptions for allowed countries on the default unallowed list
        exceptions = {
            "India",
            "Indonesia",
            "Russia"
        }

        return exceptions