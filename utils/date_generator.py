#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      lifel
#
# Created:     01/04/2024
# Copyright:   (c) lifel 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime

def get_time_now():
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%YT%H:%M")
    return dt_string

def get_date_future():
    """This functions returns adds ten days
    to the current date"""
    now = datetime.datetime.now()
    new_now = now + datetime.timedelta(days = 10)
    dt_string = new_now.strftime("%d/%m/%YT%H:%M")
    return dt_string

def get_date_past():
    """This functions returns adds ten days
    to the current date"""
    now = datetime.datetime.now()
    new_now = now - datetime.timedelta(days = 10)
    dt_string = new_now.strftime("%d/%m/%YT%H:%M")
    return dt_string


