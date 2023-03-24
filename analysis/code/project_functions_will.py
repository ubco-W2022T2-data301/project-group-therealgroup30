import pandas as pd
#untiered mortgage affordability
def load_and_process_untieredaverage(path):
    #clean
    df = (
        pd.read_csv(path)
        .dropna(how='all')
    )
    #process
    df2 = (
        df
        .groupby('RegionName').mean(numeric_only = True)
        .sort_values('PopRank')
        .assign(Average_affordability=lambda x: x.iloc[:,4:].mean(axis=1))
        .drop(df.iloc[:, 4:], axis = 1)
        .reset_index()
    )
    return df2

def load_and_process_meltdates(path):
    #select UnitedStates data only
    df = pd.read_csv(path).iloc[:3]
    #melt data
    df2 = (
        df
        .melt(id_vars='tier', value_vars=df.columns[4:-1])
        .assign(Date=lambda x: pd.to_datetime(x['variable'], format="%Y-%m-%d"))
        .rename(columns={'value': 'Affordability'})
        .drop(columns=['variable'])
    )

    return df2
    
def tostates(df):
    state_codes = ['DC', 'AL', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    for i in state_codes:
        df.loc[df['RegionName'].str.contains(i), 'RegionName'] = i
    #group states 
    df2 = (
        df.groupby('RegionName')
        .mean(numeric_only=True)
        .drop(columns='RegionID')
        .reset_index()
    )
    return df2

def meltdates_to_tierdiff(meltdates):
    df = (  
        meltdates
        .groupby(['Date', 'tier'])
        .agg({'Affordability': 'sum'})
        .reset_index()
    )
    # Pivot the data so each tier becomes a separate column and make columns for the difference of two tiers
    df2 = (
        df.
        pivot(index='Date', columns='tier', values='Affordability')
        .assign(bottom_middle_diff = lambda x: x['Bottom Tier'] - x['Middle Tier'])
        .assign(middle_upper_diff = lambda x: x['Middle Tier'] - x['Upper Tier'])
    )

    return df2
    

def withAverageColumn(path):
    df = (
        pd.read_csv(path)
        .assign(Average_affordability=lambda x: x.iloc[:,4:].mean(axis=1))
    )
    return df