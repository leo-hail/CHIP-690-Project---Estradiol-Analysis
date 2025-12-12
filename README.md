# CHIP-690-Project---Estradiol-Analysis
## Overview
In recent months the Food and Drug Administration (FDA) has taken the black box warning off hormone replacement therapy (hrt) drugs. One of these drugs called estradiol which had the black box label due to its high risks for blood clots, heart attack, stroke, and certain cancers. In this milestone, I am analyzing the population of people who have taken estradiol and had an adverse effect from it.

## Research Questions
1.	What are the common adverse effects of taking estradiol?
2.	How many people died from estradiol?
3.	What percentages of people had the adverse effects of each high risk : blood clots, heart attack, stroke, and cancer?

## Data Sources and Format Reasoning
The information for this report is provided by the FDA Adverse Event Reporting System (FAERS) and reports from the years 2004-2025 were used.

Due to long loading times when accessing the data via URL, I opted to download the datasets as Excel files instead. These files were downloaded thru the FAERS public dashboard and filtered before downloading. In total there was about 42,000 cases of adverse effects involving estradiol thru the years 2004-2025, after filtering entries involving outcomes such as "Died, Hospitalizied, and Non-Serious" the entries from 2004-2025 were 29,441. One file was entries from years 2004-2014, while the other one was 2015-2025. These two files were then combined to create one estradiol database used for analysis. 
