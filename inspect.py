#!/usr/bin/env python2.7

import webbrowser
import psutils
from time import sleep

# Linux
# chrome_path = '/usr/bin/chromium-browser %s'

# Windows
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
PROC_NAME = 'chrome.exe'

delay=5

with open('data/threats-merged.csv', 'r') as file:
    for line in file:
        # open url
        url = line.partition(';')[0]
        webbrowser.get(chrome_path).open(url)
        # wait for malware download
        sleep(delay)
        # kill processus
        for proc in psutils.process_iter():
            if proc.name == PROC_NAME:
                proc.kill()
