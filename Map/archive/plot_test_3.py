# import plotly.express as px
# px.set_mapbox_access_token(
#     "pk.eyJ1IjoiZXJhbmdyaW4iLCJhIjoiY2thanE2Mnc2MGN6aDJycGV0MHl4MXI3bCJ9.hAQ0SAX1JGgeM_9lBZtC2g")
# df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon",
#                         color="peak_hour", size="car_hours",
#                         color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
# fig.show()


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.show()