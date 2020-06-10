# import plotly.express as px
# px.set_mapbox_access_token(open(".mapbox_token").read())
# df = px.data.carshare()
# fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon",     
#     color="peak_hour", size="car_hours",
#     color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
# fig.show()

# #import json
# import plotly.plotly as py
# import plotly.tools as tls
# import plotly.graph_objs as go

# #setup
# tls.set_credentials_file(username='erangrin', api_key='pk.eyJ1IjoiZXJhbmdyaW4iLCJhIjoiY2thanE2Mnc2MGN6aDJycGV0MHl4MXI3bCJ9.hAQ0SAX1JGgeM_9lBZtC2g')
# mapbox_access_token = “MAPBOX-KEY”

# source_red ='https://raw.githubusercontent.com/plotly/datasets/master/florida-red-data.json’
# source_blue ='https://raw.githubusercontent.com/plotly/datasets/master/florida-blue-data.json’

# data = go.Data([
# go.Scattermapbox(
# lat=[‘45.5017’],
# lon=[’-73.5673’],
# mode=‘markers’,
# )
# ])
# layout = go.Layout(
# height=600,
# autosize=True,
# hovermode=‘closest’,
# mapbox=dict(
# layers=[
# dict(
# sourcetype ='geojson’,
# source = source_red,
# type ='fill’,
# color ='rgba(163,22,19,0.8)’
# )],
# accesstoken=mapbox_access_token,
# bearing=0,
# center=dict(
# lat=27.8,
# lon=-83
# ),
# pitch=0,
# zoom=5.2,
# style=‘light’
# ),
# )

# updatemenus=list([
# dict(
# buttons=list([
# dict(
# args=[‘mapbox.layers.source’, source_red],
# label=‘red’,
# method=‘relayout’
# ),
# dict(
# args=[‘mapbox.layers.source’, source_blue],
# label=‘blue’,
# method=‘relayout’
# )
# ]),
# direction ='left’,
# pad = {‘r’: 10,'t’: 10},
# showactive = True,
# type ='buttons’,
# x = 0.1,
# xanchor ='left’,
# y = 1.1,
# yanchor ='top’
# )
# ])

# layout[‘updatemenus’] = updatemenus

# fig = dict(data=data, layout=layout)
# py.iplot(fig, filename=‘county-level-choropleths-python’)

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.express as px

fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()