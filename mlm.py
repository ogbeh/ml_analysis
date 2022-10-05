# %%
from itertools import count
import pandas as pd
import matplotlib.pyplot as mp
import numpy as np


df_review = pd.read_csv('IMDB Dataset.csv')
df_review

df_positive = df_review[df_review['sentiment']=='positive'][:9000]
df_negative = df_review[df_review['sentiment']=='negative'][:1000]

df_review_imb = pd.concat([df_positive, df_negative])

positive_sent_count = df_positive[df_positive['sentiment']=='positive'].count()
negative_sent_count = df_negative[df_negative['sentiment']=='negative'].count()
print(df_review_imb)

print(df_review_imb.count())

print("Total Count of Negative Sentiment->",
      negative_sent_count,
      "Total Count of Positive Sentiment->",
      positive_sent_count)


counts = df_review_imb['sentiment'].value_counts()
print(counts)

counts.plot(kind="bar", figsize=(9, 8))
mp.show()
 
#df = pd.DataFrame(data, columns=["review", "sentiment"])

# plot the dataframe
#df.plot(x="review", y='sentiment', kind="bar", figsize=(9, 8))
 
# print bar graph
#mp.show()