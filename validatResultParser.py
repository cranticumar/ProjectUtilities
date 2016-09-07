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

results = list()

for testcase in os.listdir(directory):
    testresultsdir = os.path.join(directory, testcase, 'TestResults')
    if not os.path.exists(testresultsdir):
        results.append([testcase, 'Malfunctioned'])
    else:
        resFile = os.path.join(testresultsdir, 'Results.txt')
        with open(resFile, 'rb') as resHandle:
            result = re.search('\[(\w+)\]', resHandle.readlines()[1]).group(1)
            results.append([testcase, result])

pp.pprint(results)

with open(os.path.join(directory, 'results.csv'), 'wb') as csvfile:
    w = csv.writer(csvfile)
    for res in results:
        w.writerow(res)
