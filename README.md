# Project-3

# CO2 Emissions, Health Metrics, and Environmental Impact Analysis

## Table of Contents
- [Overview](#overview)
- [Project Details](#project-details)
- [Goals](#goals)
- [Methodology](#methodology)
- [Visualizations](#visualizations)
- [Conclusions](#conclusions)
- [Future Work](#future-work)
- [Collaborators](#collaborators)
- [Tools and Libraries](#tools-and-libraries)
- [Instructions](#instructions)
- [Ethical Considerations](#ethical-considerations)
- [References](#references)

## Overview
<<<<<<< HEAD

### What is this project about?
This project explores the relationship between CO2 emissions and agriculture. It aims to understand the impact how the increase of co2 emissions over time has impacted crop yields and how farmers have adjusted to this.
=======
This project explores the relationship between CO2 emissions and various environmental and human health factors, including agricultural activities, forest fires, industrial activities, and population growth. The aim is to provide insights that can inform policymakers on how to reduce CO2 emissions and improve public health. Using global datasets from 1990 to 2020, the project leverages interactive visualizations to uncover patterns between CO2 emissions, health indicators, and environmental metrics, such as temperature and forest fires, across different countries.
>>>>>>> 94d6bd7ecc13e1a775abde488cb9da007330c3b1

## Project Details

### Background
<<<<<<< HEAD
Our initial goal was to see how CO2 emissions have impacted the crops over time and therefore impacted human health.

### Goals
- **[Dhawani]** Do countries with higher land use for agriculture have higher CO2 emissions.
- **[Megan]** What is the relationship between CO2 emissions and agricultural gdp.
- **[Eduardo]** Do countries with higher CO2 emissions use more pesticides to grow their crops?
- **[Jenny]** Has crop yield improved over time with pesticides? Has pesticide use decreased the amount of land needed to produce crops?
=======
Rising CO2 emissions are a significant contributor to climate change, affecting both environmental stability and human health. This project focuses on how emissions are influenced by factors such as industrial growth, agricultural activities, and forest fires, and how these emissions correlate with health outcomes like mortality rates and life expectancy. The data spans global emissions and environmental metrics from various regions, providing a comprehensive analysis of the impacts of emissions over time.

## Goals
- Analyze the relationship between CO2 emissions and factors such as agricultural land use, forest fires, and industrial activities.
- Explore correlations between CO2 emissions and health outcomes, including mortality rates and life expectancy.
- Create an interactive dashboard to allow users to filter and visualize data by region, year, and specific emission sources.
- Investigate how population growth impacts CO2 emissions and explore potential mitigation strategies.
>>>>>>> 94d6bd7ecc13e1a775abde488cb9da007330c3b1

## Methodology

### Data Collection
- Global datasets on CO2 emissions, agricultural activities, forest fires, and health metrics were collected from public repositories.
- Data was sourced from CSV and JSON files and stored in an SQLite database for analysis covering the period 1990 to 2020.

<<<<<<< HEAD
1. **Data Collection:**
   - Data was downloaded from [Our World in Data](https://ourworldindata.org/).
=======
### Data Cleaning
- Data was cleaned using Pandas to handle missing values and ensure consistency. Additional columns, such as "CO2 emission per capita," were created for deeper analysis.
>>>>>>> 94d6bd7ecc13e1a775abde488cb9da007330c3b1

### Data Transformation
- Transformations included scaling and normalizing data, with new metrics generated (e.g., forest fire emissions to total emissions ratio).

<<<<<<< HEAD
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
=======
### Exploratory Data Analysis (EDA)
- Tools like Plotly, Matplotlib, and Seaborn were used to create line charts, scatter plots, and heatmaps to explore relationships between variables.

### Data Analysis
- Correlation matrices and linear regression models were used to identify the impact of CO2 emissions on health and environmental factors.

### Interactive Dashboard
- A Dash-based dashboard allows users to explore emissions data, filter by country, emission source, and visualize relationships between CO2 emissions and natural / industrial activities using different charts. 

## Visualizations
- **CO2 Emissions by Year**: Line chart showing CO2 emission trends globally.
- **CO2 Emissions vs Forest Fires**: Scatter plot of CO2 emissions against forest fire incidents.
- **CO2 Emissions vs Industrial Activity**: Line chart comparing emissions from industrial activities across countries.
- **Health Impacts of CO2 Emissions**: Heatmap showing correlations between CO2 emissions and mortality rates.
- **CO2 Emissions vs Population (2020)**: Bubble chart illustrating the relationship between population size and CO2 emissions.
- **Agricultural Land (%) vs CO2 Emissions**: Scatter plot showing the correlation between agricultural land use and CO2 emissions.
- **CO2 Emissions vs Life Expectancy**: Scatter plot highlighting the relationship between CO2 emissions and life expectancy.
- **Top 10 Countries by CO2 Emissions**: Bar chart listing the leading contributors to global CO2 emissions.
>>>>>>> 94d6bd7ecc13e1a775abde488cb9da007330c3b1

## Conclusions
The analysis confirms that CO2 emissions are driven primarily by industrial activities, forest fires, and population growth. A significant correlation was found between higher emissions and adverse health outcomes, including increased mortality rates. The dashboard provides a powerful tool for policymakers to explore these relationships and make data-driven decisions to mitigate the effects of emissions on public health and the environment.

## Future Work
<<<<<<< HEAD
- Add more data related to agriculture that's imported/exported.
- Exploration of agricultural production on the environment - related emissions to production.

## Collaborators
- **[Megan]** Secondary research, story development, analysis related to CO2 emissions & agricultural GDP.
=======
- Expand health metrics to include more detailed data on disease prevalence linked to air pollution.
- Investigate the impact of reforestation and clean energy adoption on reducing CO2 emissions.
- Evaluate the effectiveness of current environmental policies in reducing emissions.
- Incorporate real-time data to monitor ongoing effects of climate actions and policies.

## Collaborators
- **[Dhwani]**: Data analysis, dashboard development, visualizations, Database management, data cleaning,conclusions, and future work recommendations.

## Tools and Libraries
- **Dash**: For building the interactive dashboard.
- **Plotly**: For creating interactive visualizations.
- **Pandas**: For data cleaning and manipulation.
- **Matplotlib & Seaborn**: For static visualizations.
- **SQLite**: For managing the dataset.
- **SQLAlchemy**: For database querying.
- **Numpy**: For numerical computations.
- **Kaleido**: For exporting high-quality static images of visualizations

## Instructions to use interactive dashboard.
1. Clone the repository.
2. Install required Python libraries:
   ```bash
3. pip install dash plotly pandas
   Place data files (e.g., data.json) in the project directory.
4. Run the app:
5. python app.py

## Ethical Considerations
The project uses publicly available, anonymized datasets to ensure data privacy. Care was taken to present objective correlations between environmental factors and health outcomes without overstating causality. The analysis was conducted transparently to support unbiased reporting and inform equitable policy decisions.

## References:
World Bank Open Data
World Health Organization (WHO) Global Health Observatory
kaggle

## Links : 

Global Country Information Dataset 2023 - kaggle 

🌍 Climate Change Impact on Agriculture 🌱 - kaggle 

CO₂ and Greenhouse Gas Emissions - our world in data

Agri-food CO2 emission dataset - Forecasting ML - kaggle 

>>>>>>> 94d6bd7ecc13e1a775abde488cb9da007330c3b1
