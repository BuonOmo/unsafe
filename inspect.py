#!/usr/bin/env python2.7

from subprocess import Popen
from time import sleep

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

delay=15

with open('data/threats-merged.csv', 'r') as file:
    for line in file:
        # open url
        url = line.partition(';')[0]
        proc = Popen([chrome_path, '--disable-web-security', url]
        # wait for malware download
        sleep(delay)
        # kill browser
        proc.kill()
