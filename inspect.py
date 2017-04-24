#!/usr/bin/env python2.7
from __future__ import print_function
from collections import defaultdict
from subprocess import Popen
from time import sleep
import sys

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
log_file = open('log', 'w')


def log(message):
    print(message)
    print(message, file=log_file)

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

delay = 60

c = defaultdict(int)
count = 0
with open('data/threats-merged.csv', 'r') as file:
    lines = file.readlines()
    for line_group in chunks(lines, 6):
        try:
            # open url
            proc_list = []
            for line in line_group:
                url = line.split(';')[0]
                threat_type = line.split(';')[1]
                if c[url] > 0 or threat_type == 'SOCIAL_ENGINEERING':
                    continue
                c[url] += 1
                count += 1
                log("{}: {}".format(count, url))
                proc_list.append(Popen([chrome_path, '--disable-web-security', url]))
            # wait for malware download
            sleep(delay)
            # kill browser
            for proc in proc_list:
                proc.kill()
        except Exception as e:
            print(e, file=sys.stderr)
