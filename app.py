import argparse
import api

def email_format_valid(email):
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flag suspicious listings")
    parser.add_argument('--email', type=str, help="Suspicious email")
    parser.add_argument('--phone', type=str, help="Suspicious phone number")
    parser.add_argument('--address', type=str, help="Suspicious address")
    parser.add_argument('--image', type=str, help="Suspicious image, specify in one of the common image formats")
    parser.add_argument('--listing', type=str, help="Suspicious listing, specify as JSON")
    args = parser.parse_args()

    if email_format_valid(args.email):
        api.flag_suspicious_email(args.email)

    # do similar calls for others
    # photo and listing will need libraries

