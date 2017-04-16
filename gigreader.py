# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import requests
import sys
import re


class GigReader:

    def __init__(self, ip="192.168.0.1"):
        self.router_web = "http://" + ip
        self.cookie = self.get_cookie()
        self.limit = self.get_limit()
        self.usage = 0

    def get_cookie(self):
        try:
            response = requests.get(self.router_web + "/html/home.html")
            return response.headers['Set-Cookie']
        except requests.exceptions.ConnectionError, e:
            sys.stdout.write(repr(e.message)+"\r\n")
            sys.exit(0)

    def get_limit(self):
        headers = {"Content-Type": "text/html", "Cookie": self.cookie}
        response = requests.get(self.router_web + "/api/monitoring/start_date", headers=headers)
        xml_string = response.text

        if "error" in xml_string:
            return -1

        else:
            root = ET.fromstring(xml_string)
            return float(re.findall(r'\d+', root[1].text)[0])

    def update_usage(self):
        headers = {"Content-Type": "text/html", "Cookie": self.cookie}
        response = requests.get(self.router_web + "/api/monitoring/month_statistics", headers=headers)
        xml_string = response.text

        if "error" in xml_string:
            self.usage = -1

        else:
            root = ET.fromstring(xml_string)
            total = int(root[0].text) + int(root[1].text)
            gibibyte = (total * 0.93132257461548) / 1000000000
            self.usage = round(gibibyte, 2)

    def print_progress(self):
        limit = round(self.limit, 2)
        bar_len = 60
        filled_len = int(round(bar_len * self.usage / float(limit)))

        bar = '█' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s %s / %s %s\r' % (bar, self.usage, 'GB', limit, 'GB'))
        sys.stdout.flush()
