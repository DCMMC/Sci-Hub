from __future__ import print_function
import platform

print()

# Python 2.x incompatibility
if int(platform.python_version_tuple()[0]) < 3:
    print("This script is NOT compatible with Python 2.x")
    print("Use this command to run the script:\n")
    print("python3 test.py\n")
    print("*"*30 + "\n" + "\tTEST FAILED" + "\n" + "*"*30)
    quit()

if platform.system() not in ['Linux', 'Darwin']:
    print("Looks like you are not running on GNU/Linux or a Mac")
    print("If this test is successful then you can run: ")
    print("\npython3 sci_hub.py\n")

# import built in dependencies and check
try:
    import argparse
    import os
    import re
    import sys
    print("Built in modules imported successfully.\n")
except(ImportError):
    print("Error in importing built in dependencies\n")
    print("Make sure os, sys, re, platform, modules can be imported\n")
    print("Try reinstalling python3\n")
    print("*"*30 + "\n" + "\tTEST FAILED" + "\n" + "*"*30)
    quit()

try:
    from bs4 import BeautifulSoup
    import requests
    print("External dependencies successfully imported\n")
except(ImportError):
    print("Error in importing external dependencies.\n")
    print("Run appropriate configuration file.\n")
    print("Make sure bs4 and requests are importable.\n")
    print("*"*30 + "\n" + "\tTEST FAILED" + "\n" + "*"*30)
    quit()

print("*"*30 + "\n" + "\tTEST PASSED" + "\n" + "*"*30)

def main():
    resp = requests.get("https://google.com")
    soup = BeautifulSoup(resp.content, "lxml")
    re.match("fojwe", "orji")
    print(sys.version)
    parser = argparse.ArgumentParser()
    print(parser.parse_args)

main()
