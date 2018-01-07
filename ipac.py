import pandas as pd
import csv

year_1 = pd.read_csv('/home/sukoushal/Desktop/Python/IPAC/year_1.csv')
year_2 = pd.read_csv('/home/sukoushal/Desktop/Python/IPAC/year_2.csv')
year_3 = pd.read_csv('/home/sukoushal/Desktop/Python/IPAC/year_3.csv')
year_4 = pd.read_csv('/home/sukoushal/Desktop/Python/IPAC/year_4.csv')
year_5 = pd.read_csv('/home/sukoushal/Desktop/Python/IPAC/year_5.csv')
year_6 = pd.read_csv('/home/sukoushal/Desktop/Python/IPAC/year_6.csv')

year_1.columns = ['constituency', 'first', 'second', 'third', 'fourth']
year_2.columns = ['constituency', 'first', 'second', 'third', 'fourth']
year_3.columns = ['constituency', 'first', 'second', 'third', 'fourth']
year_4.columns = ['constituency', 'first', 'second', 'third', 'fourth']
year_5.columns = ['constituency', 'first', 'second', 'third', 'fourth']
year_6.columns = ['constituency', 'first', 'second', 'third', 'fourth']


year_1 = year_1.loc[:, year_1.columns != 'constituency'].applymap(lambda x: float(x.strip('%')))
year_2 = year_2.loc[:, year_2.columns != 'constituency'].applymap(lambda x: float(x.strip('%')))
year_3 = year_3.loc[:, year_3.columns != 'constituency'].applymap(lambda x: float(x.strip('%')))
year_4 = year_4.loc[:, year_4.columns != 'constituency'].applymap(lambda x: float(x.strip('%')))
year_5 = year_5.loc[:, year_5.columns != 'constituency'].applymap(lambda x: float(x.strip('%')))
year_6 = year_6.loc[:, year_6.columns != 'constituency'].applymap(lambda x: float(x.strip('%')))


year1 = year_1[['first','second', 'third', 'fourth']]
year2 = year_2[['first','second', 'third', 'fourth']]
year3 = year_3[['first','second', 'third', 'fourth']]
year4 = year_4[['first','second', 'third', 'fourth']]
year5 = year_5[['first','second', 'third', 'fourth']]
year6 = year_6[['first','second', 'third', 'fourth']]

##############################################
from sklearn.cluster import KMeans

cluster = KMeans(n_clusters = 4, n_init = 100, max_iter = 500, algorithm = 'full')
cluster.fit(year6)

six_pre = cluster.labels_
second_pre = cluster.predict(year2)
third_pre = cluster.predict(year3)
first_pre = cluster.predict(year1)
fourth_pre = cluster.predict(year4)
five_pre = cluster.predict(year5) 
pre = [first_pre, second_pre, third_pre, fourth_pre, five_pre, six_pre]
year = [year_1, year_2, year_3, year_4, year_5, year_6]
columns = ['year1', 'year_2', 'year_3', 'year_4', 'year_5', 'year_6']
for i in range(len(pre)): 
	clusters = [[] for c in xrange(4)]
	for (row, label) in enumerate(pre[i]):
		clusters[label].append(row) 
	year[i]['polarity'] = ''
	for j in range(4):
		print j
		for k in clusters[j]:
			year[i].polarity.iloc[k] = j

cluster.cluster_centers_

cluster_map = {0: 'Divided-Unipolar', 1: 'Unipolar', 3:'Bipolar' , 2	: 'Multipolar'}

for i in year:
	i['class'] = i['polarity'].map(cluster_map)

final_6 = pd.DataFrame()
for i in range(len(year)):
	final_6[str(columns[i])] = year[i]['class']


final_list = [final_1, final_2, final_3, final_4, final_5, final_6]


year_first = pd.DataFrame()
from_year = ['from_1', 'from_2', 'from_3', 'from_4', 'from_5', 'from_6']

for i in range(len(final_list)):
	year_first[from_year[i]] = final_list[i]['year1']

from collections import Counter

year_first['most_prob'] = ''
for i in range(len(year_first)):
	year_first['most_prob'].iloc[i] = Counter(list(year_first.iloc[i])).most_common(1)[0][0]







