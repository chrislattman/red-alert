'''
This is the public API that we share with other websites/apps.
'''
import db # this is just whatever db we end up using 

def flag_suspicious_phone(phone):
    pass

def flag_suspicious_address(addr):
    pass

def flag_suspicious_image(img):
    # compares to hash using https://perception.thorn.engineering/en/latest/index.html api
    pass

def flag_suspicious_email(email):
    # flag based on both the email string and the email domain
    domain = email.split('@')[1]
    domain_sus = db.is_domain_suspicious(domain)
    email_sus = db.is_email_suspicious(email)

    # return relevant info as json
    return (domain_sus, email_sus)

def flag_suspicious_ip(ip):
    return db.is_ip_suspicious(ip)

def flag_suspicious_listing(listing):
    # this will call all the above functions
    pass
