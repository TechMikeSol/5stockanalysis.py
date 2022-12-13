# 5stockanalysis.py

IDEAL STOCK API

Ideal stock API allows

Application programming interfaces are a great way to collect valuable information from a server to your computer. In this project we used the website: https://polygon.io/ to request information of stocks from 2021-03-25 to 2022-03-29 and then apply statistical analysis on the weekly closing price of the desire stock.

Tools used for this project: python and matplotlib. Additionally, you will find csv files where the information of the API was collected, saved, and then used for statistical analysis.

Please refer to the following section for more information of this project.

Content

extract.py
In this file you will find the starting code to request information from the API. You will need a "key" (not provided) that can be obtained by creating an account in https://polygon.io/

This information is then stored and properly labled in a csv file with its respective stock ticker (AAPL, MSFT, VOO, GOOG, DIS).

analysis.py
This file retrieves the information stored in the csv file to calculate the weekly standard deviation of each stock (one provided in this example). Additionally, a visualization is provided to better understand the changes of variation of the stock from 2021-03-29 to 2022-05-25

You can also find a multi-graph visual in 5Stocksubplots.png of the analyzed stocks and their standard deviations.
