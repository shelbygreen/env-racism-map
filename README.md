# Mapping Environmental Racial Inequality in Texas

## Objective
Guided by the Texas Freedom Network, Climate Cabinet will provide data on race, income, and air pollution, creating a map of disparate impact from pollution in Texas. This mapping tool will help identify Texas communities that are most affected by pollution and that are vulnerable to pollution’s effects. It will be vital in increasing rates of awareness of climate change among the next generation of voters and policymakers in Texas.

## Timeline (Gantt Chart)

## Background
While all Texans feel the environmental impacts of pollution and a changing climate, low-income communities and communities of color feel it more. Spatial, economic, and racial injustices are products of unjust policies designed to further the divide between struggle and prosperity. These major drivers are the reason why 82% of all of the waste dumped in Houston, from the 1930s to 1978, was in black neighborhoods (Bullard, R. (2000). Dumping in Dixie: Race, Class, and Environmental Quality. Westview Press). And why there is a concentrated prevalence of chemical plants, but lack of grocery stores, in low-income communities and communities of color (Texas Southern University, 2017).

## What is the problem?
Communities of color and low-wealth are disproportionately exposed to environmental pollutants and hazards. The EPA pointed out that minorities and those with lower incomes were exposed more often to several air pollutants, hazardous waste facilities, contaminated fish, and agricultural pesticides at the workplace and black children had significantly higher blood lead levels compared to white children. The environmental disparities are caused by the combination of the location of polluting activities and residencies. Industries locate where land prices are low and labor forces reside. Therefore, people with a lower socio-economic status often live nearby these industries.

### What constraints need to be acknowledged?


## Cumulative Impact Assessment 
CIA is a methodology to identify populations bearing a disproportionate health risk burden. A CIA will estimate differential health risks from environmental exposures within populations, examine the extent and sources of environmental inequality, and identify high-risk areas.

### 1. Identify the indicators and their data sources
## Polluation Burden Indicators 
|   Component               |   Indicator                                      |   Description                                                                                                     |   Data Source                                                                                                |   Unit of Analysis Available  |
|---------------------------|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------|
|   Environmental Exposure  |   Ozone concentration                            |   Ozone summer seasonal avg. of daily maximum 8-hour concentration in air in parts per billion                    |   EPA, Office of Air and Radiation (OAR) fusion of model and monitor data; CDC’s Daily PM2.5 Concentrations  |   County; Census tract        |
|   Environmental Exposure  |   PM2.5 concentration                            |   PM2.5 levels in air, µg/m3 annual avg.                                                                          |   EPA, OAR fusion of model and monitor data; CDC’s Daily PM2.5 Concentrations                                |   County; Census tract        |
|   Environmental Exposure  |   Toxic releases from facilities                 |   Toxicity-weighted concentrations of chemical releases to air from facility emissions and off-site incineration  |   EPA, Risk Screening Environmental Indicators (RSEI)                                                        |   County; Census tract        |
|   Environmental Exposure  |   Traffic density                                |   Percentage of population exposed to busy roadways                                                               |   Texas State Department of Transportation                                                                   |   County; Census tract        |
|   Environmental Exposure  |   Diesel emissions                               |   Diesel particulate matter level in air, µg/m3                                                                   |   EPA, National Air Toxics Assessment                                                                        |   County; Census tract        |
|   Environmental Effects   |   Lead risk and exposure                         |   Total number of houses and proportion of houses by year of construction                                         |   ACS 5 year estimates                                                                                       |   County; Census tract        |
|   Environmental Effects   |   Proximity to Risk Management Plan (RMP) sites  |   Count of RMP facilities within 5km, each divided by distance in kilometers                                      |   EPA, RMP Database                                                                                          |   County; Census tract        |
|   Environmental Effects   |   Proximity to Superfund sites                   |   Count of proposed or listed superfund sites within 5 km, each divided by distance in kilometers                 |   EPA, CERCLIS database                                                                                      |   County; Census tract        |
|   Environmental Effects   |   Proximity to Hazardous Waste Facilities        |   Count of hazardous waste facilities within 5km, each divided by distance in kilometers                          |   EPA, RCRAInfo Database                                                                                     |   County; Census tract        |
|   Environmental Effects   |   Wastewater Discharge                           |   RSEI modeled Toxic Concentrations at stream segments within 500 meters, divided by distance in kilometers (km)  |   EPA, RSEI modeled toxic concentrations to stream reach segments                                            |   County; Census tract        |
## Population Indicators
|   Component              |   Indicator                          |   Description                                                                   |   Data Source                                |   Unit of Analysis Available  |
|--------------------------|--------------------------------------|---------------------------------------------------------------------------------|----------------------------------------------|-------------------------------|
|   Sensitive Populations  |   Cardiovascular disease             |   Mortality rate from cardiovascular diseases per 100,00 population             |   Texas Department of State Health Services  |   County                      |
|   Sensitive Populations  |   Chronic lower respiratory disease  |   Mortality rate from chronic lower respiratory diseases per 100,00 population  |   Texas Department of State Health Services  |   County                      |
|   Sensitive Populations  |   Low birth weight infants           |   % births weighing < 5.5 lbs                                                   |   Texas Department of State Health Services  |   County                      |
|   Sensitive Populations  |   Children and older adults          |   % population aged <10 y or >65 y                                              |   US Census Bureau                           |   County; Census tract        |
|   Socioeconomic Factors  |   Educational attainment             |   % population over age 25 with less than a high school education               |   ACS 5 year estimates                       |   County; Census tract        |
|   Socioeconomic Factors  |   Housing Burden                     |   % population where > 30% income goes towards rent                             |   ACS 5 year estimates                       |   County; Census tract        |
|   Socioeconomic Factors  |   Poverty                            |   % population living below 185% of the federal poverty level                   |   ACS 5 year estimates                       |   County; Census tract        |
|   Socioeconomic Factors  |   Race                               |   % non-white                                                                   |   ACS 5 year estimates                       |   County; Census tract        |

### 2. Correlation Analysis
Correlation analysis is a statistical technique for investigating the relationship between two continuous quantitative variables, and indicates the probability of one condition occurring, given that the other condition is present. A Pearson’s Correlation Coefficient (r) measures the strength and direction of the relationship that exists between these two sets of variables, and can range in a continuum between the values of -1 and +1. Spearman rank correlation is a non-parametric test that is used to measure the degree of association between two variables.

### 3. Cumulative Score Calculation
Score = Pollution Burden Score x Population Characteristics

#### Calculating the Pollution Burden Score
1. Raw values for each environmental exposure and effects indicator are assigned a percentile rank based on their relative value to the values for that indicator. Action performed on all counties/census tracts in Texas. Counties/census tracts that have no value for an indicator are excluded from the percentile ranking and assigned a 0 percentile score to mitigate against underestimating.

2. The sum of the environmental exposure indicator percentiles and the half-weighted environmental effect indicator percentiles are then divided by 7.5 (from 5 + 0.5*5). 

3. The averaged cumulative pollution burden percentiles are scaled to a range of zero to ten by (1) dividing them by the highest average cumulative pollution burden percentile and (2) multiplying the result by ten. 

#### Calculating the Pollution Burden Score
1. Raw values for each sensitive populations and socioeconomics indicator are assigned a percentile rank based on their relative value to the values for that indicator. Action performed on all counties/census tracts in Texas. Counties/census tracts that have no value for an indicator are excluded from the percentile ranking and assigned a 0 percentile score to mitigate against underestimating.

2. The sum of the environmental exposure indicator percentiles and the half-weighted environmental effect indicator percentiles are then divided by 8 (from 4 + 4). 

3. The averaged cumulative pollution burden percentiles are scaled to a range of zero to ten by: (1) dividing them by the highest average cumulative pollution burden percentile and (2) multiplying the result by ten.

### 4. Data Visualization
### 5. Interactive Mapping Tool 


## Sources
1. Loustaunau, M. G., & Chakraborty, J. (2019). Vehicular Air Pollution in Houston, Texas: An Intra-Categorical Analysis of Environmental Injustice. International journal of environmental research and public health, 16(16), 2968. https://doi.org/10.3390/ijerph16162968
2. Crawford, J. (2018). Environmental Racism in Houston's Harrisburg/Manchester Neighborhood. http://bay.stanford.edu/blog/2018/3/15/environmental-racism-in-houstons-harrisburgmanchester-neighborhood
3. Union of Concerned Scientists. (2016). Double Jeopardy in Houston. https://www.ucsusa.org/resources/double-jeopardy-houston
4. Moderator: Sacoby M. Wilson, Participants: Robert Bullard, Jacqui Patterson, and Stephen B. Thomas. Environmental Justice. Jun 2020.56-64.http://doi.org/10.1089/env.2020.0019
5. Kruize, H., Droomers, M., van Kamp, I., & Ruijsbroek, A. (2014). What causes environmental inequalities and related health effects? An analysis of evolving concepts. International journal of environmental research and public health, 11(6), 5807–5827. https://doi.org/10.3390/ijerph110605807
6. Crowder, K., & Downey, L. (2010). Interneighborhood migration, race, and environmental hazards: modeling microlevel processes of environmental inequality. AJS; American journal of sociology, 115(4), 1110–1149. https://doi.org/10.1086/649576
