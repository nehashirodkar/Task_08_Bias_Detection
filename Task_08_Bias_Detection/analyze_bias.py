import json
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

with open("results/raw_responses.json", "r") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df["sentiment"] = df["response"].apply(lambda t: TextBlob(t).sentiment.polarity)

df.to_csv("analysis/sentiment_scores.csv", index=False)

summary = df.groupby("prompt_file")["sentiment"].mean()
print(summary)

plt.bar(summary.index, summary.values)
plt.xticks(rotation=45)
plt.title("Sentiment by Prompt")
plt.savefig("analysis/visualizations/sentiment_by_condition.png")
plt.show()
