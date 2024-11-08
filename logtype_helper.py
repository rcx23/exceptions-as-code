class LogType:
    def __init__(self):
        pass
    
    def get_service_accounts(self):
        # Returns a set of service accounts
        allowed_accounts = {
            "svc-infrastructure",
            "svc-access-role",
            "svc-jenkins",
        }
        
        return allowed_accounts
    
    def get_employee_exceptions(self):
        # Returns a dictionary of exceptions for user email and IP
        # ***** Comment use case/reasoning for exception
        # Key: Email || Value: IP
        gd_exceptions = {
            "firstname.lastname@company.com": "1.1.1.1"  # Reason For Exception: Known false positive on user's home IP
        }

        return gd_exceptions