import dash
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_daq as daq
#from jupyter_dash import JupyterDash
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd



app = Dash(__name__)
server = app.server

# Create a Plotly subplot with multiple subplots
#fig = make_subplots(rows=2, cols=2, subplot_titles=('HTF_in', 'HTF_out', 'HTF_flow', 'AIR_in'))

# Define the initial traces for each subplot
# traces = []
# for i, col in enumerate(df.columns):
#     trace = go.Scatter(x=[], y=[], mode='lines', name=col)
#     fig.add_trace(trace, row=(i // 3) + 1, col=(i % 3) + 1)
#     traces.append(trace)

# Define the layout
app.layout = html.Div(
    style={'display': 'grid', 'grid-template-rows': '1fr 1fr', 'height': '100vh'},  # Use CSS grid for layout
    children=[
        html.Div(
            style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'border': '1px solid black'},  # First row with two columns
            children=[
                html.Div(
                    style={'border': '1px solid black', 'background-color': '#E3FAF7', 'padding': '10px'},  # Left column in first row
                    children=[
                        
                        

                        html.Img(src="/assets/HYPERGRYD_LOGO_RGB_Color.jpg", className="logo"),
                        html.H1('Sensors'),
                        html.Div(className="knob-container",children=[
                            daq.LEDDisplay(id="HTF_in", label="HTF_in", value=1.00),
                            daq.LEDDisplay(id="HTF_out", label="HTF_out", value=2.00),
                            daq.LEDDisplay(id="HTF_flow", label="HTF_flow", value=12.00),
                            daq.LEDDisplay(id="AIR_in", label="AIR_in", value=1.00),
                            daq.LEDDisplay(id="AIR_out", label="AIR_out", value=14.00),
                            daq.LEDDisplay(id="AIR_flow", label="AIR_flow", value=15.00),
                            daq.LEDDisplay(id="RH_in", label="RH_in", value=16.00),
                            daq.LEDDisplay(id="RH_out", label="RH_out", value=19.00),
                            daq.LEDDisplay(id="deltaP", label="deltaP", value=35.00)
                        ]),
                        
                        
                        # Add content for the left column of the first row here
                    ]
                ),
                html.Div(
                    style={'border': '1px solid black', 'background-color': 'lightgrey', 'padding': '10px'},  # Right column in first row
                    children=[
                        html.H1('Actuators'),
                        
                        daq.ToggleSwitch(
                            id="my-toggle-switch",
                            label="Automatic | Manual",
                            color="red",
                            value = True
                        ),
                        
                        daq.Knob(
                                    id="my-knob",
                                    min= 0,
                                    max=100,
                                    disabled=False,
                            
                                    label="Valves setting",
                                    scale={"start": 0, "labelInterval": 5, "interval": 5},
                                    color={
                                        "gradient": True,
                                        "ranges": {"blue": [30, 75], "red": [75, 100]},}
                            
                        
                                ),
                        
                        html.Div(
                             daq.LEDDisplay(id="my-leddisplay", value="40", color="#39FF14"),
                        )
                        # Add content for the right column of the first row here
                    ],
                    
                )
            ]
        ),
        html.Div(
            style={'border': '1px solid black','background-color': "#DDE7DB", 'padding': '10px'},  # Second row with single column
            children=[
                html.H1('Charts'),
                #fig = make_subplots(rows=1, cols=2)
                html.Div(dcc.Graph(id="my-graph", figure= {}),
                         className="row"),
                dcc.Interval(id="timing", interval=1000, n_intervals=2),
                # Add content for the bottom row here
            ]
        )
    ]
)
@app.callback(
    Output("my-leddisplay", "value"),
    Input("my-knob", "value"),
    
)
def update(knob_value):
    
    return knob_value

#in callbacko dorost kon ke ba on/off kardane manual in disable beshe
@app.callback(
    Output("my_knob","disabled"),
    Input("my-toggle-switch","value")
)
def update(Automatic):
    if Automatic:
        return disabled
    else:
        return 


@app.callback(
    Output("HTF_in", "value"),
    Output("HTF_out", "value"),
    Output("my-graph", "figure"),
    Input("timing", "n_intervals"),
) 
    

    
def update_g(n_intervals):
    pressure_1 = randrange(10)  # mimics data pulled from live database
    pressure_2 = randrange(10)  # mimics data pulled from live database

    fig = go.Figure(
        [
            go.Bar(
                x=["HTF_in"],
                y=[pressure_1],
            ),
            go.Bar(
                x=["HTF_out"],
                y=[pressure_2],
            ),
            go.Bar(
                x=["HTF_flow"],
                y=[pressure_1],
            ),
            go.Bar(
                x=["AIR_in"],
                y=[pressure_1],
            ),
            go.Bar(
                x=["AIR_out"],
                y=[pressure_1],
            ),    
            
        ]
    )
    
    fig.update_layout(yaxis={"range": [0, 20]})

    return pressure_1, pressure_2, fig

    


if __name__ == '__main__':
    app.run_server( debug=True,port =9797, mode= "inline")
