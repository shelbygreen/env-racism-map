#  Export attributes for regions

# libraries
import pandas as pd # dataframe manipulation
import requests # api requests
import addfips # dictionary for state FIPS codes 
import geopandas as gpd # geodataframe manipulation
import numpy as np # calculations
from sodapy import Socrata # api requests
import pymongo # mongodb 
from pymongo import MongoClient # mongodb
import yaml # handles credentials

# If QA is True, save a copy of the dataframe as a CSV file for review
QA = False

# read YAML file
yaml_file = open('./keys.yaml')
parsed_yaml = yaml.load(yaml_file, Loader=yaml.FullLoader)

# ----- POPULATION CHARACTERISTICS SCORE -----
# TODO: add tract level 

# get pop. char. indicators
def county_data_for_population_score(st, yr):
    """
    Returns a dataframe containing the 8 pop. char. 
    indicators for each county in the defined state.

    st = abbrevation for state of interest (TX, FL, ...) - string
    yr = end year of interst for the ACS 5-year estimates - integer
    """

    # acs requests
    host, dataset = 'https://api.census.gov/data', 'acs/acs5'
    year = str(yr) # convert year to string
    # pop. char. indicators - refer to documentation for more info
    variables = ["B03002_001E", "B03002_003E", "B17001_001E", "B17001_002E",
              "B16010_001E", "B16010_002E",
              "B01001_001E", "B01001_003E", "B01001_004E", "B01001_027E",
              "B01001_028E", "B01001_020E", "B01001_021E", "B01001_022E",
              "B01001_023E", "B01001_024E", "B01001_025E", "B01001_044E",
              "B01001_045E", "B01001_046E", "B01001_047E", "B01001_048E",
              "B01001_049E", "B25070_001E", "B25070_007E", "B25070_008E",
              "B25070_009E", "B25070_010E", "B25070_011E"]
    # variable names for the pop. char. indicators
    col_names = ["name", "tpop_race", "tpop_nhwhite", "tpop_poverty", "tpop_impoverished", 
                "tpop_education", "tpop_lthsgraduate", "tpop_age", "tpop_lt5M",
                "tpop_5to9M", "tpop_lt5F", "tpop_5to9F", "tpop_65to66M", "tpop_67to69M", "tpop70to74M",
                "tpop_75to79M", "tpop_80to84M", "tpop_over85M", "tpop_65to66F", "tpop_67to69F", "tpop70to74F",
                "tpop_75to79F", "tpop_80to84F", "tpop_over85F", "tpop_incomeonhousing", "tpop_30to34.9IonH",
                "tpop_35to39.9IonH", "tpop_40to49.9IonH", "tpop_over50IonH", "tpop_NAIonH", "state",
                "county"]
    # loop through the variables for defined state and year
    # store results in a dataframe
    for variable in variables:
        print("Fetching data for {} variable".format(variable))
        url = "/".join([host, year, dataset])
        get_vars = ["NAME"] + variables
        predicates = {}
        predicates["get"] = ",".join(get_vars)
        predicates["for"] = "county:*"
        predicates["in"] = "state:" + addfips.AddFIPS().get_state_fips(st)
        r = requests.get(url, params=predicates)
        df = pd.DataFrame(columns = col_names, data = r.json()[1:])
    #create column of census tract names
    name_information = df.name
    #modify the dataframe to remove the name column and format values as integers
    df = df[df.columns[~df.columns.isin(['name'])]].astype(int)
    # create dataframe from the retrieved data
    indicators_df = pd.DataFrame()
    # do the calculations for each indicator and store it in the newly made dataframe
    indicators_df = indicators_df.assign(
        name = name_information.apply(lambda x: x.split(',')[0]),
        population = df.tpop_race,
        nwpopulation = df.tpop_nhwhite,
        nwpopulation_p = 100*(df.tpop_nhwhite/df.tpop_race),
        poverty = df.tpop_impoverished,
        poverty_p = 100*(df.tpop_impoverished/df.tpop_poverty),
        educational_attainment_p = 100*(df.tpop_lthsgraduate/df.tpop_education),
        age_0to9 = df.tpop_lt5M+df.tpop_5to9M+df.tpop_lt5F+df.tpop_5to9F,
        age_0to9_p = 100*((df.tpop_lt5M+df.tpop_5to9M+df.tpop_lt5F+df.tpop_5to9F)/df.tpop_age),
        age_10to64 = df.tpop_age - (df.tpop_lt5M+df.tpop_5to9M+df.tpop_lt5F+df.tpop_5to9F) - (df.tpop_65to66M+df.tpop_67to69M+df.tpop70to74M+df.tpop_75to79M
        +df.tpop_80to84M+df.tpop_over85M+df.tpop_65to66F+df.tpop_67to69F
        +df.tpop70to74F+df.tpop_75to79F+df.tpop_80to84F+df.tpop_over85F),
        age_10to64_p = 100*((df.tpop_age - (df.tpop_lt5M+df.tpop_5to9M+df.tpop_lt5F+df.tpop_5to9F) - (df.tpop_65to66M+df.tpop_67to69M+df.tpop70to74M+df.tpop_75to79M
        +df.tpop_80to84M+df.tpop_over85M+df.tpop_65to66F+df.tpop_67to69F
        +df.tpop70to74F+df.tpop_75to79F+df.tpop_80to84F+df.tpop_over85F))/(df.tpop_age)),
        age_65 = df.tpop_65to66M+df.tpop_67to69M+df.tpop70to74M+df.tpop_75to79M
        +df.tpop_80to84M+df.tpop_over85M+df.tpop_65to66F+df.tpop_67to69F
        +df.tpop70to74F+df.tpop_75to79F+df.tpop_80to84F+df.tpop_over85F,
        age_65_p = 100*((df.tpop_65to66M+df.tpop_67to69M+df.tpop70to74M+df.tpop_75to79M
        +df.tpop_80to84M+df.tpop_over85M+df.tpop_65to66F+df.tpop_67to69F
        +df.tpop70to74F+df.tpop_75to79F+df.tpop_80to84F+df.tpop_over85F)/df.tpop_age),
        housing_burden_p = 100*((df["tpop_30to34.9IonH"]+df["tpop_35to39.9IonH"]+df["tpop_40to49.9IonH"]
            +df["tpop_over50IonH"])/(df.tpop_incomeonhousing-df.tpop_NAIonH)),
        county = df.county)
    #add health data to the indicators dataframe 
    #this is for TX only. from the TX DSHS
    if st == 'TX':
        TX_health_indicators_df = pd.read_csv('./raw_data/TX_health_indicators.csv').rename(index=str, columns={'county': 'name'})

        indicators_df = indicators_df.merge(TX_health_indicators_df[['name','low_birth_weight','cardiovascular_disease']], how='left', on="name")
        
    del df, TX_health_indicators_df

    # save as dataframe and/or CSV file
    if QA:
        indicators_df.to_csv('county_population_df.csv', index=False)
        return indicators_df
    else:
        return indicators_df

# add geographic data to the dataframe
def add_geodata_to_dataframe(ut, st, ogdf):
    """
    Returns modified dataframe with geodata added

    ut = unit of data (tract or county) - string
    st = abbreviation for state of interest - string
    ogdf = dataframe that will be modified - dataframe
    """

    # filter shapefile by state and add it to the dataframe 
    # for tract level
    if ut == "tract":
        print("Fetching geographic {} data".format(ut))
        # read in shp file
        if st == 'TX':
            tempdf = gpd.read_file("./boundary_data/tl_2018_48_tract/tl_2018_48_tract.shp")[['GEOID','geometry']]
        else:
            tempdf = gpd.read_file("./boundary_data/usatracts/usa_tracts.shp")[['STATEFP','GEOID','geometry']]
            tempdf = tempdf.rename(index=str, columns={'STATEFP': 'state'})
        # filter shp file based on state
        tempdf = tempdf[tempdf['state'] == addfips.AddFIPS().get_state_fips(st)]
        # add geodata
        print("Adding geographic {} data to the dataframe".format(ut))
        geo_dataframe = tempdf.merge(ogdf, how='left', on='geoid')
    # for county level
    elif ut == "county":
        print("Fetching geographic {} data".format(ut))
        # read in shp file
        tempdf = gpd.read_file("./boundary_data/tl_2019_us_county/tl_2019_us_county.shp")[['STATEFP','COUNTYFP', 'GEOID', 'geometry']]
        tempdf = tempdf.rename(index=str, columns={'STATEFP': 'state', 'COUNTYFP':'county'})
        # fiter shp file based on state 
        tempdf = tempdf[tempdf['state'] == addfips.AddFIPS().get_state_fips(st)]
        tempdf['county'] = tempdf['county'].astype(int)
        # add geodata
        print("Adding geographic {} data to the dataframe".format(ut))
        geo_dataframe = tempdf.merge(ogdf, how='left', on='county')
    # unit is not clearly defined or unavailable
    else:
        print("Please check 'ut' input to make sure it is either 'tract' or 'county', not {}".format(ut))

    del tempdf

    # save as dataframe and/or CSV file
    if QA:
        geo_dataframe.to_csv('geocounty_population_df.csv', index=False)
        return geo_dataframe
    else:
        return geo_dataframe

# calculate county population score and export geojson
def county_calculate_population_score(ogdf):
    """
    Returns modified geodataframe containing a column of the population score

    ogdf - dataframe of interest - geodataframe
    """

    # create new dataframe
    df = pd.DataFrame()
    # add indicator percentiles
    df = df.assign(
        nwpopulation_percentile = 100*ogdf.nwpopulation.rank(pct=True),
        poverty_percentile = 100*ogdf.poverty.rank(pct=True),
        edu_percentile = 100*ogdf["educational_attainment_p"].rank(pct=True),
        age0to9_percentile = 100*ogdf.age_0to9_p.rank(pct=True),
        age65_percentile = 100*ogdf.age_65_p.rank(pct=True),
        housingburden_percentile = 100*ogdf["housing_burden_p"].rank(pct=True),
        lbw_percentile = 100*ogdf["low_birth_weight"].rank(pct=True),
        cardio_percentile = 100*ogdf["cardiovascular_disease"].rank(pct=True) 
    )
    # averaged the percentiles
    df["averaged_percentiles"] = (df.fillna(0)["nwpopulation_percentile"] + df.fillna(0)["poverty_percentile"] +  
                            df.fillna(0)["edu_percentile"] + df.fillna(0)["age0to9_percentile"] +
                            df.fillna(0)["age65_percentile"] + df.fillna(0)["housingburden_percentile"]
                            + df.fillna(0)["lbw_percentile"] + df.fillna(0)["cardio_percentile"])/8
    # calculate the population score
    df["score"] = 10*df["averaged_percentiles"]/df['averaged_percentiles'].max()
    # add the population score to the original dataframe
    ogdf["score"] = df["score"].round(2)

    del df 
    # save as dataframe and/or CSV file
    if QA:
       ogdf.to_csv('county_population_score.csv', index=False)
       return ogdf
    else:
        return ogdf

# ----- POLLUTION BURDEN SCORE -----
# TODO: add tract level 

# get daily ozone concentrations
def get_ozone_data(yr, st):
  """
  Get ozone data from the CDC API
  
  yr - year of interest - string
  st - fips code for the state of interest - string
  """

  #establish connection to the CDC's data via Socrata
  client = Socrata("data.cdc.gov", parsed_yaml['cdc_key'], parsed_yaml['cdc_username'], parsed_yaml['cdc_password'])

  #set timeout to 60 seconds
  client.timeout = 60

  #get number of records in the dataset
  record_count = client.get(
        "kmf5-t9yc",
        where=f"year2 = '{yr}' AND statefips = '{st}'",
        select="COUNT(*)"
  )

  print("The record count is", record_count)
  print("Getting data from the Socrata API...")

  #get data from dataset
  start = 0 #start at page 0
  chunk_size = 50000 #fetch 50,000 rows at a time
  results = [] #empty list to store data
  while True:
    #add data to the list
    results.extend(client.get(
          "kmf5-t9yc",
          where=f"year2 = '{yr}' AND statefips = '{st}'", # SQL query
          select="year2, month, countyfips, o3_max_pred", # interested columns
          offset=start,
          limit=chunk_size
    ))
    #pagination
    start = start + chunk_size
    print("At record number", start)
    #stop adding to the list once all the data is fetched
    if (start > int(record_count[0]['COUNT'])):
      break

  #return list so that it can be stored in a dataframe
  return results

# calculate mean ozone concentration
def get_ozone_values():
    """
    Return a dataframe of the mean ozone concentration for the summer
    months for a 3-year period
    """
    print("Calculating mean ozone values")
    #list of years of interest
    years_list = ['2012', '2013', '2014']

    #create an empty dataframe that will store the results
    results_df = pd.DataFrame()

    #fetch results and store in the dataframe
    for year in years_list:
        fetched_data = get_ozone_data(year, '48')
        temp_df = pd.DataFrame.from_records(fetched_data)
        results_df = results_df.append(temp_df)

    #filter months column to only keep summer months (MAY-OCT)
    summer_months = ['MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT']
    summer_results_df = results_df.loc[results_df['month'].isin(summer_months)].reset_index(drop=True)

    #convert datatypes
    summer_results_df["year2"] = pd.to_datetime(summer_results_df['year2'])
    summer_results_df['o3_max_pred'] = summer_results_df['o3_max_pred'].astype(float)
    summer_results_df["countyfips"] = '48' + summer_results_df["countyfips"].str.zfill(3)
    summer_results_df['countyfips'] = summer_results_df['countyfips'].astype(int)

    # calculate annual summer mean ozone concentrations
    annual_county_ozone = summer_results_df.set_index('year2').groupby('countyfips')['o3_max_pred'].resample('A').mean()

    # calculate 3Y summer mean ozone concentrations
    period_county_ozone = annual_county_ozone.reset_index().groupby('countyfips').mean()

    # order the ozone concentration values and assign a percentile based on the distribution
    period_county_ozone = period_county_ozone.assign(ozone_percentile = 100*period_county_ozone["o3_max_pred"].rank(pct=True))
    
    # save as dataframe and/or CSV file
    if QA:
       period_county_ozone.to_csv('county_ozone.csv', index=False)
       return period_county_ozone
    else:
        return period_county_ozone

# get daily pm2.5 concentrations
def get_pm25_data(yr, st):
    """
    Get pm2.5 data from the CDC API
  
    yr - year of interest - string
    st - fips code for the state of interest - string
    """
    #establish connection to the CDC's data via Socrata
    client = Socrata("data.cdc.gov", parsed_yaml['cdc_key'], parsed_yaml['cdc_username'], parsed_yaml['cdc_password'])

    #set timeout to 200 seconds
    client.timeout = 300

    #get number of records in the dataset
    record_count = client.get(
            "qjju-smys",
            where=f"year = '{yr}' AND statefips = '{st}'",
            select="COUNT(*)"
    )

    print("The record count is", record_count)
    print(f"Getting {yr} data from the Socrata API...")

    #get data from dataset
    start = 0 #starting at page 0
    chunk_size = 50000 #fetching 50,000 rows at a time
    results = [] #empty list to store data
    while True:
        #add data to the list
        results.extend(client.get(
            "qjju-smys",
            where=f"year = '{yr}' AND statefips = '{st}'",
            select="year, date, countyfips, pm_mean_pred",
            offset=start,
            limit=chunk_size
        ))
        #pagination
        start = start + chunk_size
        print("At record number", start)
        #stop adding to the list once all the data is fetched
        if (start > int(record_count[0]['COUNT'])):
            break

    #return list so that it can be stored in a dataframe
    return results

# calculate mean pm2.5 concentration 
def get_pm25_values():
    """
    Return a dataframe of the mean ozone concentration for the summer
    months for a 3-year period
    """
    print("Calculating mean pm2.5 values")
    #list of years of interest
    years_list = ['2012', '2013', '2014']

    #create an empty dataframe that will store the results
    results_df = pd.DataFrame()

    #fetch results and store in the dataframe
    for year in years_list:
        fetched_data = get_pm25_data(year, '48')
        temp_df = pd.DataFrame.from_records(fetched_data)
        results_df = results_df.append(temp_df)

    #convert datatypes
    results_df["date"] = pd.to_datetime(results_df['date'])
    results_df['pm_mean_pred'] = results_df['pm_mean_pred'].astype(float)
    results_df["countyfips"] = results_df["countyfips"]
    results_df['countyfips'] = results_df['countyfips'].astype(int)

    #calculate average quaterly estimates by county
    quarter_county_pm = results_df.set_index('date').groupby('countyfips')['pm_mean_pred'].resample('Q').mean()

    #calculate average of the quarterly estimates for the three-year period
    period_county_pm25 = quarter_county_pm.reset_index().groupby('countyfips').mean()

    #order the pm2.5 concentration values and assign a percentile based on the distribution
    period_county_pm25 = period_county_pm25.assign(pm_percentile = 100*period_county_pm25["pm_mean_pred"].rank(pct=True))

    # save as dataframe and/or CSV file
    if QA:
       period_county_pm25.to_csv('county_pm25.csv', index=False)
       return period_county_pm25
    else:
        return period_county_pm25

# get TRI facilities within the region
def get_TRI_facilities():
    """
    Selecting TRI facilities within a region
    via PIP query
    """
    print("Getting TRI facilities counts")
    #import pre-filtered, TX TRI facilities 
    #TODO: switch to US TRI Facilities 
    df = pd.read_csv('./raw_data/TX_TRI.csv')

    # only show results from 2011 to 2013
    df = df[(df["V_TRI_FORM_R_EZ.REPORTING_YEAR"] > 2010) & (df["V_TRI_FORM_R_EZ.REPORTING_YEAR"] < 2014)].reset_index(drop=True)

    #change datatype and case
    df["TRI_FACILITY.FACILITY_NAME"] = df["TRI_FACILITY.FACILITY_NAME"].str.title()
    df["TRI_FACILITY.STREET_ADDRESS"] = df["TRI_FACILITY.STREET_ADDRESS"].str.title()
    df["TRI_FACILITY.COUNTY_NAME"] = df["TRI_FACILITY.COUNTY_NAME"].str.title()
    df["TRI_FACILITY.PARENT_CO_NAME"] = df["TRI_FACILITY.PARENT_CO_NAME"].str.title()
    df["V_TRI_FORM_R_EZ.REPORTING_YEAR"] = df["V_TRI_FORM_R_EZ.REPORTING_YEAR"].astype(int)
    df["V_TRI_FORM_R_EZ.CHEM_NAME"] = df["V_TRI_FORM_R_EZ.CHEM_NAME"].str.title()
    df["V_TRI_FORM_R_EZ.AIR_TOTAL_RELEASE"] = df["V_TRI_FORM_R_EZ.AIR_TOTAL_RELEASE"].astype(float)
    df["V_TRI_FORM_R_EZ.FUGITIVE_TOT_REL"] = df["V_TRI_FORM_R_EZ.FUGITIVE_TOT_REL"].astype(float)

    #modify df to sum the release amounts for years 2011-2013
    TX_TRI_df = df.set_index('V_TRI_FORM_R_EZ.REPORTING_YEAR').groupby(['TRI_FACILITY.TRI_FACILITY_ID','TRI_FACILITY.FACILITY_NAME','TRI_FACILITY.STREET_ADDRESS','TRI_FACILITY.COUNTY_NAME','TRI_FACILITY.PARENT_CO_NAME','V_TRI_FACILITY_EZ.LATITUDE','V_TRI_FACILITY_EZ.LONGITUDE'])[['V_TRI_FORM_R_EZ.AIR_TOTAL_RELEASE','V_TRI_FORM_R_EZ.FUGITIVE_TOT_REL']].sum().reset_index()

    #import shapefile of the counties
    county_shp = gpd.read_file('./boundary_data/tl_2019_us_county/tl_2019_us_county.shp').drop(columns=['MTFCC','FUNCSTAT', 'INTPTLAT', 'INTPTLON', 'CLASSFP', 'CSAFP', 'CBSAFP', 'METDIVFP'])
    # filter based on state
    # TODO: update code to be able to filter any state
    county_shp = county_shp[county_shp["STATEFP"] == '48'].reset_index()

    #convert pandas dataframe to geopandas dataframe
    sites_gdf = gpd.GeoDataFrame(TX_TRI_df, geometry=gpd.points_from_xy(TX_TRI_df["V_TRI_FACILITY_EZ.LONGITUDE"], TX_TRI_df["V_TRI_FACILITY_EZ.LATITUDE"]))

    #create an empty dataframe that will store the results
    TX_TRI_county_df = gpd.GeoDataFrame(columns=['GEOID','TRIcount'])

    #list of interested tracts and counties
    county_list = [i for i in county_shp["GEOID"]]

    #PIP query and exports returned list as a dataframe
    for i in county_list:
        counties = county_shp.loc[county_shp['GEOID'] == i].reset_index(drop=True)
        pip_mask = sites_gdf.within(counties.loc[0, 'geometry'])
        pip_data = sites_gdf.loc[pip_mask]
        #create list of sites per geoid
        number_of_sites = len(pip_data)
        print(f"{i} has {number_of_sites} sites")
        TX_TRI_county_df = TX_TRI_county_df.append({'GEOID': i, 'TRIcount': number_of_sites}, ignore_index=True)
        print(f"Exported list of sites in {i} to the dataframe")

    #order the counts per geoid and assign a percentile based on the distribution
    TX_TRI_county_df = TX_TRI_county_df.assign(TRIcount_percentile = 100*TX_TRI_county_df["TRIcount"].rank(pct=True))

    #add geographic details to the dataframe 
    TX_TRI_county_df = TX_TRI_county_df.merge(county_shp, on='GEOID', how='right')

    #remove unnecessary columns from the dataframe
    TX_TRI_county_df = TX_TRI_county_df.drop(columns=['index', 'STATEFP','COUNTYFP','COUNTYNS','LSAD'])

    #set GEOID as the index 
    TX_TRI_county_df = TX_TRI_county_df.set_index('GEOID')

    # add geographic bounds
    bounds = pd.Series(
        TX_TRI_county_df.geometry.envelope.set_crs(epsg=4326, inplace=True)
        .bounds.round(2)
        .apply(lambda row: list(row), axis=1),
        name="bounds")
        
    TX_TRI_county_df = (pd.DataFrame(TX_TRI_county_df.drop(columns=["geometry"])).join(bounds))

    # save as dataframe and/or CSV file
    if QA:
       TX_TRI_county_df.to_csv('TX_TRI_county.csv', index=False)
       return TX_TRI_county_df
    else:
        return TX_TRI_county_df

# get SF facilities within the region
def get_SF_facilities():
    """
    Selecting SF facilities within a region
    via PIP query
    """
    print("Getting SF facilities counts")
    #import pre-filtered, TX TRI facilities 
    #TODO: switch to US TRI Facilities 
    SF_df = pd.read_csv('./raw_data/TX_SFsites.csv')[['SEMS EPA ID', 'SITE NAME', 'ADDRESS', 'COUNTY', 'LATITUDE/LONGITUDE']]

    #formatting
    SF_df['SITE NAME'] = SF_df['SITE NAME'].str.title()
    SF_df['ADDRESS'] = SF_df['ADDRESS'].str.title()
    SF_df['COUNTY'] = SF_df['COUNTY'].str.title()
    SF_df['LATITUDE'] = SF_df['LATITUDE/LONGITUDE'].apply(lambda x: x.split(': ')[-1])
    SF_df['LONGITUDE'] = SF_df['LATITUDE/LONGITUDE'].apply(lambda x: x.split(': ')[1].split('L')[0])
    SF_df = SF_df.drop(columns='LATITUDE/LONGITUDE')

    #import shapefile of the counties
    county_shp = gpd.read_file('./boundary_data/tl_2019_us_county/tl_2019_us_county.shp').drop(columns=['MTFCC','FUNCSTAT', 'INTPTLAT', 'INTPTLON', 'CLASSFP', 'CSAFP', 'CBSAFP', 'METDIVFP'])
    # filter based on state
    # TODO: update code to be able to filter any state
    county_shp = county_shp[county_shp["STATEFP"] == '48'].reset_index()

    #convert pandas dataframe to geopandas dataframe
    sites_gdf = gpd.GeoDataFrame(SF_df, geometry=gpd.points_from_xy(SF_df.LONGITUDE, SF_df.LATITUDE))

    #create an empty dataframe that will store the results
    TX_SF_county_df = pd.DataFrame(columns=['COUNTY','SFcount'])

    #list of interested counties
    county_list = [i for i in county_shp["NAME"]]

    #PIP query and exports returned list as a dataframe
    for i in county_list:
        pip_data = sites_gdf.loc[sites_gdf["COUNTY"] == i]
        number_of_sites = len(pip_data)
        print(f"{i} has {number_of_sites} sites")
        TX_SF_county_df = TX_SF_county_df.append({'COUNTY': i, 'SFcount': number_of_sites}, ignore_index=True)
        print(f"Exported list of sites in {i} to the dataframe")

    #order the counts per geoid and assign a percentile based on the distribution
    TX_SF_county_df = TX_SF_county_df.assign(SFcount_percentile = 100*TX_SF_county_df["SFcount"].rank(pct=True))

    #add geographic details to the dataframe 
    TX_SF_county_df = TX_SF_county_df.merge(county_shp, left_on='COUNTY', right_on='NAME', how='right')

    #drop the unnecessary columns
    TX_SF_county_df = TX_SF_county_df.drop(columns=['COUNTY', 'STATEFP','COUNTYFP','COUNTYNS','LSAD'])

    #set index to GEOID
    TX_SF_county_df = TX_SF_county_df.set_index('GEOID')

    # save as dataframe and/or CSV file
    if QA:
       TX_SF_county_df.to_csv('TX_TRI_county.csv', index=False)
       return TX_SF_county_df
    else:
        return TX_SF_county_df

# calculate the pollution burden score
def county_calculate_pollution_score(ozone_df, pm25_df, TRI_df, SF_df):
    """
    Return a dataframe or CSV of the pollution burden score

    ozone_df - dataframe of the ozone values - dataframe
    pm25_df - dataframe of the pm2.5 values - dataframe
    TRI_df - dataframe of the TRI counts - dataframe
    SF_df - dataframe of the SF counes - dataframe
    """

    # join the pollutants into 1 dataframe
    pollutants_df = pd.merge(ozone_df, pm25_df, on='countyfips', how='left')
    # rename the index
    pollutants_df.index.names = ['GEOID']
    # drop the index 
    pollutants_df = pollutants_df.reset_index()

    # join the facilities into 1 dataframe
    facilities_df = pd.merge(TRI_df, SF_df[['SFcount', 'SFcount_percentile']], on='GEOID', how='left')
    # rename the index
    facilities_df = facilities_df.reset_index()
    # drop the index
    facilities_df["GEOID"] = pd.to_numeric(facilities_df["GEOID"])

    # join the pollutants and facilities dataframe 
    county_pollution = pollutants_df.merge(facilities_df, on='GEOID')

    # create averaged percentiles column
    county_pollution["averaged_percentiles"] = (county_pollution["ozone_percentile"] + county_pollution["pm_percentile"] + county_pollution["TRIcount_percentile"] + county_pollution["SFcount_percentile"])/4

    # create score column
    county_pollution["score"] = (10*county_pollution["averaged_percentiles"]/county_pollution['averaged_percentiles'].max()).round(2)

    # save as dataframe and/or CSV file
    if QA:
       county_pollution.to_csv('county_pollution_score.csv', index=False)
       return county_pollution
    else:
        return county_pollution

# ----- CUMULATIVE RISK SCORE -----
# TODO: add tract level

# calculate the cumulative risk score
def county_calculate_cumulative_score(population_df, pollution_df):
    """
    Returns json + geojson 
    json - id, bounds, name, all population indicators, all pollution indicators, + cumulative score
    geojson - id, bounds, name, population score, polluation score, + cumulative score 

    population_df - dataframe from county_calculate_population_score() - dataframe
    pollution_df - dataframe from county_calculate_pollution_score() - dataframe
    """
    print("Calculating cumulative score")
    # convert GEOID to int64
    population_df["GEOID"] = pd.to_numeric(population_df["GEOID"])

    #merge the two dataframes
    county_cumulative_score = population_df.merge(pollution_df, on='GEOID')

    #create cumulative risk score column
    county_cumulative_score["cmlscore"] = (county_cumulative_score["score_x"]*county_cumulative_score["score_y"]).round(2)

    print("Cleaning")
    county_cumulative_score.to_csv('county_cumulative_score.csv')

    # dropping columns
    county_cumulative_score = county_cumulative_score.drop(columns=['ozone_percentile', 'pm_percentile', 'TRIcount_percentile', 'NAME', 'NAMELSAD', 'SFcount_percentile', 'averaged_percentiles'])
    
    # renaming columns
    county_cumulative_score = county_cumulative_score.rename(columns={'GEOID':'id', 'score_x':'population_score', 'score_y':'pollution_score', 'ALAND':'landarea', 'AWATER':'waterarea'})
    
    # round all to 2 decimal places
    county_cumulative_score = county_cumulative_score.applymap(lambda x: round(x, 1) if isinstance(x, (int, float)) else x)
    
    # ID must be a string to work in graphql, we will convert back to an integer on frontend
    county_cumulative_score["id"] = county_cumulative_score['id'].astype("str")
    
    # convert NaN to None
    county_cumulative_score = county_cumulative_score.replace({np.nan: None})

    # drop index
    
    
    # export to GEOJSON
    print("Exporting to geojson")
    county_cumulative_score.to_file("geocounty_cumulative_score.geojson", driver="GeoJSON")
    
    # export to JSON
    print("Exporting to json")
    county_cumulative_score = county_cumulative_score.drop(columns=['geometry'])

    with open("county_cumulative_score.json", "w") as outfile:
        outfile.write(json.dumps([row.to_dict() for index, row in county_cumulative_score.iterrows()]))
    

# export data
if __name__ == "__main__":
    # compute county population characteristics score 
    county_population = county_data_for_population_score('TX', 2018)
    geo_county_population = add_geodata_to_dataframe('county', 'TX', county_population)
    county_population_score = county_calculate_population_score(geo_county_population)

    # compute county pollution burden score 
    county_ozone = get_ozone_values()
    county_pm25 = get_pm25_values()
    county_TRI = get_TRI_facilities()
    county_SF = get_SF_facilities()
    county_pollution_score = county_calculate_pollution_score(county_ozone, county_pm25, county_TRI, county_SF)

    # compute cumulative score
    county_calculate_cumulative_score(county_population_score, county_pollution_score)
