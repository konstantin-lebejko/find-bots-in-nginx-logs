import re


def pull_ip(string):
    ip_re = re.search('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', string)
    return ip_re.group(1)
