from playwright.sync_api import Playwright, sync_playwright, expect
import os
import json
import csv

def get_user_list():
    file = open("users.csv")
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)

    rows = []

    for row in csvreader:
        rows.append(row)

    instructor = row[0][0]

    students = []

    for col in range(1, len(rows)):
        user = rows[col][0]
        students.append(user)

    final_string = "\n".join(students)
    return final_string

def get_instructor_credentials():
    file = open("users.csv")
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)

    rows = []

    for row in csvreader:
        rows.append(row)

    instructor_id = rows[0][0]
    instructor_pass = rows[0][4]

    return instructor_id, instructor_pass

