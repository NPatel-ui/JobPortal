import pandas as pd
df=pd.read_csv(r"C:\Users\Nitay\Desktop\Internship\cleaned_job_descriptions.csv")
print(df.isnull().sum())

