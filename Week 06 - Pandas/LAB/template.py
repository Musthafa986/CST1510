"""
RECORD CHECK  -  my version
===========================

Name  :  Musthafa
Lane  :  IT
Date  :  08/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv(r"C:\Users\mmt31\OneDrive\Desktop\MDX\CST1510\Week 6\Week 06 - Pandas\Week 06 - Pandas\LAB\servers_template.csv")   # replace with pd.read_csv("your_file.csv")

# ================================================================= PROCESS
df["percent"] = (df["used"] / df["total"]) * 100
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["status"] = df["percent"].apply(lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK")

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print("All servers:")
print(df)

print("\nServers that are not OK:")
print(df[df["status"] != "OK"])

counts = df.groupby("status").size()
print("\nCount per status:")
print(counts)

df.to_csv(r"C:\Users\mmt31\OneDrive\Desktop\MDX\CST1510\Week 6\Week 06 - Pandas\Week 06 - Pandas\LAB\servers_template.csv", index=False)

counts.plot(kind="bar")
plt.title("Servers per Status")
plt.xlabel("Status")
plt.ylabel("Number of Servers")
plt.xticks(rotation=0)
plt.savefig("status_counts.png")
plt.close()

# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
