from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('final_sales_data.csv')
# print(df.head())

fig = px.line(df, x='date', y='sales', color='region')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Sales of Pink Morsel Over Time',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div([dcc.Dropdown(
        options=[{'label': region, 'value': region} for region in df['region'].unique()] + ['all'],
        value='west',
        id='region-dropdown'
    )], style={'width':'25%', 'display':'inline-block'}),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

@callback(
    Output('example-graph-2', 'figure'),
    Input('region-dropdown', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    new_fig = px.line(filtered_df, x='date', y='sales', color='region')
    return new_fig

if __name__ == '__main__':
    app.run(debug=True)