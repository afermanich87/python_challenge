## python_challenge

This assignment uses your acquired python skills to analyze two different sets of data, PyBank and PyPoll.

## Prep Work

Before you start:

* Create a new repository (e.g.- one that did not previously exist) for this project called `python_challenge`.

* Clone the new repository to your computer.

* Inside your local git repository, create a directory for each Python challenge: **PyBank** and  **PyPoll**.

* Inside of each folder that you just created, add the following:

  * A new file called `main.py`. This will be the main script to run for each analysis.
  * A `Resources` folder that contains the CSV files you used with the correct path to each. 
    * Named respectively `Resources_bank` and `Resources_poll` for the corresponding challenge.
  * An `Analysis` folder that contains your text file that has the results from your analysis.
    * Named respectively `Analysis_bank` and `Analysis_poll` for the corresponding challenge.

* Push these changes to GitHub.

## PyBank Instructions

In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will use a set of financial data called [budget_data.csv](PyBank/Resources_bank/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses".

Create a Python script that analyzes the budget records to calculate each of the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

* Print the analysis to the terminal

* Export a text file with the final results to your `Analysis_bank` folder

Your analysis should look similar to the following:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```
  

## PyPoll Instructions

In this challenge, you are tasked with helping a small town modernize its vote counting process.

You will use a set of poll data called [election_data.csv](PyPoll/Resources_poll/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 

Create a Python script that analyzes the voting and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote

* Print the analysis to the terminal

* Export a text file with the final results to your `Analysis_poll` folder


Your analysis should look similar to the following:


  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  ```

## Final Tips

* Commit your work and back it up with pushes to GitHub.
* Add a detailed `README.md` file to your repository.


- - -

© 2022 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
