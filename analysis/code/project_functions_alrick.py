import pandas as pd 

# function to clean the dataset for my first visualization of the affordability ratio by tier.
def loadProcessByTier(data):
    df = pd.read_csv(data)
    df2 =( 
        df.melt(id_vars=['RegionID', 'RegionName', 'PopRank', 'tier'],
        var_name='Date', value_name='Mortgage/Income ratio')
        .assign(Date=lambda x: pd.to_datetime(x['Date']))
    )
    return df2

def loadSortByRegionPop(data):
    df = pd.read_csv(data)
    df2 = (
        df.sort_values(by='PopRank')
        .assign(AverageRatio=lambda x: x.iloc[:, 4:].mean(axis=1))
        .groupby('RegionName').mean().reset_index()
        .sort_values(by='PopRank')
    )
    return df2

def loadSortByState(data):
    df = pd.read_csv(data)
    df2 = (
        df.sort_values(by='PopRank')
        .assign(AverageRatio=lambda x: x.iloc[:, 4:].mean(axis=1))
        .groupby('RegionName').mean().reset_index()
        .assign(State=lambda x: x['RegionName'].apply(lambda x: x.split(',')[-1].strip()))
        .groupby('State').mean().reset_index()
        .drop(['PopRank', 'RegionID'], axis=1)
    )
    return df2

def loadSortByStateAverage(data):
    df = pd.read_csv(data)
    df2 = (
        df.sort_values(by='PopRank')
        .assign(AverageRatio=lambda x: x.iloc[:, 4:].mean(axis=1))
        .groupby('RegionName').mean().reset_index()
        .assign(State=lambda x: x['RegionName'].apply(lambda x: x.split(',')[-1].strip()))
        .groupby('State').mean().reset_index()
        .drop(['PopRank', 'RegionID'], axis=1)
        .sort_values('AverageRatio')
    )
    return df2

def loadSortByStateLine(data):
    df = pd.read_csv(data)
    df2 = (
        df.melt(id_vars=['RegionID', 'RegionName', 'PopRank', 'tier'], var_name='Date', value_name='AffordabilityRatio')
        .assign(Date=lambda x: pd.to_datetime(x['Date']))
        .assign(State=lambda x: x['RegionName'].apply(lambda x: x.split(',')[-1].strip()))
        .groupby(['State', 'Date']).mean().reset_index()
    )
    return df2
