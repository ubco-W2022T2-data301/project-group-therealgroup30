import pandas as pd

#functions for cleaning data
def cleand(path):
    '''coverts file path to dataframe, removes null values, and sets data as necessary'''
    df = pd.read_csv(path).dropna()
    # set identifier "RegionID" as string
    df['RegionID'] = df['RegionID'].astype('str')
    # set categorical data
    df['tier'] = df['tier'].astype('category')
    df['RegionID'] = df['RegionID'].astype('category')
    df['RegionName'] = df['RegionName'].astype('category')
    return df

def isNull(df):
    '''if null values exist, generate preview of entries with null values'''
    if df.isnull().any(axis=None):
        print("\nPreview of data with null values:\nxxxxxxxxxxxxx")
        print(df[df.isnull().any(axis=1)].head(3))
        plt.show()
    else:
        print('No null values found')

def isDup(df):
    '''if duplicate values exist, generate count statistics of duplicate entries'''
    if len(df[df.duplicated()]) > 0:
        print("No. of duplicated entries: ", len(df[df.duplicated()]))
        print(df[df.duplicated(keep=False)].sort_values(by=list(df.columns)).head())
    else:
        print("No duplicated entries found")
        
#functions for processing data        
def avgOverTime(df):
    '''returns dataframe with added column which is an average of all affordability columns'''
    df['Affordability(1999-2016)'] = (df['1999-06-30'] + df['1999-09-30'] + df['1999-12-31'] + df['2000-03-31'] + df['2000-06-30'] + df['2000-09-30'] + df['2000-12-31'] + df['2001-03-31'] + df['2001-06-30'] + df['2001-09-30'] + df['2001-12-31'] + df['2002-03-31'] + df['2002-06-30'] + df['2002-09-30'] + df['2002-12-31'] + df['2003-03-31'] + df['2003-06-30'] + df['2003-09-30'] + df['2003-12-31'] + df['2004-03-31'] + df['2004-06-30'] + df['2004-09-30'] + df['2004-12-31'] + df['2005-03-31'] + df['2005-06-30'] + df['2005-09-30'] + df['2005-12-31'] + df['2006-03-31'] + df['2006-06-30'] + df['2006-09-30'] + df['2006-12-31'] + df['2007-03-31'] + df['2007-06-30'] + df['2007-09-30'] + df['2007-12-31'] + df['2008-03-31'] + df['2008-06-30'] + df['2008-09-30'] + df['2008-12-31'] + df['2009-03-31'] + df['2009-06-30'] + df['2009-09-30'] + df['2009-12-31'] + df['2010-03-31'] + df['2010-06-30'] + df['2010-09-30'] + df['2010-12-31'] + df['2011-03-31'] + df['2011-06-30'] + df['2011-09-30'] + df['2011-12-31'] + df['2012-03-31'] + df['2012-06-30'] + df['2012-09-30'] + df['2012-12-31'] + df['2013-03-31'] + df['2013-06-30'] + df['2013-09-30'] + df['2013-12-31'] + df['2014-03-31'] + df['2014-06-30'] + df['2014-09-30'] + df['2014-12-31'] + df['2015-03-31'] + df['2015-06-30'] + df['2015-09-30'] + df['2015-12-31'] + df['2016-03-31'] + df['2016-06-30']) / 69
    return df

def affByYear(df):
    '''returns data gruped by average mortgage by year'''
    #drop all categorical columns, find avg affordability for each period, restructure data, rename columns
    df = df.drop(['RegionID','tier','PopRank','RegionName', 'Affordability(1999-2016)'], axis=1).describe().drop(['count', 'std', 'min', '25%', '50%', '75%', 'max']).transpose().reset_index().rename(columns={'index': 'Year', 'mean': 'Mortgage Affordability'})
    #translate date to datetime object and extract year
    df['Year'] = pd.to_datetime(df['Year'])
    #groupby year
    df = df.groupby(df.Year.dt.year).mean().reset_index()
    return df

def affCompState(df, index):
    '''return df with added column comparing the affordability for each state to the affodability for a specified state'''
    state = str(df['RegionName'][index])
    ls = df['Affordability(1999-2016)']
    ls2 = []
    for i in ls:
        if i > ls[index]:
            ls2.append('Less Affordable')
        elif i < ls[index]:
            ls2.append('More Affordable')
        else:
            ls2.append('Same Affordability')
    df[f"Affordability Compared to {state}"] = ls2
    return df

def getGeoLoc(df):
    '''adds latitude and longitude columns'''
    lat = []
    long = []
    lat.append(32.318230) #AL
    long.append(-86.902298)
    lat.append(32.788891) #AZ
    long.append(-92.957779)
    lat.append(36.778259) #CA
    long.append(-119.417931)
    lat.append(39.550053) #CO
    long.append(-105.782066)
    lat.append(41.500751) #CT
    long.append(-72.757378)
    lat.append(38.89037) #DC
    long.append(-77.03196)
    lat.append(28.518795) #FL
    long.append(-81.44426)
    lat.append(32.648323) #GA
    long.append(-83.444534)
    lat.append(40.113937) #IL
    long.append(-89.15877)
    lat.append(37.527233) #KY
    long.append(-85.28762)
    lat.append(42.15603) #MA
    long.append(-71.5659)
    lat.append(38.952724) #MD
    long.append(-76.70125)
    lat.append(44.862617) #MI
    long.append(-85.73514)
    lat.append(46.34936) #MN
    long.append(-94.19837)
    lat.append(38.367966) #MO
    long.append(-92.47788)
    lat.append(35.539345) #NC
    long.append(-79.18542)
    lat.append(39.3564) #NV
    long.append(-116.655396)
    lat.append(42.937084) #NY
    long.append(-75.6107)
    lat.append(40.41305) #OH
    long.append(-82.71121)
    lat.append(35.459164) #OK
    long.append(-97.37394)
    lat.append(43.938812) #OR
    long.append(-120.55859)
    lat.append(40.809677) #PA
    long.append(-77.77727)
    lat.append(41.667397) #RI
    long.append(-71.58632)
    lat.append(35.860119) #TN
    long.append(-86.660156)
    lat.append(31.462734) #TX
    long.append(-99.33304)
    lat.append(39.833332) #USA
    long.append(-98.583336)
    lat.append(39.323742) #UT
    long.append(-111.67824)
    lat.append(37.51282) #VA
    long.append(-78.697945)
    lat.append(47.411293) #WA
    long.append(-120.55627)
    lat.append(44.64179) #WI
    long.append(-89.73674)
    df["Latitude"] = lat
    df["Longitude"] = long
    return df

def affCompYear(df, index):
    '''return df with added column comparing the affordability for each year to the affodability for a specified year'''
    year = str(df['Year'][index])
    ls = df['Mortgage Affordability']
    ls2 = []
    for i in ls:
        if i > ls[index]:
            ls2.append('Less Affordable')
        elif i < ls[index]:
            ls2.append('More Affordable')
        else:
            ls2.append('Same Affordability')
    df[f"Affordability Compared to {year}"] = ls2
    return df

#removing unnecessary data for analysis
def removePeriodCol(df):
    '''removes all original affordability columns - useful if only working with averages'''
    df = df.drop(['1999-06-30','1999-09-30','1999-12-31','2000-03-31','2000-06-30','2000-09-30','2000-12-31','2001-03-31','2001-06-30','2001-09-30','2001-12-31','2002-03-31','2002-06-30','2002-09-30','2002-12-31','2003-03-31','2003-06-30','2003-09-30','2003-12-31','2004-03-31','2004-06-30','2004-09-30','2004-12-31','2005-03-31','2005-06-30','2005-09-30','2005-12-31','2006-03-31','2006-06-30','2006-09-30','2006-12-31','2007-03-31','2007-06-30','2007-09-30','2007-12-31','2008-03-31','2008-06-30','2008-09-30','2008-12-31','2009-03-31','2009-06-30','2009-09-30','2009-12-31','2010-03-31','2010-06-30','2010-09-30','2010-12-31','2011-03-31','2011-06-30','2011-09-30','2011-12-31','2012-03-31','2012-06-30','2012-09-30','2012-12-31','2013-03-31','2013-06-30','2013-09-30','2013-12-31','2014-03-31','2014-06-30','2014-09-30','2014-12-31','2015-03-31','2015-06-30','2015-09-30','2015-12-31','2016-03-31','2016-06-30'], axis=1)
    return df

def gbState(df):
    '''groups data in dataframe by state and removes extra data'''
    #Isolate the state in title for clear plotting
    ls = df['RegionName'].tolist()
    ls1 = []
    for i in ls:
        if i == 'United States':
            m = 'USA'
        else: 
            m = i[-2:]
        ls1.append(m)
    df['RegionName'] = ls1
    #remove all other categorical columns and groupby regian name
    df = df.drop(['RegionID','tier'], axis=1).groupby("RegionName").mean().reset_index()
    return df

def gbPop(df):
    '''groups dataframe by population'''
    df = df.groupby('PopRank').mean().reset_index()
    return df

    