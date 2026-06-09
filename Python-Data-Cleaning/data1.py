import pandas as pd
df=pd.read_csv(r"C:\Users\acer\Downloads\titanic.csv")
print(df)
print(df.head())


#duplicate check

print(df.duplicated().sum())
# no duplicates
#df1=df.drop_duplicates()
#print(df1)

#null check
print(df.isnull().sum())
print(df["Age"].skew())

print(df["Age"].median())
df["Age"]=df["Age"].fillna(28)

print(df.isnull().sum())

print(df.info())



#outlires
columns=df.select_dtypes(include=["int64","float64"]).columns
print(columns)


column=['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
for col in column:
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr=q3-q1
    lower_bound=q1-1.5*iqr
    upper_bound=q3+1.5*iqr

    outliers=df[(df[col]>upper_bound)|(df[col]<lower_bound)]
    print(len(outliers))


for col in column:
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr=q3-q1
    lower_bound=q1-1.5*iqr
    upper_bound=q3+1.5*iqr
    df[col]=df[col].clip(lower=lower_bound,upper=upper_bound)

# for print again run this
for col in column:
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr=q3-q1
    lower_bound=q1-1.5*iqr
    upper_bound=q3+1.5*iqr

    outliers=df[(df[col]>upper_bound)|(df[col]<lower_bound)]
    print(len(outliers))

#save the data

#df.to_csv("Cleaned Titanic data.csv",index=False)

