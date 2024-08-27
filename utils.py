# Copyright 2024 Angie Tran, Diego Cid
#
# This file is part of Beach Buddy.
# Beach Buddy is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published by
# the Free Software Foundation, either version 1 of the License, or
# (at your option) any later version.
#
# Beach Buddy is distributed in the hope that it will be useful,
# but WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# See the MIT License for more details.
#
# You should have received a copy of the MIT License
# along with Beach Buddy. If not, see <https://mit-license.org/>.
"""
File: utils.py
Author: Angie Tran and Diego Cid
Description: Utility file that includes any utility functions and helper functions
"""
from csulb_course import CSULBCourse
import discord
import pandas as pd
import numpy as np
import csv
import os
from datetime import datetime, timezone


def get_time():
    now = datetime.utcnow()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def get_date():
    now = datetime.utcnow()
    current_date = now.strftime("%B %d %Y")
    return current_date


def check_days_last_scrape():
    path_fall = "seasons/fall_2024.csv"
    timestamp_fall = os.path.getmtime(path_fall)
    datestamp = datetime.fromtimestamp(timestamp_fall)
    days_between = datetime.utcnow() - datestamp
    if days_between.days >= 2:
        return True
    return False


def main():
    print(get_date())
    print(get_time())
    print(check_days_last_scrape())


if __name__ == "__main__":
    main()
