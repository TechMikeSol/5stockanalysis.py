import statistics as stats
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure as fig
import csv


# AAPL DATA CALCULATION

# Load CSV file
AAPL_data = []
with open ("AAPL.csv", "r") as infile:
    reader = csv.DictReader(infile)
    # Save the dictReader object into a list of dictionaries for analysis
    for row in reader:
        AAPL_data.append(row)
print(AAPL_data)

# Start at first row in dictionary using i = 0
i = 0
# Create empty list to save MSFT Standard Deviations in
AAPL_stdev_data = []
while i < len(AAPL_data):
    # If any day I'm getting is greater than the dataset, break
    if i + 1 >= len(AAPL_data) or i + 2 >= len(AAPL_data) or i + 3 >= len(AAPL_data) or i + 4 >= len(AAPL_data):
        break
        # Get days 1-5
    Day1 = float(AAPL_data[i]["Closing_price"])
    Day2 = float(AAPL_data[i+1]["Closing_price"])
    Day3 = float(AAPL_data[i+2]["Closing_price"])
    Day4 = float(AAPL_data[i+3]["Closing_price"])
    Day5 = float(AAPL_data[i+4]["Closing_price"])

    # Analyze pop st dev for all
    pop_stdev = stats.pstdev([Day1,Day2,Day3,Day4,Day5])
    AAPL_stdev_data.append(pop_stdev)
    i += 5
#print(AAPL_stdev_data)

week_num = 0
#print(AAPL_data)
for stdev in AAPL_stdev_data:
        week_num += 1
        print(f"AAPL Week {week_num} Standard deviation is {stdev}")

# VOO DATA CALCULATION

VOO_data = []
with open ("VOO.csv", "r") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        VOO_data.append(row)
print(VOO_data)
i = 0


VOO_stdev_data = []
while i < len(VOO_data):
    if i + 1 >= len(VOO_data) or i + 2 >= len(VOO_data) or i + 3 >= len(VOO_data) or i + 4 >= len(VOO_data):
        break
        # Get days 1-5
    Day1 = float(VOO_data[i]["Closing_price"])
    Day2 = float(VOO_data[i+1]["Closing_price"])
    Day3 = float(VOO_data[i+2]["Closing_price"])
    Day4 = float(VOO_data[i+3]["Closing_price"])
    Day5 = float(VOO_data[i+4]["Closing_price"])

    # Analyze pop st dev for all
    pop_stdev = stats.pstdev([Day1,Day2,Day3,Day4,Day5])
    VOO_stdev_data.append(pop_stdev)
    i += 5
#print(VOO_stdev_data)

week_num = 0
#print(VOO_data)
for stdev in VOO_stdev_data:
        week_num += 1
        print(f"VOO Week {week_num} Standard deviation is {stdev}")


# GOOG DATA CALCULATION

GOOG_data = []
with open ("GOOG.csv", "r") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        GOOG_data.append(row)
print(GOOG_data)
i = 0


GOOG_stdev_data = []
while i < len(GOOG_data):
    if i + 1 >= len(GOOG_data) or i + 2 >= len(GOOG_data) or i + 3 >= len(GOOG_data) or i + 4 >= len(GOOG_data):
        break
        # Get days 1-5
    Day1 = float(GOOG_data[i]["Closing_price"])
    Day2 = float(GOOG_data[i+1]["Closing_price"])
    Day3 = float(GOOG_data[i+2]["Closing_price"])
    Day4 = float(GOOG_data[i+3]["Closing_price"])
    Day5 = float(GOOG_data[i+4]["Closing_price"])

    # Analyze pop st dev for all
    pop_stdev = stats.pstdev([Day1,Day2,Day3,Day4,Day5])
    GOOG_stdev_data.append(pop_stdev)
    i += 5
#print(GOOG_stdev_data)

week_num = 0
#print(GOOG_data)
for stdev in GOOG_stdev_data:
        week_num += 1
        print(f"VOO Week {week_num} Standard deviation is {stdev}")

# DIS DATA CALCULATION

DIS_data = []
with open ("DIS.csv", "r") as infile:
    reader = csv.DictReader(infile)
    # Save this dictReader object into a list of dictionaries for analysis
    for row in reader:
        DIS_data.append(row)
print(DIS_data)

# Start at first row in dictionary using i = 0
i = 0
DIS_stdev_data = []
while i < len(DIS_data):
    if i + 1 >= len(DIS_data) or i + 2 >= len(DIS_data) or i + 3 >= len(DIS_data) or i + 4 >= len(DIS_data):
        break
        # Get days 1-5
    Day1 = float(DIS_data[i]["Closing_price"])
    Day2 = float(DIS_data[i+1]["Closing_price"])
    Day3 = float(DIS_data[i+2]["Closing_price"])
    Day4 = float(DIS_data[i+3]["Closing_price"])
    Day5 = float(DIS_data[i+4]["Closing_price"])

    # Analyze pop st dev for all
    pop_stdev = stats.pstdev([Day1,Day2,Day3,Day4,Day5])
    DIS_stdev_data.append(pop_stdev)
    i += 5
#print(DIS_stdev_data)

week_num = 0
#print(DIS_data)
for stdev in DIS_stdev_data:
        week_num += 1
        print(f"VOO Week {week_num} Standard deviation is {stdev}")

# MSFT DATA CALCULATION

# Load CSV file
MSFT_data = []
with open ("VOO.csv", "r") as infile:
    reader = csv.DictReader(infile)
    # Save the dictReader object into a list of dictionaries for analysis
    for row in reader:
        MSFT_data.append(row)
print(MSFT_data)

# Start at first row in dictionary using i = 0
i = 0
# Create empty list to save MSFT Standard Deviations in
MSFT_stdev_data = []
while i < len(MSFT_data):
    # If any day I'm getting is greater than the dataset, break
    if i + 1 >= len(MSFT_data) or i + 2 >= len(MSFT_data) or i + 3 >= len(MSFT_data) or i + 4 >= len(MSFT_data):
        break
        # Get days 1-5, typecast data to floats, 
    Day1 = float(MSFT_data[i]["Closing_price"])
    Day2 = float(MSFT_data[i+1]["Closing_price"])
    Day3 = float(MSFT_data[i+2]["Closing_price"])
    Day4 = float(MSFT_data[i+3]["Closing_price"])
    Day5 = float(MSFT_data[i+4]["Closing_price"])

    # Analyze pop st dev for all closing prices and save to MSFT_stdev_data list 
    pop_stdev = stats.pstdev([Day1,Day2,Day3,Day4,Day5])
    MSFT_stdev_data.append(pop_stdev)
    # Increment up to 5 days to skip to 5 days
    i += 5
#print(MSFT_stdev_data)

week_num = 0
#print(MSFT_data)
# Get each week and increment by 1
for stdev in MSFT_stdev_data:
        week_num += 1
        print(f"MSFT Week {week_num} Standard deviation is {stdev}")

# Plot data using matplot as plt
#fig(figsize = (10,10), dpi=100)


fig,(ax1, ax2, ax3, ax4, ax5,) = plt.subplots(1,5, sharey = True, sharex = True)
fig.suptitle("5 Stock Standard Deviation", fontsize = "15")

ax1.plot(AAPL_stdev_data, label = "AAPL", color = "blue")
ax2.plot(MSFT_stdev_data, label = "MSFT", color = "black")
ax3.plot(VOO_stdev_data, label = "VOO", color = "red")
ax4.plot(GOOG_stdev_data, label = "GOOG", color = "green")
ax5.plot(DIS_stdev_data, label = "DIS", color = "purple")
fig.text(0.5, 0.04, 'Week', ha = 'center', fontsize = "15")
fig.text(0.04, 0.5, 'Standard Deviation', va = 'center', rotation = 'vertical', fontsize = "15")
#plt.ylabel("Standard Deviation")
fig.legend()
plt.show()
#plt.savefig("5stocks.png")    