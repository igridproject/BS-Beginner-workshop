#!/usr/bin/python
import requests
import json
import time

print("\nExample Python Programming with BigStream Storage API")

# Define BigStream Storage API
bs_url = "http://demo.bs.igridproject.info/api/"

def printLine():
    bar = "--- ----------------------------------------- ---"
    print(bar)

# Get stroage list
res = requests.get(bs_url+"storage")
if res.status_code != 200:
    print("Error status code "+str(res.status_code))
    exit(1)
res.encoding = "utf-8"
output = res.json()
print("*** List BigStream Storage")
print("GET "+bs_url)
print("Result:")
printLine()
print(json.dumps(output,indent=4, sort_keys=True))
printLine()
output = output[:3]

# Get storage stats
print("\n*** Storage Information (show only first 3)")
for i in output:
    full_url = bs_url+"storage/"+i+"/stats"
    print("\nGET "+full_url)
    print("Result:")
    printLine()
    res = requests.get(full_url)
    if res.status_code != 200:
        print("Error cannot get "+full_url)
    storage_stat = res.json()
    print(json.dumps(storage_stat,indent=4, sort_keys=True))
    printLine()

# Get 1st last Data record each storage
print("\n*** Get 1st record of each storage (show only first 3)")
for i in output:
    full_url = bs_url+"storage/"+i+"/objects?limit=1"
    print("\nGET "+full_url)
    printLine()
    res = requests.get(full_url)
    if res.status_code != 200:
        print("Error cannot get "+full_url)
    # GET /<storage>/objects always return array of object
    array = res.json()
    data = array[0]
    # If too big size Show only meta
    if len(res.content) > 2000:
        print("Data too big for print in console")
        print(json.dumps(data["meta"],indent=4, sort_keys=True))
    else:
        print(json.dumps(data,indent=4, sort_keys=True))
    printLine()

# Get Access Data record each storage
print("\n*** Access last record of each storage (show only first 3)")
for i in output:
    full_url = bs_url+"object/"+i
    print("\nGET "+full_url)
    printLine()
    res = requests.get(full_url)
    if res.status_code != 200:
        print("Error cannot get "+full_url)
    # GET /<storage>/objects always return array of object
    data = res.json()

    # If too big size Show only meta
    if len(res.content) > 10000:
        print("Data too big for print in console")
        print(json.dumps(data["meta"],indent=4, sort_keys=True))
    else:
        print(json.dumps(data,indent=4, sort_keys=True))
    printLine()