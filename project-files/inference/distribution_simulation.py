import pandas as pd
import numpy as np

# Algorithm explanation:
# we use the existing data points and random noise from the normal distribution to generate
# new fake observations. Then we can have more complete and realistic data. The parameter
# sigma controls the added noise of the new coordinates. A sigma of 0.1 leads to a 5.5 km
# standard deviation


# Make a dataframe, define new columns for northing and easting as the average of min and max
df = pd.read_excel("bears.xlsx", usecols=["Species", "WGS84 N-min", "WGS84 N-max", "WGS84 E-min", "WGS84 E-max"]).dropna()
df['WGS84 N'] = (df['WGS84 N-min'] + df['WGS84 N-max']) / 2
df['WGS84 E'] = (df['WGS84 E-min'] + df['WGS84 E-max']) / 2
df = df.drop(['WGS84 N-min', 'WGS84 N-max', 'WGS84 E-min', 'WGS84 E-max'], axis=1)

def add_new_data_points(dataframe, real_number, sigma): #Real number of species needs to be checked e.g. from Wikipedia
    #A sigma of 0.01 equals about 550 meters in latitude Finland. In longitude, it equals 1.1 kilometers.
    #We can simply use sigma / 2 in longitude to make it 550 meters as well.
    new_rows = real_number - len(dataframe)
    if new_rows <= 0:
        return dataframe 
    
    # Select real data points to make new fake observations
    selected_real_data = dataframe.sample(n=new_rows)
    
    # Add noise
    noise_lat = np.random.normal(0, sigma, new_rows)
    noise_lon = np.random.normal(0, sigma / 2, new_rows)
    
    fake_data = {
        'Species': ['fake observation'] * new_rows,
        'WGS84 N': selected_real_data['WGS84 N'] + noise_lat,
        'WGS84 E': selected_real_data['WGS84 E'] + noise_lon
    }
    fake_data_df = pd.DataFrame(fake_data)
    
    new_df = pd.concat([dataframe, fake_data_df], ignore_index=True)
    #new_df.to_excel("new_bears.xlsx", index=False) #Make an excel file, this is not necessary.
    return new_df

altered_dataframe = add_new_data_points(df, 2000, 0.1)
