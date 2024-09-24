import datetime
import sys
import os
from collections import defaultdict

dt = datetime.datetime.strptime(sys.argv[1], '%Y-%m-%d')
dir_name = os.path.join(os.getcwd(), "input")
dict_email = defaultdict(lambda: defaultdict(int))

for i in range(1, 8):
    current_dt = dt - datetime.timedelta(days=i)
    with open(os.path.join(dir_name, f"{current_dt.strftime('%Y-%m-%d')}.csv"), 'r') as f:
        for line in f.readlines():
            arr_line = line.split(sep=',')
            if len(arr_line) == 3:
                email, action, action_dt = arr_line
                dict_email[email][action] += 1

filepath = os.path.join(os.getcwd(), "output")
if not os.path.exists(filepath):
    os.makedirs(filepath)
filepath = os.path.join(filepath, f"{dt.strftime('%Y-%m-%d')}.csv")

with open(filepath, "w") as out:
    for ind, email in enumerate(dict_email.keys()):
        if ind != 0:
            out.write("\n")
        line = f"{email},{dict_email[email]['CREATE']},{dict_email[email]['READ']},{dict_email[email]['UPDATE']},{dict_email[email]['DELETE']}"
        out.write(line)


