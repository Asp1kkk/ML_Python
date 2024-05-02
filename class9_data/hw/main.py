import pandas as pd
import numpy as np
import time

def getDF():
	dfs = []

	for i in range(10):
		studentDf = pd.read_csv(f'./Data/raw/Students_info_{i}.csv')
		gradeDf = pd.read_csv(f'./Data/raw/Students_marks_{i}.csv')

		concatedDf = pd.concat([studentDf, gradeDf], axis=1)
		dfs.append(concatedDf)
	
	df = pd.concat(dfs, ignore_index=True)

	df = df.rename(columns={'parental level of education': 'education', 'test preparation course': 'test preparation'})

	return df

# = = = = = = = = = = = = 1 = = = = = = = = = = = =

df = getDF()

#print(df.head())

# = = = = = = = = = = = = 2 = = = = = = = = = = = =

df = df.drop(columns=['index'])

#print(df.head(10))

# = = = = = = = = = = = = 3 = = = = = = = = = = = =

#print(f"columns: {df.shape[1]}", f"rows: {df.shape[0]}", sep="\n")

# = = = = = = = = = = = = 4 = = = = = = = = = = = =

#print('math score mean:', df['math score'].mean())
#print('math score std:', df['math score'].std())
#print('math score min:', df['math score'].min())
#print('math score max:', df['math score'].max())

#print('reading score mean:', df['reading score'].mean())
#print('reading score std:', df['reading score'].std())
#print('reading score min:', df['reading score'].min())
#print('reading score max:', df['reading score'].max())

#print('writing score mean:', df['writing score'].mean())
#print('writing score std:', df['writing score'].std())
#print('writing score min:', df['writing score'].min())
#print('writing score max:', df['writing score'].max())

# = = = = = = = = = = = = 5 = = = = = = = = = = = =

#print(np.where(pd.isnull(df))) # [] => Пустых нет
#print(np.where(pd.isna(df))) # [] => Пустых нет

# = = = = = = = = = = = = 6 = = = = = = = = = = = =

#print('math score mean:', df['math score'].mean())
#print('reading score mean:', df['reading score'].mean())
#print('writing score mean:', df['writing score'].mean())

# = = = = = = = = = = = = 7 = = = = = = = = = = = =

#print('math mean (completed)', df.loc[df['test preparation'] == 'completed']['math score'].mean())
#print('reading mean (completed)', df.loc[df['test preparation'] == 'completed']['reading score'].mean())
#print('writing mean (completed)', df.loc[df['test preparation'] == 'completed']['writing score'].mean())

#print('- - - - - - - - - - - - - - - -')

#print('math mean (none)', df.loc[df['test preparation'] == 'none']['math score'].mean())
#print('reading mean (none)', df.loc[df['test preparation'] == 'none']['reading score'].mean())
#print('writing mean (none)', df.loc[df['test preparation'] == 'none']['writing score'].mean())

# = = = = = = = = = = = = 8 = = = = = = = = = = = =

#print(df.lunch.unique())

# = = = = = = = = = = = = 9 = = = = = = = = = = = =

# см. в getDF на 16 строке

# = = = = = = = = = = = = 10 = = = = = = = = = = = =

#passmark = 50

#mathCompleted = df.loc[df["math score"] >= passmark].shape[0]
#mathAndCourseCompleted = df.loc[(df["math score"] >= passmark) & (df['test preparation'] == 'completed')].shape[0]
#mathWomenAndCourseNotCompleted = df.loc[(df["math score"] < passmark) & (df['test preparation'] == 'none') & (df['gender'] == 'female')].shape[0]

#print(f'{mathCompleted} students successfully completed their math exam (>= 50). This is {(mathCompleted / 1000) * 100}%')

#print(f'{mathAndCourseCompleted} students who successfully pass the preparation course successfully completed their math exam (>= 50). This is {(mathAndCourseCompleted / 1000) * 100}%')

#print(f'{mathWomenAndCourseNotCompleted} female students who didn\'t pass the preparation course successfully didn\'t complete their math exam (< 50). This is {(mathWomenAndCourseNotCompleted / 1000) * 100}%')

# = = = = = = = = = = = = 11 = = = = = = = = = = = =

#def timeSpended(func):
#	def wrapper(*args, **kwargs):
#		start = time.time()
#		result = func(*args, **kwargs)
#		print("time spent: ", time.time() - start)
#		return result
#	return wrapper

#@timeSpended
#def func():
#	print(df.groupby(['race/ethnicity'])['reading score'].mean())

#func()

#print('- - - - - - - - - - - - - - - -')

#@timeSpended
#def func1():
#	print(df.groupby(['education'])['writing score'].min())

#func1()


# = = = = = = = = = = = = 12 = = = = = = = = = = = =

#@timeSpended
#def func3():
#	groups = df.groupby(['race/ethnicity'])
#	for group, group_df in groups:
#		print(group[0], " ", group_df['reading score'].mean())

#func3()

#@timeSpended
#def func4():
#	groups = df.groupby(['education'])
#	for group, group_df in groups:
#		print(group[0], " ", group_df['writing score'].min())

#func4()

# = = = = = = = = = = = = 13 = = = = = = = = = = = =

#grouped = pd.pivot_table(df, index=['gender', 'education'], aggfunc={"reading score": 'mean', "writing score": 'mean', "math score": 'mean'})

#print(grouped)

# = = = = = = = = = = = = 14 = = = = = = = = = = = =

df['Math_PassStatus'] = df['math score'].apply(lambda x: 'P' if x >= 50 else 'F')
df['Reading_PassStatus'] = df['reading score'].apply(lambda x: 'P' if x >= 50 else 'F')
df['Writing_PassStatus'] = df['writing score'].apply(lambda x: 'P' if x >= 50 else 'F')

# = = = = = = = = = = = = 15 = = = = = = = = = = = =

df['OverAll_PassStatus'] = df.apply(lambda row: 'P' if row['Math_PassStatus'] == 'P' and row['Reading_PassStatus'] == 'P' and row['Writing_PassStatus'] == 'P' else 'F', axis=1)

print(df.loc[df['OverAll_PassStatus'] == 'P'].shape[0])

# = = = = = = = = = = = = 16 = = = = = = = = = = = =

def GetGrade(first, second, third):
	avg = (first+ second + third) / 3
	if avg > 90:
		return 'A'
	elif avg > 80:
		return 'B'
	elif avg > 70:
		return 'C'
	elif avg > 60:
		return 'D'
	elif avg > 50:
		return 'E'
	else:
		return 'F'

df['Grade'] = df.apply(lambda row: GetGrade(row['math score'], row['reading score'], row['writing score']), axis=1)

print(df)
	