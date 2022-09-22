import pandas as pd
import plotly
import plotly.express as px
from datetime import datetime



sheet_id = '1DK8gJYZI2fYHIZ-nRga8HUmYSHWEwqC3gCOfrxVKeKo'
sheet_name = 'resultados'
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

df2 = pd.read_csv(url)

df2 = df2.groupby(by=['month'],as_index=False).sum()

print(df2.head())

# data = pd.read_csv(r'C:\\Users\\fernando.martinez\\Documents\\PANDAS.csv', delimiter=';')


# # graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)


# from datetime import datetime
# def convert_datetime(dt):
#     return datetime.strftime(dt, '%m-%Y')

# data['month'] = data['month'].apply(convert_datetime)


# print(pd.DataFrame(data))