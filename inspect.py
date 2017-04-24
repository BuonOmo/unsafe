#!/usr/bin/env python2.7

from collections import defaultdict
from subprocess import Popen
from time import sleep

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

delay=15

c = defaultdict(int)
count = 0
with open('data/threats-merged.csv', 'r') as file:
    for line in file:
        # open url
        url = line.split(';')[0]
        threat_type = line.split(';')[1]
        if c[url] > 0 or threat_type == 'SOCIAL_ENGINEERING':
            continue
        c[url] += 1
        count += 1
        print "%d: %s".format(count, url)
        proc = Popen([chrome_path, '--disable-web-security', url]
        # wait for malware download
        sleep(delay)
        # kill browser
        proc.kill()
