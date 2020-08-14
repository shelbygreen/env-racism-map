# Mapping Environmental Racial Inequality in Texas, 2020

## Objective
Guided by the Texas Freedom Network, Climate Cabinet will provide data on race, income, and air pollution, creating a map of disparate impact from pollution in Texas. This mapping tool will help identify Texas communities that are most affected by pollution and that are vulnerable to pollution’s effects. It will be vital in increasing rates of awareness of climate change among the next generation of voters and policymakers in Texas.

## Timeline (Gantt Chart)

## Background
While all Texans feel the environmental impacts of pollution and a changing climate, low-income communities and communities of color feel it more. Spatial, economic, and racial injustices are products of unjust policies designed to further the divide between struggle and prosperity. These major drivers are the reason why 82% of all of the waste dumped in Houston, from the 1930s to 1978, was in black neighborhoods (Bullard, R. (2000). Dumping in Dixie: Race, Class, and Environmental Quality. Westview Press). And why there is a concentrated prevalence of chemical plants, but lack of grocery stores, in low-income communities and communities of color (Texas Southern University, 2017).

## What is the problem?
Communities of color and low-wealth are disproportionately exposed to environmental pollutants and hazards. The EPA pointed out that minorities and those with lower incomes were exposed more often to several air pollutants, hazardous waste facilities, contaminated fish, and agricultural pesticides at the workplace and
black children had significantly higher blood lead levels compared to white children. The environmental disparities are caused by the combination of the location of polluting activities and residencies. Industries locate where land prices are low and labor forces reside. Therefore, people with a lower socio-economic status often live nearby these industries.

## Cumulative Risk Assessment 
### 1. Set the research question: Who suffers the most from exposure to industrial pollution?
CRA is a tool to identify populations bearing a disproportionate health risk burden. A CRA will estimate differential health risks from environmental exposures within populations, examine the extent and sources of environmental inequality, and identify high-risk areas.
### 2. Identify the indicators and their data sources
### 3. Data preparation and cleaning
### 4. Data analysis
#### 4a. Exploratory data analysis
#### 4b. Imputation
#### 4c. Diagonistic Checking
### 5. Statistical Trend Analysis
### 6. Data visualization

### Hypotheses
Proximate industrial pollution is a continuous, tract-level measure of neighborhood proximity to TRI facility air pollution that weights the potential effect of each TRI facility inversely according to geographic distance from the facility, thereby incorporating both the level of toxic air emissions produced by each TRI facility and facility proximity to the center of each census tract.


The following variables will be explored to establish relationships and trends that support the existence of environmental racism:
| Variable       | Type  | Justification | Source  |
| :--------------| :------------:| :-------| -------:|
| Non-white population       | Socioeconomic | Hispanics and non-Hispanic Blacks are disproportionately exposed to outdoor air pollution and related health risks than non-Hispanic Whites       | [American Community Survey](https://www.census.gov/programs-surveys/acs/data.html) |
| People living below the poverty line (%)    | Socioeconomic      | Socially advantaged individuals are less likely to suffer adverse health effects because they can afford to equip their dwellings with air purification, purchase newer homes, and/or reside in neighborhoods with lower exposure to air pollution.   | [American Community Survey](https://www.census.gov/programs-surveys/acs/data.html) |
| PM2.5 (and other air pollutants) Exposure | Environmental   | To identify the air pollution burden and chemicals with the greatest health impacts  | [USEPA's National Air Toxic Assessment](https://www.epa.gov/national-air-toxics-assessment/2014-national-air-toxics-assessment) and [the USEPA's Risk Screening Environmental Indicators model](https://www.epa.gov/rsei)  |
| Proximity to hazardous sites* | Environmental  | Individuals who live close (within 1 mi (fenceline zone) or within 25 mi (vulnerability zone) to noxious industrial facilities and waste sites are more likely to be hospitalized for asthma. Communities closest to these hazardous facilities are likely to experience the greatest impacts from an explosion or chemical release—and would have the least amount of time to escape these dangers | [USEPA's Toxic Release Inventory](https://www.epa.gov/toxics-release-inventory-tri-program), [USEPA's Risk Management Plan](https://rtk.rjifuture.org/rmp/location_search/search_by_location/?city=&county=&state=TX), and Google Places API |
| Concentration of traffic-related air pollution (TRAP) zones | Environmental   | Living near highly trafficked freeways/highways increases the of damage to developing brains, lungs, hearts, and circulatory systems. In addition to particulate pollution and ground-level ozone, a number of traffic-related air pollutants – such as diesel particulate matter, benzene, 1,3 butadiene, and formaldehyde – are known to cause cancer.  | [USEPA’s 2011 National-Scale Air Toxics Assessment](https://www.epa.gov/national-air-toxics-assessment/2011-national-air-toxics-assessment) |

*hazardous sites include refineries, chemical plants, energy plants, wastewater/sewage treatment facilities, landfills, and hazardous waste sites. 

### What constraints need to be acknowledged?


## Sources
1. Loustaunau, M. G., & Chakraborty, J. (2019). Vehicular Air Pollution in Houston, Texas: An Intra-Categorical Analysis of Environmental Injustice. International journal of environmental research and public health, 16(16), 2968. https://doi.org/10.3390/ijerph16162968
2. Crawford, J. (2018). Environmental Racism in Houston's Harrisburg/Manchester Neighborhood. http://bay.stanford.edu/blog/2018/3/15/environmental-racism-in-houstons-harrisburgmanchester-neighborhood
3. Union of Concerned Scientists. (2016). Double Jeopardy in Houston. https://www.ucsusa.org/resources/double-jeopardy-houston
4. Moderator: Sacoby M. Wilson, Participants: Robert Bullard, Jacqui Patterson, and Stephen B. Thomas. Environmental Justice. Jun 2020.56-64.http://doi.org/10.1089/env.2020.0019
5. Kruize, H., Droomers, M., van Kamp, I., & Ruijsbroek, A. (2014). What causes environmental inequalities and related health effects? An analysis of evolving concepts. International journal of environmental research and public health, 11(6), 5807–5827. https://doi.org/10.3390/ijerph110605807
6. Crowder, K., & Downey, L. (2010). Interneighborhood migration, race, and environmental hazards: modeling microlevel processes of environmental inequality. AJS; American journal of sociology, 115(4), 1110–1149. https://doi.org/10.1086/649576
