"""
import time
from time import strftime
while True:
    print(strftime("%m/%d/%Y %H:%M:%S"),flush=True)
    print("\r",flush=True)
    time.sleep(1)
"""

from datetime import datetime
import os
temp=datetime.now().strftime("%S")
while True:
    date1=datetime.now()
    formatted=date1.strftime('%Y-%m-%d %H:%M:%S')
    if int(date1.strftime("%S"))==(int(temp)+1)%60:
        print(formatted)
        temp=date1.strftime("%S")