import pandas as pd
import csv
import plotly.figure_factory as pff

df=pd.read_csv("data1.csv")
fig=pff.create_distplot([df["Avg Rating"].tolist()],["Mobiles"],show_hist=False)
fig.show()