import pandas as pd

df = pd.read_csv("data/dataset1.csv")

df.describe().to_csv("data/summary.csv")

print("Pipeline success")
