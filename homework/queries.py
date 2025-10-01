"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

import os
import csv
from collections import defaultdict


def create_output_directory(query_name):
    """Create output directory for a query"""
    output_dir = f"files/{query_name}/"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir


def write_output_files(output_dir, results):
    """Write results to output files"""
    # Write the main results to part-00000
    with open(os.path.join(output_dir, "part-00000"), "w", encoding="utf-8") as f:
        for result in results:
            f.write(f"{result}\n")
    
    # Create _SUCCESS file to indicate successful completion
    with open(os.path.join(output_dir, "_SUCCESS"), "w", encoding="utf-8") as f:
        pass


def read_tips_data():
    """Read the tips dataset"""
    data = []
    with open("files/input/tips.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def query_1():
    """Query 1: Total bill amount by day"""
    data = read_tips_data()
    day_totals = defaultdict(float)
    
    for row in data:
        day = row['day']
        total_bill = float(row['total_bill'])
        day_totals[day] += total_bill
    
    results = []
    for day, total in sorted(day_totals.items()):
        results.append(f"{day}\t{total:.2f}")
    
    output_dir = create_output_directory("query_1")
    write_output_files(output_dir, results)


def query_2():
    """Query 2: Average tip by sex"""
    data = read_tips_data()
    sex_tips = defaultdict(list)
    
    for row in data:
        sex = row['sex']
        tip = float(row['tip'])
        sex_tips[sex].append(tip)
    
    results = []
    for sex, tips in sorted(sex_tips.items()):
        avg_tip = sum(tips) / len(tips)
        results.append(f"{sex}\t{avg_tip:.2f}")
    
    output_dir = create_output_directory("query_2")
    write_output_files(output_dir, results)


def query_3():
    """Query 3: Count of meals by smoker status"""
    data = read_tips_data()
    smoker_counts = defaultdict(int)
    
    for row in data:
        smoker = row['smoker']
        smoker_counts[smoker] += 1
    
    results = []
    for smoker, count in sorted(smoker_counts.items()):
        results.append(f"{smoker}\t{count}")
    
    output_dir = create_output_directory("query_3")
    write_output_files(output_dir, results)


def query_4():
    """Query 4: Average total bill by time"""
    data = read_tips_data()
    time_bills = defaultdict(list)
    
    for row in data:
        time = row['time']
        total_bill = float(row['total_bill'])
        time_bills[time].append(total_bill)
    
    results = []
    for time, bills in sorted(time_bills.items()):
        avg_bill = sum(bills) / len(bills)
        results.append(f"{time}\t{avg_bill:.2f}")
    
    output_dir = create_output_directory("query_4")
    write_output_files(output_dir, results)


def query_5():
    """Query 5: Maximum tip by party size"""
    data = read_tips_data()
    size_tips = defaultdict(list)
    
    for row in data:
        size = int(row['size'])
        tip = float(row['tip'])
        size_tips[size].append(tip)
    
    results = []
    for size, tips in sorted(size_tips.items()):
        max_tip = max(tips)
        results.append(f"{size}\t{max_tip:.2f}")
    
    output_dir = create_output_directory("query_5")
    write_output_files(output_dir, results)


#
# ORQUESTADOR:
#
def run():
    """Orquestador"""
    query_1()
    query_2()
    query_3()
    query_4()
    query_5()


if __name__ == "__main__":

    run()
