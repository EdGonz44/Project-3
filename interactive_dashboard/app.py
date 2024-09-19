import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your dataset
data = pd.read_json('data.json')

#HeatMap-Pesticide imports
complete_e = pd.read_csv()
outlier_e = pd.read_csv()
q1_e = pd.read_csv()
q2_e = pd.read_csv()
q3_e = pd.read_csv()
q3_e = pd.read_csv()
q4_e = pd.read_csv()


# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("CO2 Emissions Dashboard & Correlation Analysis"),

    # Section 1: General CO2 Emissions Dashboard
    html.H2("General CO2 Emissions Dashboard"),
    
    html.Div([
        html.Label('Select Country:'),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in data['Area'].unique()],
            value='Afghanistan'
        ),
        html.Label('Select Data:'),
        dcc.Dropdown(
            id='data-dropdown',
            options=[
                {'label': 'Total Emission', 'value': 'total_emission'},
                {'label': 'Average Temperature', 'value': 'Average Temperature °C'},
                {'label': 'Manure Management', 'value': 'Manure Management'},
                {'label': 'Fertilizers Manufacturing', 'value': 'Fertilizers Manufacturing'},
                {'label': 'Rice Cultivation', 'value': 'Rice Cultivation'},
                {'label': 'Forest Fires', 'value': 'Forest fires'},
                {'label': 'Savanna Fires', 'value': 'Savanna fires'}
            ],
            value='total_emission'
        )
    ], style={'width': '45%', 'display': 'inline-block'}),

    html.Div([
        html.Label('Select Visualization Type:'),
        dcc.Dropdown(
            id='chart-dropdown',
            options=[
                {'label': 'Line Chart', 'value': 'line'},
                {'label': 'Bar Chart', 'value': 'bar'},
                {'label': 'Scatter Plot', 'value': 'scatter'},
                {'label': 'Stacked Bar Chart', 'value': 'stacked_bar'},
                {'label': 'Area Chart', 'value': 'area'}
            ],
            value='line'
        )
    ], style={'width': '45%', 'display': 'inline-block', 'padding-left': '5%'}),

    # Graph to display the general data visualizations
    dcc.Graph(id='graph'),

    # Second visualization - Scatter plot to show correlation between temperature and emissions
    dcc.Graph(id='scatter-plot'),

    # Section 2: CO2 Emissions Correlation Dashboard
    html.H2("CO2 Emissions Correlation Dashboard"),

    # First Section: CO2 Emissions vs. Forest Fires & Savanna Fires
    html.H3("CO2 Emissions vs. Forest Fires & Savanna Fires"),
    dcc.Graph(id='fires-emissions-graph'),

    # Second Section: CO2 Emissions vs. Industrial Activities (Manure Management, Fertilizer Production)
    html.H3("CO2 Emissions vs. Industrial Activities"),
    dcc.Graph(id='industry-emissions-graph'),

     
     html.Div([
        html.Label('Correlation Heatmaps/Pesticides:'),
        dff.Dropdown(
            id='correlation-heatmap-dropdown',
            options = [
                {'label':'Select Variables', 'value': 'None'},
                {'label':'World', 'value': 'world'},
                {'label': 'Outlier', 'value':'outlier'},
                {'label': 'Q1', 'value': 'q1'},
                {'label': 'Q2', 'value': 'q2'},
                {'label': 'Q3', 'value': 'q3'},
                {'label': 'Q4', 'value': 'q4'}
            ],
            value = 'world'
        ),
    ], style={'width': '45%', 'display': 'inline-block'}),
    dcc.Graph(id='correlation-pest-chart'),
    

])

# Callback to update the main general dashboard graph based on dropdown selections
@app.callback(
    Output('graph', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('data-dropdown', 'value'),
     Input('chart-dropdown', 'value')]
)
def update_graph(selected_country, selected_data, selected_chart_type):
    # Filter the data based on country selection
    filtered_data = data[data['Area'] == selected_country]

    if filtered_data.empty:
        # Fallback if no data is available
        return {
            'layout': {
                'xaxis': {'visible': False},
                'yaxis': {'visible': False},
                'annotations': [{
                    'text': 'No data available for the selected options',
                    'xref': 'paper',
                    'yref': 'paper',
                    'showarrow': False,
                    'font': {'size': 20}
                }]
            }
        }

    # Generate the figure based on the selected chart type
    if selected_chart_type == 'line':
        fig = px.line(filtered_data, x='Year', y=selected_data, title=f'{selected_data} Over Time for {selected_country}')
    elif selected_chart_type == 'bar':
        fig = px.bar(filtered_data, x='Year', y=selected_data, title=f'{selected_data} Over Time for {selected_country}')
    elif selected_chart_type == 'scatter':
        fig = px.scatter(filtered_data, x='Year', y=selected_data, title=f'{selected_data} Over Time for {selected_country}')
    elif selected_chart_type == 'stacked_bar':
        fig = px.bar(filtered_data, x='Year', y=['Manure Management', 'Fertilizers Manufacturing', 'Forest fires', 'Savanna fires'], 
                     title=f'Stacked Emissions Breakdown for {selected_country}', barmode='stack')
    elif selected_chart_type == 'area':
        fig = px.area(filtered_data, x='Year', y=['Manure Management', 'Fertilizers Manufacturing', 'Forest fires', 'Savanna fires'], 
                      title=f'Area Chart of Emissions Breakdown for {selected_country}')
    else:
        fig = {}

    return fig

# Callback for CO2 Emissions vs. Forest Fires & Savanna Fires
@app.callback(
    Output('fires-emissions-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_fires_emissions_graph(selected_country):
    filtered_data = data[data['Area'] == selected_country]
    fig = px.line(filtered_data, x='Year', 
                  y=['total_emission', 'Forest fires', 'Savanna fires'],
                  labels={'value': 'CO2 Emissions and Fires', 'variable': 'Type'},
                  title=f'CO2 Emissions vs. Forest Fires & Savanna Fires for {selected_country}')
    return fig

# Callback for CO2 Emissions vs. Industrial Activities
@app.callback(
    Output('industry-emissions-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_industry_emissions_graph(selected_country):
    filtered_data = data[data['Area'] == selected_country]
    fig = px.line(filtered_data, x='Year', 
                  y=['total_emission', 'Manure Management', 'Fertilizers Manufacturing'],
                  labels={'value': 'CO2 Emissions and Industrial Activities', 'variable': 'Type'},
                  title=f'CO2 Emissions vs. Industrial Activities for {selected_country}')
    return fig

# Callback to create a scatter plot to show correlation between temperature and total emissions
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_scatter(selected_country):
    filtered_data = data[data['Area'] == selected_country]
    fig = px.scatter(filtered_data, x='Average Temperature °C', y='total_emission',
                     title=f'Correlation between Temperature and Emissions for {selected_country}')
    return fig


#Callback for the new chart based on HeatMap correlation
@app.callback(
    Output('correlation-pest-chart', 'figure'),
    [Input('correlation-heatmap-dropdown', 'value')]
)
def update_pest_corr(selected_option):
    if selected_option =='world':
        #Creates pest-matrix based on selected metric for correlation-heatmap-dropdown
        corr_matrix_df = complete_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier'])
        corr_mat = corr_matrix_df.corr()
        # Generate a heatmap
        fig = px.imshow(corr_mat, title = 'Correlation Matrix World',
                        color_continuous_scale='RdBu',
                        zmin=-1, zmax=1)
            
    elif selected_option =='outlier':
    #Creates pest-matrix based on selected metric for correlation-heatmap-dropdown
        corr_matrix_df = outlier_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier'])
        corr_mat = corr_matrix_df.corr()
        # Generate a heatmap
        fig = px.imshow(corr_mat, title = 'Correlation Matrix Outlier',
                        color_continuous_scale='RdBu',
                        zmin=-1, zmax=1)
    elif selected_option =='q1':
    #Creates pest-matrix based on selected metric for correlation-heatmap-dropdown
        corr_matrix_df = q1_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier'])
        corr_mat = corr_matrix_df.corr()
        # Generate a heatmap
        fig = px.imshow(corr_mat, title = 'Correlation Matrix Q1',
                        color_continuous_scale='RdBu',
                        zmin=-1, zmax=1)
        
    elif selected_option =='q2':
    #Creates pest-matrix based on selected metric for correlation-heatmap-dropdown
        corr_matrix_df = q2_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier'])
        corr_mat = corr_matrix_df.corr()
        # Generate a heatmap
        fig = px.imshow(corr_mat, title = 'Correlation Matrix Q2',
                        color_continuous_scale='RdBu',
                        zmin=-1, zmax=1)
        
    elif selected_option =='q3':
    #Creates pest-matrix based on selected metric for correlation-heatmap-dropdown
        corr_matrix_df = q3_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier'])
        corr_mat = corr_matrix_df.corr()
        # Generate a heatmap
        fig = px.imshow(corr_mat, title = 'Correlation Matrix Q3',
                        color_continuous_scale='RdBu',
                        zmin=-1, zmax=1)
        
    elif selected_option =='q4':
    #Creates pest-matrix based on selected metric for correlation-heatmap-dropdown
        corr_matrix_df = q4_e.drop(columns = ['Code', 'Year', 'Country', 'Z-Score', 'Is-Outlier'])
        corr_mat = corr_matrix_df.corr()
        # Generate a heatmap
        fig = px.imshow(corr_mat, title = 'Correlation Matrix World',
                        color_continuous_scale='RdBu',
                        zmin=-1, zmax=1)
    else:
         fig = {}
    return fig




if __name__ == '__main__':
    app.run_server(debug=True)






