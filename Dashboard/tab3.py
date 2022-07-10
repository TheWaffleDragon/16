import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def render_tab(df):
    
    
    layout = html.Div([html.H1('Kanały sprzedaży', style={'text-align': 'center'}),
            html.Div([dcc.Checklist(id='channel-checklist', 
            options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
            value=df['Store_type'].unique()[0],
            inline=True)]),
            html.Div([html.Div([dcc.Graph('heat-channels')]),html.Div([dcc.Graph('bar-sex-channels')]
            )]
            )]
            )

    return layout