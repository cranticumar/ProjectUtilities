import argparse
import json
import os
import re
import csv
from collections import OrderedDict

argParser = argparse.ArgumentParser()

argParser.add_argument('-f', '--folder', dest='folder',
                       help='root folder of all test case folders', required=True)
cmdargs = argParser.parse_args()

cam0dict = dict()
cam1dict = dict()

for (r, d, f) in os.walk(cmdargs.folder):
    for eachjson in f:
        if os.path.splitext(eachjson)[1] == '.json':
            with open(os.path.join(r, eachjson), 'r') as jsonFh:
                raw_metrics = jsonFh.read()
                tc = re.sub(
                    '[A-Z]', lambda match: '_' + match.group(0).lower(), r.split('\\')[-2])
                if not tc in cam1dict:
                    cam0dict[tc] = dict()
                    cam1dict[tc] = dict()
                sepCameraIdData = raw_metrics.split(tc + '":')
                sepCameraIdData = [
                    json.JSONDecoder(object_pairs_hook=OrderedDict).decode(
                        sepCameraIdData[1][:-2]),
                    json.JSONDecoder(object_pairs_hook=OrderedDict).decode(sepCameraIdData[2].split('}')[0] + '}')]
                for cameraData in sepCameraIdData:
                    for k, v in cameraData.iteritems():
                        if k != 'camera_id':
                            if type(v) is list:
                                while len(v) < 6:
                                    v.append(0)
                                if tc in ['test_reprocessing_capture_stall', 'test_reprocessing_latency', 'test_reprocessing_throughput']:
                                    k = k + cameraData['reprocess_type']
                                if tc in ['test_reprocessing_latency', 'test_reprocessing_throughput']:
                                    k = k + cameraData['capture_message']

                                if cameraData['camera_id'] == '0':
                                    if k not in cam0dict[tc]:
                                        cam0dict[tc][k] = v
                                    else:
                                        cam0dict[tc][k] = cam0dict[tc][k] + v
                                elif cameraData['camera_id'] == '1':
                                    if k not in cam1dict[tc]:
                                        cam1dict[tc][k] = v
                                    else:
                                        cam1dict[tc][k] = cam1dict[tc][k] + v

cam0csv = open(os.path.join('CTSKPI_0.csv'), 'wb')
cam1csv = open(os.path.join('CTSKPI_1.csv'), 'wb')
cam0writer = csv.writer(cam0csv)
cam1writer = csv.writer(cam1csv)

for testsuite, tcaseObj in cam0dict.iteritems():
    for tcase, metrics in tcaseObj.iteritems():
        cam0writer.writerow([testsuite, tcase] + metrics)

for testsuite, tcaseObj in cam1dict.iteritems():
    for tcase, metrics in tcaseObj.iteritems():
        cam1writer.writerow([testsuite, tcase] + metrics)

cam0csv.close()
cam1csv.close()
