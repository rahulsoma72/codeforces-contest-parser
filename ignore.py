
import os
import sys
import requests
import re
from bs4 import BeautifulSoup
import shutil
import time

page = requests.get("https://rahulsoma72.github.io")
print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
