import plotly.express as px
px.set_mapbox_access_token("pk.eyJ1IjoiZXJhbmdyaW4iLCJhIjoiY2thanE2Mnc2MGN6aDJycGV0MHl4MXI3bCJ9.hAQ0SAX1JGgeM_9lBZtC2g")
df = px.data.carshare()
print(df)
fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon",     
    color="peak_hour", size="car_hours",
    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
fig.show()

