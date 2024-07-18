#!/usr/bin/python3
"""
Task zero
"""
import sys
from datetime import date, time
import re


def validateLine(line):

    valid = re.compile(
            r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
            r'\[[^\]]+\] "GET /projects/260 HTTP/1.1" \d{3} \d+')
    if valid.match(line):
        e_time = line.split('[')[1].split(']')[0]
        e_date = e_time.split()[0]
        e_time = e_time.split()[1]
        try:
            if ((isinstance(date.fromisoformat(e_date), date)) and
                    (isinstance(time.fromisoformat(e_time), time))):
                return True
        except ValueError:
            return False


count = size = 0
status_num = {}
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
try:
    for line in sys.stdin:
        count += 1
        tokens = line.split()
        if validateLine(line):
            if len(tokens) > 7:
                try:
                    status = int(tokens[7])
                except ValueError:
                    status = None
                size += int(tokens[8])

            if status is not None:
                if str(status) in status_num:
                    status_num[str(status)] += 1
                else:
                    status_num[str(status)] = 1
        else:
            if len(tokens) >= 2:
                tmp_status = tokens[len(tokens) - 2]
                if tmp_status in status_codes:
                    if tmp_status in status_num:
                        status_num[tmp_status] += 1
                    else:
                        status_num[tmp_status] = 1
            try:
                tmp_size = int(tokens[len(tokens) - 1])
                size += tmp_size
            except ValueError:
                pass
        if count == 10:
            print('File size: {}'.format(size))
            for status in status_codes:
                if status in status_num:
                    print('{}: {}'.format(status,
                                          status_num[str(status)]))
            count = 0
    print('File size: {}'.format(size))
    for status in status_codes:
        if status in status_num:
            print('{}: {}'.format(status, status_num[str(status)]))
except KeyboardInterrupt as e:
    print('File size: {}'.format(size))
    print(e)
