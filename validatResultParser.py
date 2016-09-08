import argparse
import os
import pprint
import re
import csv

argParser = argparse.ArgumentParser()
pp = pprint.PrettyPrinter(indent=4)
argParser.add_argument('-d', '--dir', dest='directory', required=True,
                       help='Parent directory for all results.txt files')
args = argParser.parse_args()
directory = args.directory

results = dict()

if os.path.exists('results.csv'):
    with open('results.csv', 'rb') as csvfiler:
        r = csv.reader(csvfiler)
        for row in r:
            results[row[1]] = [row[2], row[0]]

for testcase in os.listdir(directory):
    testresultsdir = os.path.join(directory, testcase, 'TestResults')

    if not os.path.exists(testresultsdir) and testcase not in results.keys():
        results[testcase] = ['Malfunctioned', directory]
    else:
        if not os.path.exists(testresultsdir):
            results[testcase] = ['Malfunctioned', directory]
        else:
            resFile = os.path.join(testresultsdir, 'Results.txt')
            with open(resFile, 'rb') as resHandle:
                result = re.search('\[(\w+)\]', resHandle.readlines()[1]).group(1)
                results[testcase] = [result, directory]

# pp.pprint(results)

with open('results.csv', 'wb') as csvfilew:
    w = csv.writer(csvfilew)
    for key, value in results.items():
        w.writerow([key] + value)
