# CO2 Emissions and Agricultural Variables

## Table of Contents
1. [Overview](#overview)
2. [Project Details](#project-details)
   - [Background](#background)
   - [Goals](#goals)
   - [Methodology](#methodology)
   - [Highlights](#highlights)
   - [Dashboard](#dashboard)
3. [Conclusions](#conclusions)
4. [Future Work](#future-work)
5. [Collaborators](#collaborators)

## Overview

This project investigates the relationship between climate change and agricultural variables, focusing on how increasing CO2 emissions over time correlate with crop yields. The analysis explores CO2 emissions on both national and global scales to determine how these emissions interact with a country’s agricultural profile. Key variables examined include crop yield, crop type, pesticide use, and gross domestic product (GDP).

## Project Details

### Goals
Our primary goals were to answer the following questions:
- Do countries with higher agricultural land use have higher CO2 emissions?
- Is there a correlation between CO2 emissions and crop yield?
- Has pesticide use led to improved crop yields and reduced land use over time?
- Do countries with higher CO2 emissions use more pesticides to grow crops?
- What is the relationship between CO2 emissions and agricultural GDP?

### Methodology

1. **Data Collection:**
   - Data was sourced from [Our World in Data](https://ourworldindata.org/) and the Kaggle dataset [Climate Change Impact on Agriculture](https://www.kaggle.com/datasets/waqi786/climate-change-impact-on-agriculture/data).

2. **Data Cleaning:**
   - Relevant columns related to CO2 emissions and agricultural variables were selected for analysis.
   - Using `pandas`, we removed missing data (`dropna`) and duplicate entries (`drop_duplicates`), and renamed columns for consistency.
   - Merging datasets required cleaning columns like the country names. For instance, "Africa (AFO)" was standardized to "Africa," and "USA" was changed to "United States" for compatibility.

3. **Exploratory Data Analysis (EDA):**
   - We generated summary statistics to examine the mean, median, variance, standard deviation, and standard error for crop yields per hectare across countries.
   - Conducted linear regressions and Pearson’s correlation tests to investigate the relationships between CO2 emissions and variables like crop yield, crop type, pesticide use, GDP, and agricultural GDP.
   - Visualized time series data to track CO2 emissions over time by country.

4. **Feature Engineering:**
   - Created new variables, including:
      - **ag_gdp**: Agricultural GDP, capturing the size of agriculture relative to a country’s economy.
      - **pop_to_gdp**: Population-to-GDP ratio.
      - **pop_to_ag_gdp**: Population-to-agricultural-GDP ratio, to account for the role of population size in agricultural production.
   - Compiled a cumulative dataset for country-level comparisons.

5. **Data Analysis:**
   - Correlation analysis was performed on the main and cumulative datasets.
   - A multiple linear regression model was developed to predict CO2 emissions based on population, GDP, and agricultural GDP, explaining 57% of the variation in CO2 emissions.
   - Linear regressions explored the relationship between CO2 emissions and crop yield in the USA, as well as globally for various crops.
   - A pesticide correlation heatmap tested relationships between variables like CO2 emissions, GDP, agricultural GDP, population, total land, and pesticide use.

6. **Visualization:**
   - We generated line plots, scatter plots with linear regression, and correlation heatmaps using `pandas`, `matplotlib`, `scipy`, and `numpy`.
   - Visualizations included:
      - Scatter plots: CO2 emissions vs. forest fire incidents, agricultural land use, and life expectancy.
      - Line charts: CO2 emission trends and industrial emissions across countries.
      - Heatmaps: CO2 emissions vs. mortality rates, and CO2 emissions vs. pesticide use.
      - Interactive dashboards displaying correlation analyses filtered by GDP quartiles and outliers.

7. **Statistical Analysis:**
   - A statistical summary table displayed the central tendency and variation of crop yields across countries, with the standard error of the mean (SEM) indicating how representative the sample was of the broader population.
   - Pearson’s correlation and linear regressions explored CO2 emissions and their relationship with GDP quartiles and outliers.

8. **Tools and Libraries:**
    - **Pandas**: Data cleaning and manipulation.
    - **Numpy**: Numerical computations.
    - **Matplotlib & Seaborn**: Visualizations.
    - **Sklearn**: Linear regression modeling.
    - **Plotly**: Interactive visualizations.
    - **Scipy**: Statistical analysis.
    - **Dash**: Dashboard development.
    - **SQLite & SQLAlchemy**: Database management and querying.
    - **Kaleido**: Exporting high-quality static images.

## Highlights

#### Figure 1: CO2 Emissions Over Time by Country
![Figure 1](https://github.com/EdGonz44/Project-3/blob/main/images/ds1.png)

*This bar chart highlights the top 10 countries with the highest CO2 emissions over time. It provides a comparative view of emissions by country, helping identify major contributors to global CO2 output.*

#### Figure 2: Top 10 Countries by CO2 Emissions
![Figure 2](https://github.com/EdGonz44/Project-3/blob/main/images/ds2.png)

*This chart further breaks down the CO2 emissions of the top 10 countries, showing their relative contribution to global emissions.*

#### Figure 3: Summary Statistics of Crop Yield
![Figure 3](https://github.com/EdGonz44/Project-3/blob/main/images/jj1.png)

*The summary statistics table presents key metrics such as mean, median, variance, and standard error of the mean for crop yield (measured in metric tons per hectare) across different countries.*

#### Figure 4a: CO2 Emissions vs. Average Crop Yield (Global)
![Figure 4a](https://github.com/EdGonz44/Project-3/blob/main/images/jj2.png)

*This interactive scatter plot shows the relationship between CO2 emissions and average crop yield globally. The linear regression and Pearson's r correlation indicate the strength of this relationship. Users can hover over data points for detailed information.*

#### Figure 4b: CO2 Emissions vs. Average Crop Yield by Crop Type
![Figure 4b](https://github.com/EdGonz44/Project-3/blob/main/images/jj3.png)

*This interactive chart allows users to select different crop types from a dropdown menu to examine the relationship between CO2 emissions and crop yield for specific crops. It includes linear regression analysis and Pearson's r correlation for each crop type.*

#### Figure 5a: Pesticide Correlation Heatmap (Global)
![Figure 5a](https://github.com/EdGonz44/Project-3/blob/main/images/eg1.png)

*The global heatmap displays Pearson’s r correlation coefficients between various variables, including CO2 emissions, pesticide use, GDP, and agricultural GDP. Users can hover over each cell to view precise correlation values.*

#### Figure 5b: Pesticide Correlation Heatmap (By Quartiles & Outliers)
![Figure 5b](https://github.com/EdGonz44/Project-3/blob/main/images/eg2.png)

*This heatmap allows users to filter correlations based on GDP quartiles or outliers, offering a more granular analysis of the relationship between CO2 emissions, pesticide use, and other key variables.*

#### Figure 6a: CO2 Emissions vs. Pesticide Use (Global)
![Figure 6a](https://github.com/EdGonz44/Project-3/blob/main/images/eg3.png)

*This scatter plot with linear regression shows the global relationship between CO2 emissions and pesticide use. Pearson's r correlation is used to measure the strength of the association.*

#### Figure 6b: CO2 Emissions vs. Pesticide Use (By Quartiles & Outliers)
![Figure 6b](https://github.com/EdGonz44/Project-3/blob/main/images/eg4.png)

*Continuing from the previous figure, this scatter plot allows users to filter data by GDP quartiles and outliers, offering insights into how economic factors influence the relationship between CO2 emissions and pesticide use.*

#### Figure 7: CO2 Emissions by GDP Quartile
![Figure 7](https://github.com/EdGonz44/Project-3/blob/main/images/mo1.png)

*This line chart displays CO2 emissions over time, segmented by GDP quartile. Users can choose to view all countries or focus on specific quartiles to analyze emissions trends relative to economic status.*

## Interactive Dashboard Access
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install dash plotly pandas
   ```
3. Place data files (e.g., `data.json`) in the project directory.
4. Run the app:
   ```bash
   python app.py
   ```

## Conclusions
- There was no correlation found between CO2 emissions and crop yields.
- Pesticides and CO2 emissions do not show consistent correlation across economic groupings.
- Strong relationships were found between CO2 emissions, population, and agricultural GDP.
- The dashboard is a powerful tool to explore how variables like industrial activities, forest fires, crop yield, and pesticide use impact CO2 emissions.
- Small standard deviations in crop yields per hectare suggest consistent yields across countries. Low SEM indicates the sample data closely represents the population means.

## Future Work
- Investigate correlations between CO2 emissions and the nutritional value of crops.
- Expand health metrics to include more detailed data on disease prevalence linked to air pollution.
- Incorporate real-time data to monitor the ongoing effects of climate policies.
- Include data on agricultural imports and exports to explore the role of trade in food production.

## Collaborators
- **Eddie Gonzalez**: Data analysis, visualization, database, dashboard development, CO2, pesticides, and GDP analysis.
- **Dhwani Shah**: Data analysis, visualization, database, dashboard development, trend analysis.
- **Jenny Jaurequi**: CO2 emissions, crop yield analysis, README development.
- **Megan O'Connor**: Secondary research, narrative development, CO2 emissions & agricultural GDP analysis.
