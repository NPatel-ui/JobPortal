import pandas as pd
df=pd.read_csv(r"C:\Users\Nitay\Desktop\Internship\job_descriptions.csv")
print(df.isnull().sum())
df.dropna(inplace=True)
df.isnull().sum()
df.drop_duplicates(inplace=True)
df.to_csv(“cleaned_datasets.csv”,index=false”)


