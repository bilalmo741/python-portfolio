# usa_baby_names_analysis.py
# Python project: analyze US baby names by frequency and popularity

import csv

print("Welcome to the baby name analyzer!")

analysis = input("What analysis would you like to run (name comparison / maximum popularity)? ").strip().lower()

if analysis == "name comparison":
    analysisfname = input("Enter the first name to compare: ").strip()
    analysissname = input("Enter the second name to compare: ").strip()
    totalfname = 0
    totalsname = 0

    with open("usa_baby_names.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for line in reader:
            name = line[0]
            frequency = int(line[2])
            if name.lower() == analysisfname.lower():
                totalfname += frequency
            elif name.lower() == analysissname.lower():
                totalsname += frequency

    print(f"Total occurrences of {analysisfname}: {totalfname}")
    print(f"Total occurrences of {analysissname}: {totalsname}")

    if totalfname > totalsname:
        print(f"{analysisfname} was more popular.")
    elif totalsname > totalfname:
        print(f"{analysissname} was more popular.")
    else:
        print("The names were equally popular.")

elif analysis == "maximum popularity":
    namesearch = input("Enter a name to find the most popular year: ").strip()
    maxfreq = 0
    maxyear = None

    with open("usa_baby_names.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            name = line[0]
            year = int(line[1])
            frequency = int(line[2])
            if name.lower() == namesearch.lower() and frequency > maxfreq:
                maxfreq = frequency
                maxyear = year

    if maxyear is not None:
        print(f"{namesearch} was most popular in {maxyear} with {maxfreq} occurrences.")
    else:
        print(f"{namesearch} was not found.")

else:
    print("Invalid analysis. Type either 'name comparison' or 'maximum popularity'.")
