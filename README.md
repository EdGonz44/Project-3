# Project-3
CO2 Emissions, Mortality, and the Impact of Environmental Action

# Project Title

## Table of Contents
1. [Overview](#overview)
2. [Project Details](#project-details)
   - [Background](#background)
   - [Goals](#goals)
   - [Methodology](#methodology)
3. [Conclusions](#conclusions)
4. [Future Work](#future-work)
5. [Collaborators](#collaborators)

## Overview

### What is this project about?
This project explores the relationship between CO2 emissions and agriculture. It aims to understand the impact how the increase of co2 emissions over time has impacted crop yields and how farmers have adjusted to this.

## Project Details

### Background
Our initial goal was to see how CO2 emissions have impacted the crops over time and therefore impacted human health.

### Goals
- **[Dhawani]** Do countries with higher land use for agriculture have higher CO2 emissions.
- **[Megan]** What is the relationship between CO2 emissions and agricultural gdp.
- **[Eduardo]** Do countries with higher CO2 emissions use more pesticides to grow their crops?
- **[Jenny]** Has crop yield improved over time with pesticides? Has pesticide use decreased the amount of land needed to produce crops?

### Methodology
Detail the approach and methods used to achieve the project's goals.

In the "Methodology" section, you would typically describe the specific approaches, techniques, tools, and processes you used to accomplish the project's goals. Here are some examples of what you might include:

1. **Data Collection:**
   - Data was downloaded from [Our World in Data](https://ourworldindata.org/).

2. **Data Cleaning:**
   - Explain how you processed and cleaned the data to make it suitable for analysis. This could involve handling missing values, removing duplicates, or correcting data types.
   - **Example:** "Data was cleaned using Pandas, with missing values imputed using the median for continuous variables and mode for categorical variables."

3. **Data Transformation:**
   

4. **Exploratory Data Analysis (EDA):**
   - Summary statistics and correlation analyses for the dataframe.
   - Visualized timeseries data.

5. **Feature Engineering:**
   - Created new variables:
      - **ag_gdp** which is the GDP from agriculture and meant to capture the size of agriculture produced to better compare countries. This is created from the the percent of agricultural GDP and GDP.
      - **pop_to_gdp** which is the multiple for population to GDP.
      - **pop_to_ag_gdp** which is the multiple for population to agricultural GDP and is meant to account for population size and how much agriculture is produced.
   - Created an additional dataframe of the cumulative data by country.

6. **Data Analysis:**
   - Correlation analyses or main dataframe and cummulative dataframe.
   - Explored regression models where the outcome being predicted was CO2 emissions. A multiple linear regression model was created with the variables population, gdp, and agricultural gdp that explained 57% of the variation in CO2 emissions.

7. **Modeling and Prediction:**
   - If applicable, describe any machine learning models you used to make predictions or classify data.
   - **Example:** "A Random Forest model was trained to predict precipitation levels based on latitude and other weather variables."

8. **Visualization:**
   - Detail the tools and techniques you used to create visual representations of the data.
   - **Example:** "Heatmaps and line plots were generated using Seaborn to illustrate the correlation between humidity and latitude."

9. **Statistical Analysis:**
   - Describe any statistical methods you employed to analyze the data, such as hypothesis testing, ANOVA, or time series analysis.
   - **Example:** "A t-test was performed to compare the mean temperatures of cities at different latitudes."

10. **Tools and Libraries:**
    - Pandas: For data cleaning and manipulation.
    - Numpy: For numerical computations.
    - Matplotlib & Seaborn: For visualizations.
    - Sklearn: For linear regression.

#### Figure 0: [Figure Title]
![Figure 0](path/to/figure0.png)

*Brief description of Figure 0.*

#### Figure 1: [Figure Title]
![Figure 1](path/to/figure1.png)

*Brief description of Figure 1.*

#### Figure 2: [Figure Title]
![Figure 2](path/to/figure2.png)

*Brief description of Figure 2.*

#### Figure 3: [Figure Title]
![Figure 3](path/to/figure3.png)

*Brief description of Figure 3.*

#### Figure 4: [Figure Title]
![Figure 4](path/to/figure4.png)

*Brief description of Figure 4.*

#### Figure 5: [Figure Title]
![Figure 5](path/to/figure5.png)

*Brief description of Figure 5.*

## Conclusions

Summarize the key findings or results of the project.

## Future Work
- Add more data related to agriculture that's imported/exported.
- Exploration of agricultural production on the environment - related emissions to production.

## Collaborators
- **[Megan]** Secondary research, story development, analysis related to CO2 emissions & agricultural GDP.
