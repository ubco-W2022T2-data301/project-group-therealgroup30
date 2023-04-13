# Group 30 - Mortgage Affordabilty Analysis

*"Helping future home buyers one cell at a time"*

## The dataset

Our dataset is on mortgage affortability in the US with data from 1999-2016. The dataset was found on data.world and data is from Zillow. The dataset shows the percentage of income spent on a mortgage, data is organized quarterly and is calcualted as a part of Zillow’s quarterly Affordability Indices. To calculate mortgage affordability, Zillow calculates the mortgage payment for the median-valued home in a metropolitan area by using the metro-level Zillow Home Value Index for a given quarter and the 30-year fixed mortgage interest rate during that time period based on a 20 percent down payment. Then they consider what portion of the monthly median household income (U.S. Census) goes toward this monthly mortgage payment. Data is organized by metropolitan area and considers bottom, middle, and top tier homes/incomes. Zillow is a tech real-estate marketplace so the reason for data collection is quite trivial, they collect and analyze real estate data to provide valuable insights to home buyers and sellers. Data was collected by means of Freddie Mac Primary Mortgage Market Survey for mortage rates and the US Census for average monthly income. 

## Introduction

A common interest theme that appeared when discussing this dataset among team members is that it is relatively actual to our generation. Skyrocketing home prices since Covid as well as never-ending interest rate spikes have driven home affordability incredibly low. This mortage affordability dataset covers the US up to 2017 and contains relevant information as first-time home buyers in Canada are facing an unprecedented real estate market. Additionally, the large scale of this dataset offers a lot of research angles, leaving a lot of flexibility for our group to conduct a data science project. 

Throughout this data analysis project we wil discuss a variety of factors which affect and/or relate to mortgage affordability as well as our findings. Such findings stem from the influence of population size, state or region and/or its location, the difference between different class levels of US citizens and the result of time. 

## Exploratory Data Analysis Highlights 

During our exploratory data analysis, our aim was to gain a comprehensive understanding of the national growth rate for the house affordability ratio. We achieved this by examining the "United States overall" row, which calculates the average for each date and tier across all regions within the dataset. To visualize these findings, we employed pandas, numpy, matplot and seaborn to create a modified dataset and generate a linear graph. This graph featured three linear trends representing the bottom, middle, and upper tiers.

![Seaborn EDA visualization](/images/alrick/EDA_tier_affordability.png)

## Question 1

Given that our dataset contains regional data organized by states, we found it compelling to aggregate each region by its corresponding state and compute the average mortgage affordability ratio for comparison. This led us to the following research question: **What are the variations in affordability ratios across different states, and what factors could account for these disparities?**. To investigate this question, we will delve further into choropleth visualizations, enabling us to effectively illustrate the distribution of housing affordabililty ratios in the United States over time.

![United States Choropleth](/images/alrick/chloropleth_byStates.PNG)

The choropleth provides an immediate understanding of the mortgage affordability ratio concentration within each state. We observe significant disparities among the states, which we further analyze using a bar plot for numerical visualization:

![Average Affordability Ratio by States in Descending Order](/images/alrick/affordability_states_barPlot.png)

The initial visualizations reveal that California has the highest affordability ratio, indicating a less favorable situation. There is a substantial gap between California and the next highest state, Massachusetts. To represent the evolution of affordability ratios by state, we generated a time series line plot, which allows us to track changes in affordability ratios for each state throughout the years.

![Affordability Ratio Over Time By State](/images/alrick/affordability_overTime_states_lineChart.png)

We can see that affordability ratios have experienced fluctuations over time, with some periods exhibiting more pronounced changes than others. Certain states display similar trends, including a spike in affordability ratios between 2006 and 2008, while others exhibit unique patterns.

The affordability ratio varies widely across states, and these differences can be attributed to a variety of factors not directly evident in the graphs. Such factors include regional economic conditions, local housing markets, and state-level policies. As established in our first research question, population rank does not significantly impact the affordability ratio, even at the state level. By examining the visualizations, we can discern common trends and patterns among regions, characterized by distinct spikes and drops (where spikes are unfavorable and drops are favorable) over the years.

## Q2:


## Q3:

## Analysis Links

If you are further interested in data science and would like to check out our in-depth analysis and code, you can find below the link to our three separate analyses:

Angelina: [](/analysis/analysisAngelina.ipynb)
Alrick: [](/analysis/analysisAlrick.ipynb)
Will: [](/analysis/analysisWill.ipynb)

## References

All Data, raw and refined, is attributed to Zillow Group, inc.