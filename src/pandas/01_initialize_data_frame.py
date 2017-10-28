import pandas as pd
import numpy as np

#createing dataframe with
#list of countries, GDP and per capita
countries_df = pd.DataFrame([["Germany",4.150,50206],["India", 2.454, 7153], ["USA",18.558,57467]])
print(countries_df)

#Let's give logical name to columns
countries_df = pd.DataFrame([["Germany",4.150,50206],["India", 2.454, 7153], ["USA",18.558,57467]],
                            columns=("Country","GDP","Per Capita")
                            )
print(countries_df)

#Let's make country name as index
#Let's give logical name to columns
countries_df = pd.DataFrame([["Germany",4.150,50206],["India", 2.454, 7153], ["USA",18.558,57467]],
                            columns=("Country","GDP","Per Capita"),
                            index=("Germany","India","USA")
                            )
print(countries_df)

#Dataframe can be created with map also
countries_df = pd.DataFrame([{"Country":"Germany","GDP":4.150,"Per Capita":50206},
                            {"Country":"India","GDP": 2.454, "Per Capita":7153},
                            {"Country":"USA","GDP":18.558,"Per Capita":57467}
                           ])
print(countries_df)

#Dataframe with NaN values
nan_df = pd.DataFrame(np.nan, index=[0,1,2], columns=("Country","GDP","Per Capita"))
print(nan_df)

#Putting all values to 0
zero_df = pd.DataFrame(0,index=[0,1,2], columns=("Country","GDP","Per Capita"))
print(zero_df)