"""
RECORD CHECK  -  my version
===========================

Name  :  Musthafa
Lane  :  IT
Date  :  18/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """Returns the dufference, percentage used and status for one record"""
    difference = limit - value
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """Prints the report for one record"""
    print(f"{label}: {value} of {limit} GB used"
          f"({percent:.1f}%, {difference:+.1f} GB from limit) = {status}")

def load_records(path):
    """Reads the label, value, limit lines from a file and returns a lists of dicts"""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records

def write_results(path, results):
    """Writes one label, status line per result to a file"""
    with open(path, "w") as f:
        for label, status in results:
            f.write(F"{label},{status}\n")

# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

with open("my_records.txt", "w") as f:
    f.write("srv-01,87,120\n")
    f.write("srv-02,141,256\n")
    f.write("srv-03,45,64\n")
    
try:
    records = load_records("my_records.txt")
except FileNotFoundError:
    print(f"Data file not found: {"my_records.txt"} - starting with no records")
    records = []

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

results = []
over_count = 0

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    results.append((record["label"], status))
    if status == "OVER LIMIT":
        over_count += 1

write_results("my_results.txt", results)
print(f"\nOVER LIMIT: {over_count} of {len(records)} records")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
