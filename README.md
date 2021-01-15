# Election_Analysis
Analyzing the US Congressional Election in CO using Python

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:

- There were 369,711 votes case in the election.

- The candidates were:
   - Charles Casper Stockham
   - Diana DeGette
   - Raymon Anthony Doane

 - The candidate results were:
   - Charles Casper Stockham received 23.0% of the votes and 85,213 total votes.
   - Diana DeGette received 73.8% of the votes and 272,892 total votes.
   - Raymon Anthony Doane received 3.1% of the votes and 11,606 total votes.

- The winner of the election was:
  - Diana Degette, who received 73.8% of the votes and 272,892 total votes.

## Overview of Election Audit
The purpose of this audit was to aid Tom, a member of the Colorado Board of elections employee, in validating the election results for the U.S. Congressional Precinct in Colorado. The 3 methods of voting we gathered were Mail-in ballots, punch cards, and Direct Recording Electronic votes. Our goal is to generate a vote count report to certify the U.S. Congressional race by using python to calculate total votes cast, number of votes per candidate, percentage of votes per canddiate, and the ultimate winner of the election.
   
## Election Audit Results
Note: All images will be shown below their respective bullet. The images will show the python code for tallying votes by adding 1 vote to the counter while iterating through each row. In the case of the candidates and counties, the code only added a vote to the tally if the county associated with it was correct. For the largest number of county votes and the winning candidate there are no images of code shown. Since our data set is so small, this could be seen by looking at the results themselves, but otherwise, this code simply compared each vote count for its respective county or candidate and displayed the largest value it could find.

- How many votes were cast in this congressional election?
   - 369,711 votes were cast in this election.

![total_votes](https://github.com/tateml0000/Election_Analysis/blob/main/total_votes.png)

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
   - Jefferson county had 10.5% of the votes made there and 38,855 total votes made there.
   - Denver county had 82.8% of the votes made there and 306,055 total votes made there.
   - Arapahoe county had 6.7% of the votes made there and 24,801 total votes made there.

![county_votes](https://github.com/tateml0000/Election_Analysis/blob/main/county_votes.png)

- Which county had the largest number of votes?
   - Denver county had the largest number of votes made with 82.8% of the votes made in that country, totaling 306,055 votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
   - Charles Casper Stockham received 23.0% of the votes and 85,213 total votes.
   - Diana DeGette received 73.8% of the votes and 272,892 total votes.
   - Raymon Anthony Doane received 3.1% of the votes and 11,606 total votes.

![candidate_votes_1](https://github.com/tateml0000/Election_Analysis/blob/main/candidate_votes_1.png)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
   - Diana Degette, who received 73.8% of the votes and 272,892 total votes.

## Election Audit Summary
With our current code, assuming a similar format, we have the ability to determine the U.S. Congressional election winner regardless of the number of candidates as well as number of votes, but we have the ability to improve and expand it

The work done for this election could be modified for many other elections including other congressional elections, senetorial elections, and local elections. Depending on the exact election one small modification that could be made would be to the counties involved in the election for local and senetorial elections. This list of counties could be changed to include zip codes, cities, or even a demographic of people if the candidates were looking for a breakdown of voters. 
   
![county_name](https://github.com/tateml0000/Election_Analysis/blob/main/county_name.png)
   
In this image we can see that the list of counties is just a reference to a certain column of data. Depending on the given data we could change the reference number "2" to use any data, for example, if we were given the same data with an extra column for "zip code" we could edit this data in a couple different places and replace "county_name" with a new variable such as "zip_code" (one of the places to edit shown below)
   
![edit_county_name](https://github.com/tateml0000/Election_Analysis/blob/main/edit_county_name.png)
   
Another big major application would be able to determine not only the primary results, but this could include a variable to include the respective political party of each candidate so every political candidate would have their party associated with their name and vote count. This would be helpful to avoid any errors in manual input. Below is a picture of where the code would be inserted, we would just add an extra line between lines 151 and 152 that says f"Candidate Party: {candidate_party}\n". This variable would need to be initialized earlier in the code (Shown in the second image) but it would allow for more transparancy in the results.

![lines_151-152](https://github.com/tateml0000/Election_Analysis/blob/main/line_151-152.png)

![initializing_variable](https://github.com/tateml0000/Election_Analysis/blob/main/initializing_variable.png)

Another major way our code could be updated would be to include a column for congressional districts. This way we could tally the results of multiple elections simulatneously. This would take a lot of editing for the code but the primary place to start is by separating candidates based on districts. We could use our code for each county and change it to one of the districts. 

![for_loop](https://github.com/tateml0000/Election_Analysis/blob/main/for_loop.png)

![if_statement](https://github.com/tateml0000/Election_Analysis/blob/main/if_statement.png)

In this picture we are using a for loop to cycle through each candidate and county and then we use an if statement to make sure there are no overlaps and begin to talley votes. To adjust this we would need to initalize a new dictionary as candidate_votes as well as have it talley only votes that relate to a specific candidate in a certain district. The likely hood of there being two candidates with the same name is very low, but to avoid any possible error we would still need to verify both the name and the district. If we only verified the name, we could run into problems with duplicate names, and if we only verified the district, then the vote count for each candidate would be equal to the total vote count.
