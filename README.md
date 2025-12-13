# CHIP-690-Project---Estradiol-Analysis
## Overview
In recent months the Food and Drug Administration (FDA) has taken the black box warning off hormone replacement therapy (hrt) drugs. One of these drugs called estradiol which had the black box label due to its high risks for blood clots, heart attack, stroke, and certain cancers. In this milestone, I am analyzing the population of people who have taken estradiol and had an adverse effect from it.

## Research Questions
1.	What are the common adverse effects of taking estradiol?
2.	How many people died from estradiol?
3.	What percentages of people had the adverse effects of each high risk : blood clots, heart attack, stroke, and cancer?

## Data Sources and Data Extracting
The information for this report is provided by the FDA Adverse Event Reporting System (FAERS) and reports from the years 2004-2025 were used.

Due to long loading times when accessing the data via URL, I opted to download the datasets as Excel files instead. These files were downloaded thru the FAERS public dashboard and filtered before downloading. In total there was about 42,000 cases of adverse effects involving estradiol thru the years 2004-2025, after filtering entries involving outcomes such as "Died, Hospitalizied, and Non-Serious" the entries from 2004-2025 were 29,441. One file was entries from years 2004-2014, while the other one was 2015-2025. These two files were then combined to create one estradiol database used for analysis. 

## Tools
- Pandas
- Matplotlib
- Collections

## Data Cleaning
- Both files were turned into csv files with utf-8 encoding.
- Unneccessary columns such as 'Literature Reference' and 'Reporter Type'.
- Rows were dropped if 'Suspect Product Active Ingredients' columns were blank.

## Data Analysis
- From the collections module in Python Counter was used to count the amount of time each side effect was used then shown in a bar chart
- All reactions that were manufacturing based were removed to show only physical side effects.
- Value_counts were used to create a pie chart of outcomes
- For the four high risks other names for these issues were checked in the FAERS database.
- Any entries that was mentioned as a keyword was put into a category for the final pie chart. 

## Citations 
- OpenAI. (2025). ChatGPT (GPT-5.2) [Large language model]. https://chat.openai.com/
- U.S. Department of Health and Human Services. (2025, November 10). FACT SHEET: FDA initiates removal of “black box” warnings from menopausal hormone replacement therapy products. HHS.gov. https://www.hhs.gov/press-room/fact-sheet-fda-initiates-removal-of-black-box-warnings-from-menopausal-hormone-replacement-therapy-products.html
- Leonardo, H(2025). Comparative Side Effect Analysis of Three Generations of Antidepressants[Unpublished course project]. Senior Capstone MA490, Embry-Riddle Aeronautical University.





