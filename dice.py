import random
import plotly.express as ps
import plotly.figure_factory as pff
count=[]
diceResult=[]
for i in range(0,100):
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        diceResult.append(dice1+dice2)
        count.append(i)

fig=pff.create_distplot([diceResult],["output"],show_hist=False)
fig.show()
##print(dice1,dice2)