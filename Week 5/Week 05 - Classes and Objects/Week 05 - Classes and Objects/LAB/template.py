"""
RECORD CHECK  -  my version
===========================

Name  :  Musthafa
Lane  :  IT
Date  :  24/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS
# 1. Define a class called Record.
#
#    Threshold : __init__(self, label, value, limit) storing all three as
#                attributes. No methods yet.
#    Typical   : add a method status(self) that returns "OVER LIMIT" (100%+),
#                "WARNING" (90%+) or "OK", worked out from self.value and
#                self.limit. Give it a one-line docstring.
#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

class Record:
    """One server: the hostname, GB used and GB total."""

    def __init__(self, label, value, limit):
        """Store the hostname, GB used and GB total on this object."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return how full this server is, as a percentage of its total."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT if 100 or more, WARNING if 90 or more, or OK"""
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
# 2. Create your records.
#
#    Threshold : create at least 2 Record instances directly in the code.
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.

records = [
    Record("srv-01", 87.0, 100.0),
    Record("srv-02", 120.0, 100.0),
    Record("srv-03", 45.0, 100.0),
]


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

over_limit_count = 0

for record in records:
    result = record.status()

    if result == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  Musthafa")
    print("=" * 34)
    print(f"  {'Hostname':<10} : {record.label:>10}")
    print(f"  {'GB used':<10} : {record.value:>10}")
    print(f"  {'GB total':<10} : {record.limit:>10}")
    print(f"  {'Percentage':<10} : {record.percent():>10.1f}%")
    print(f"  {'Status':<10} : {result:>10}")
    print("=" * 34)

print()
print(f"{over_limit_count} of {len(records)} records are OVER LIMIT")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
