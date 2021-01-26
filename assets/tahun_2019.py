import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import datetime

url_kopi = 'https://raw.githubusercontent.com/ArgeniaP/task/main/Data%20Produksi%20Kopi%202017-2019%20Satuan%20Ton.csv'

df_kopi = pd.read_csv(url_kopi)

colors = {
    'paper_color': '#393939',
    'text': '#E1E2E5',
    'plot_color': '#ffffff',
    'confirmed_text':'#3CA4FF',
    'deaths_text':'#f44336',
    'recovered_text':'#5A9E6F',
    'highest_case_bg':'#393939'
}

divBorderStyle = {
    'backgroundColor' : '#393939',
    'borderRadius': '12px',
    'lineHeight': 0.9
}

data_kopi = df_kopi.drop()