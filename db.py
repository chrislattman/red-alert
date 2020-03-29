'''
This file includes actually calling the database 
'''
import csv 

suspicious_phones = []
suspicious_addrs = [] 
suspicious_domains = []
suspicious_emails = []
suspicious_ips = []

with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    line_count = 0
    for row in reader:
        if line_count != 0:
            suspicious_phones.append(row[1])
            suspicious_addrs.append(row[2])
            line_count += 1

with open('us-500.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    line_count = 0
    for row in reader:
        if line_count != 0:
            suspicious_emails.append(row[10])
            suspicious_domains.append(row[10].split('@')[1])
            line_count += 1

with open('ips.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    line_count = 0
    for row in reader:
        if line_count != 0:
            suspicious_ips.append(row[0].split('/')[0])
            line_count += 1


def is_phone_suspicious(phone):
    return phone in suspicious_phones

def is_addr_suspicious(addr):
    return addr in suspicious_addrs

def is_domain_suspicious(domain):
    return domain in suspicious_domains

def is_email_suspicious(email):
    return email in suspicious_emails

def is_ip_suspicious(ip):
    return ip in suspicious_ips
