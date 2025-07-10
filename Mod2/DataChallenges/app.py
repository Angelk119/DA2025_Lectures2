import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('/Users/gabriel/Desktop/marcy/DA2025_Lectures2/Mod2/data/sports.csv')
df = df[["sports", "rev_men", "rev_women"]].dropna()

# Pick 5 sports
top5= ['Basketball', 'All Track Combined', 'Tennis', 'Golf', 'Soccer']

#Copying the dataframe to not overwrite the original 
df_5 = df[df["sports"].isin(top5)].copy()

df_5["Total_Revenue"] = df_5['rev_men'].sum() + df_5['rev_women'].sum()
print(df_5.head())

fig = px.pie(df_5, values='Total_Revenue', names='sports',
             title='Total Revenue by Sports')



app = dash.Dash(__name__)
app.title = "Sports Dashboard"

app.layout = html.Div([
    html.H1("Revenue Analysis for 5 Sports", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)