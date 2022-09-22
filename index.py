from statistics import mode
from turtle import title
from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/updates')
def updates():
    return render_template('updates.html')

@app.route('/reports')
def reports():

    data = pd.read_csv(r'C:\\Users\\fernando.martinez\\Documents\\PANDAS.csv', delimiter=';')

    data.sort_values(by='month', ascending=True,inplace=True)
    month = data['month']

    fig1 = make_subplots(specs=[[{"secondary_y": True}]])
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')

    fig2 = px.bar(data, x="month", y=["gmv_gross"], title="GMV")
    fig2.update_traces(marker_color="#d3ecef")

    fig1.add_trace(go.Scatter(x=month, y=data['pfd_amount'], name='pfd_amount'),secondary_y= True,)
    fig1.add_trace(go.Scatter(x=month, y=data['vfd_amount'], name='vfd_amount'),secondary_y= True,)
    fig1.add_trace(go.Scatter(x=month, y=data['tfd_amount'], name='tfd_amount'),secondary_y= True,)
    

    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)


    sheet_id = '1DK8gJYZI2fYHIZ-nRga8HUmYSHWEwqC3gCOfrxVKeKo'
    sheet_name = 'resultados'
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    df2 = pd.read_csv(url)
    df2 = df2.groupby(by=['month'],as_index=False).sum()

    # fig3 = make_subplots(specs=[[{"secondary_y": True}]])

    fig3 = go.Figure()

    fig3.add_trace(go.Scatter(x=df2['month'], y=df2['total_orders'], name="total_orders"))
    fig3.add_trace(go.Scatter(x=df2['month'], y=df2['vfd_orders'], name="vfd_orders"))
    fig3.update_layout(showlegend=True, paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',hovermode="x")
    fig3.update_traces(mode="markers+lines", hovertemplate=None)
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('reports.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON, graph3JSON=graph3JSON)

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/glossary')
def glossary():
    return render_template('glossary.html')

@app.route('/kpis')
def kpis():
    return render_template('kpis.html')

if __name__ == '__main__':
    app.run(debug=True)

