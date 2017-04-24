#!/usr/bin/env python2.7
from __future__ import print_function
from collections import defaultdict
from subprocess import Popen
from time import sleep
import sys

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
log_file = open('log','w')


def log(message):
    print(message)
    print(message, file=log_file)


start_at = 1
delay = 15

c = defaultdict(int)
count = 0
with open('data/threats-merged.csv', 'r') as file:
    for line in file:
        try:
            # open url
            url = line.split(';')[0]
            threat_type = line.split(';')[1]
            if c[url] > 0 or threat_type == 'SOCIAL_ENGINEERING':
                continue
            c[url] += 1
            count += 1
            if count < start_at:
                continue
            log("{}: {}".format(count, url))
            proc = Popen([chrome_path, '--disable-web-security', url])
            # wait for malware download
            sleep(delay)
            # kill browser
            proc.kill()
        except Exception as e:
            print(e, file=sys.stderr)
