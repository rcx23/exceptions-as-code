class IPExceptions:
    def __init__(self):
        pass
        
    def get_office_ips(self):
        # Returns a set of known office IPs
        exceptions = {
            "1.1.1.1",
            "1.1.1.2",
            "1.1.1.3"
        }
        
        return exceptions