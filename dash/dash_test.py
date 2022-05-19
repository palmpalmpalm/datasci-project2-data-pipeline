from distutils.log import debug
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import requests


df_all = pd.DataFrame(columns=['earthnull_station_id', 'earthnull_station_name', 'earthnull_province', 'earthnull_long', 'earthnull_pm10', 'earthnull_wind_speed',
                      'earthnull_timestamp', 'earthnull_id', 'earthnull_region', 'earthnull_lat', 'earthnull_pm25', 'earthnull_wind_dir', 'earthnull_RH'])
for i in range(1, 6):
    url = 'http://localhost:8000/earthnull/all-by-station/'+str(i)
    # print(url)
    req = requests.get(url=url)
    df = pd.DataFrame(req.json())
    # print(df)
    df_all = pd.concat([df_all, df], join="inner")

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children=' '),
    dcc.Dropdown(id='dropdown',
                 options=[{'label': i, 'value': i}
                          for i in df_all['earthnull_station_id'].unique()], value='1'),
    dcc.Graph(id='graph')
])


@app.callback(
    Output(component_id='graph', component_property='figure'),
    Input(component_id='dropdown', component_property='value')
)
def update_graph(selected_city):
    filtered_city = df_all[df_all['earthnull_station_id'] == selected_city]
    line_fig = px.line(
        filtered_city, x='earthnull_timestamp', y='earthnull_pm25')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)
