import sys
import urllib.request

fh = urllib.request.urlopen("https://www.bankofcanada.ca/valet/observations/group/FX_RATES_DAILY/csv?start_date=2022-01-14")
dict = {}

def get_text(start_text, end_text):
    text = ""
    found_flag = False
    for line in fh:
        string = line.decode()
        if string == "\n":
            continue
        if found_flag :
            text = text + string
        if string.find(start_text) != -1:
            found_flag = True
        if string.find(end_text) != -1:
            break
    return text

SERIES = get_text(start_text="id", end_text="OBSERVATIONS")
print(SERIES)
SERIES = SERIES.replace('"', "")
SERIES = SERIES.split("\n")
for itr in SERIES:
    itr = itr.split(",")
    if itr[0] == "OBSERVATIONS":
        break
    dict[itr[0]] = {"label": itr[1], "description": itr[2]}

print(dict)