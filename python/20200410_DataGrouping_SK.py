# -*- coding: utf-8 -*-
import pandas as pd

df = pd.DataFrame({"Week":["A","A","B","B","C","C"],
                   "Day":["Monday","Friday","Monday","Friday","Monday","Friday"],
                   "Coffees Consumed":[5,1,4,2,3,1],
                   "Hours of Sleep":[8,7,10,7,4,12]})

grouped_data = df.groupby("Day").agg({"Coffees Consumed" : ["mean","min","max"]})
print(grouped_data)
