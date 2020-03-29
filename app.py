import argparse
import api
from email.utils import parseaddr
import ipaddress
import json

def email_format_valid(email):
    return '@' in parseaddr(email)[1]

def phone_format_valid(phone):
    return True
    # if len(phone) != 12:
    #     return False
    # for i in range(12):
    #     if i in [3,7]:
    #         if phone[i] != '-':
    #             return False
    #     elif not phone[i].isalnum():
    #         return False
    # return True

def ip_format_valid(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    return True

def img_format_valid(img):
    # check if format is JPEG/PNG/ whatever perception needs
    return True

def listing_format_valid(listing):
    return True
    # try:
    #     json.loads(listing)
    # except ValueError:
    #     return False
    # return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flag suspicious listings")
    parser.add_argument('--email', type=str, help="Suspicious email")
    parser.add_argument('--phone', type=str, help="Suspicious phone number")
    parser.add_argument('--ip', type=str, help="Suspicious IP")
    parser.add_argument('--address', type=str, help="Suspicious address")
    parser.add_argument('--img', type=str, help="Suspicious image, specify in one of the common image formats")
    parser.add_argument('--listing', type=str, help="Suspicious listing, specify as JSON")
    args = parser.parse_args()

    if email_format_valid(args.email):
        print(api.flag_suspicious_email(args.email))

    if phone_format_valid(args.phone):
        print(api.flag_suspicious_phone(args.phone))

    if ip_format_valid(args.ip):
        print(api.flag_suspicious_ip(args.ip))

    if args.address:
        print(api.flag_suspicious_address(args.address))

    if img_format_valid(args.img):
        api.flag_suspicious_image(args.img)

    if listing_format_valid(args.listing):
        api.flag_suspicious_listing(args.listing)

