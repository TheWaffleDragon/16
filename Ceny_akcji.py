from plotly.offline import iplot
import cufflinks as cf
cf.go_offline()
import pandas as pd

import plotly.io as pio
pio.renderers.default='browser'
#pio.renderers.default = 'svg'

import plotly.graph_objects as go

import plotly.io as pio
#%%
df_kghm = pd.read_csv('kgh_d.csv')
df_price = pd.read_csv('ca_c_f_d.csv')

#%%
from plotly.subplots import make_subplots

x = df_kghm['Data']
y = df_kghm['Zamkniecie']
y2 = df_price['Zamkniecie']



fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "scatter"}],
           [{"type": "scatter"}],
           [{"type": "table"}]])




# Wykres 1
fig.add_trace(go.Scatter(x=x,y=y,name='KGHM'), row=1, col=1)

# Wykres 2
fig.add_trace(go.Scatter(x=x,y=y2,name='Miedź'), row=2, col=1)

# Tabela
fig.add_trace(
    go.Table(
        header=dict(
            values=['Data','KGHM','Miedź'],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[x,y,y2],
            align = "left")
    ),
    row=3, col=1
)

fig.update_layout(title='KGHM v Miedź')


iplot(fig)