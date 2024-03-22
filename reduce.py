#!/usr/bin/env python

import sys

current_date = None
normal_count = 0
error_count = 0

for line in sys.stdin:
    date, log_type, count = line.strip().split("\t")
    
    if current_date == date:
        if log_type == "normal":
            normal_count += int(count)
        elif log_type == "error":
            error_count += int(count)
    else:
        if current_date is not None:
            print(current_date + "\tnormal\t" + str(normal_count))
            print(current_date + "\terror\t" + str(error_count))
        current_date = date
        normal_count = 0
        error_count = 0
        if log_type == "normal":
            normal_count += int(count)
        elif log_type == "error":
            error_count += int(count)

if current_date is not None:
    print(current_date + "\tnormal\t" + str(normal_count))
    print(current_date + "\terror\t" + str(error_count))
