'''
This file includes actually calling the database 
'''
import csv 
import os
import glob
import zipfile
import urllib.request

import pandas as pd

from perception import tools, hashers

suspicious_phones = []
suspicious_addrs = [] 
suspicious_domains = []
suspicious_emails = []
suspicious_ips = []

with open('merged.csv', newline='') as csvfile:
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

'''
# This URL doesn't work hence commented

urllib.request.urlretrieve(
    "https://thorn-perception.s3.amazonaws.com/thorn-perceptual-deduplication-example.zip",
    "thorn-perceptual-deduplication-example.zip"
)

with zipfile.ZipFile('thorn-perceptual-deduplication-example.zip') as f:
    f.extractall('.')

filepaths = glob.glob('thorn-perceptual-deduplication-example/*.jpg')
'''


# Now we can do whatever we want with the duplicates. We could just delete
# the first entry in each pair or manually verify the pairs to ensure they
# are, in fact duplicates.


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

def is_img_suspicious(img):
    return True
    # duplicate_pairs = tools.deduplicate(files=filepaths, hashers=[(hashers.PHash(hash_size=16), 0.2)])
    # print(duplicate_pairs)