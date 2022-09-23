#!/usr/bin/python3
"""fetches from a url, displays its content"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        if response.readable():
            data = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(data)))
            print("\t- content: {}".format(data))
            print("\t- utf8 content: {}".format(data.decode("utf-8")))
