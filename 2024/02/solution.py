#!/usr/bin/env python3
import re


def is_unsafe_report(x, y):
    if x == y:
        return True


def is_increasing(l):
    increasing = None
    errors = 0
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            if (l[i + 1] - l[i]) <= 3 and (increasing is None or increasing):
                increasing = True
            else:
                errors += 1
            continue
        if l[i] > l[i + 1]:
            if (l[i] - l[i + 1]) <= 3 and (increasing is None or not increasing):
                increasing = False
            else:
                errors += 1
            continue
        if l[i] == l[i + 1]:
            errors += 1
    return errors


fname = "input.txt"
fhandle = open(fname)
allow_error = True

d_report = {"safe": [], "unsafe": []}
for line in fhandle:
    clean_line = line.rstrip()
    report = re.findall("[0-9]+", clean_line)
    report = [int(x) for x in report]
    if allow_error:
        for j in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(j)
            if is_increasing(report_copy) == 0:
                d_report["safe"].append(report)
                break
    else:
        if is_increasing(report) == 0:
            d_report["safe"].append(report)


print(len(d_report["safe"]))
