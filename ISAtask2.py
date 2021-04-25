import pandas as pd
df = pd.read_csv('C:\Anaconda\weatherAUS.csv')

#Level 1
Avg_MaxTemp= df['MaxTemp'].mean()
Avg_MinTemp= df['MinTemp'].mean()
cobar = df[df['Location'] == 'Cobar']
Cobar_Avg_MaxTemp = cobar['MaxTemp'].mean()
Null_Sunshine = df['Sunshine'].isna().sum()
Null_Evaporation = df['Evaporation'].isna().sum()
output = {"Average Maximum Temperature":[Avg_MaxTemp],
          "Average Minimum Temperature":[Avg_MinTemp],
          "Average Maximum Temperature in the Location Cobar":[Cobar_Avg_MaxTemp],
          "Count of null value in Sunshine":[Null_Sunshine],
          "Count of null value in Evaporation":[Null_Evaporation]}
df2 = pd.DataFrame(output)
print(df2)

#Level 2
Avg_Evap= df['Evaporation'].mean()
df["Evaporation"].fillna(Avg_Evap, inplace = True)
df.dropna(inplace = True, axis=1)
df.drop('Date', inplace = True, axis =1)

#Level 3
def location(Loca):
    data = df[df['Location'] == Loca]
    return(data)
find_loca = input("Enter location to look at data- ")
print(location(find_loca))