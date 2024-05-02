import pandas as pd

df = pd.read_csv('./titanic_train.csv')

# = = = = = 1 = = = = =

#print(df['Sex'].value_counts()) # кол-во мужчин и женщин

# = = = = = 2 = = = = =

#print(df['Pclass'].value_counts()) # кол-во пассажиров разных классов

# = = = = = 3 = = = = =

#print('= = = 3 = = =')
#print(df.loc[(df.Pclass ==  3) & (df.Sex == 'male'),['Sex', 'Fare']].mean(numeric_only=True)) #12.6
#print(df.loc[(df.Pclass ==  3) & (df.Sex == 'female'),['Sex', 'Fare']].mean(numeric_only=True)) #16.1
#print('= = = 2 = = =')
#print(df.loc[(df.Pclass ==  2) & (df.Sex == 'male'),['Sex', 'Fare']].mean(numeric_only=True)) #19.7
#print(df.loc[(df.Pclass ==  2) & (df.Sex == 'female'),['Sex', 'Fare']].mean(numeric_only=True)) #21.9
#print('= = = 1 = = =')
#print(df.loc[(df.Pclass ==  1) & (df.Sex == 'male'),['Sex', 'Fare']].mean(numeric_only=True)) #67.2
#print(df.loc[(df.Pclass ==  1) & (df.Sex == 'female'),['Sex', 'Fare']].mean(numeric_only=True)) #104.1

# = = = = = 4 = = = = =

print(df.loc[(df.Sex == 'male') & (df.Pclass == 1), ['Cabin']].value_counts())
print(df.loc[(df.Sex == 'female') & (df.Pclass == 1), ['Cabin']].value_counts())

# = = = = = 5 = = = = =

print(df[df.Age.isnull()])
