# -*- coding: utf-8 -*-
"""kickstarter project v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IY7jxMpIhKvShh64ikrMhv9p7XsP25CB
"""

#importing of data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('/content/drive/My Drive/Colab Notebooks/(ongoing)kickstarter project/ks-projects-201801.csv')
df.head()

# info of dataset
df.info()

# shape of dataset
print(f'rows : {df.shape[0]}')
print(f'columns : {df.shape[1]}')

# statistical info about dataset
df.describe().T

# dropping of ID and name
df.drop(['ID','name','usd pledged'], axis=1, inplace=True)

df.head()

# to check any nan values
df.isna().sum()

# no na values

# exploratory data analyis and visualization

# object and num cols
ob_cols=[x for x in df.columns if df[x].dtype=='object']
print(ob_cols)
num_cols=[x for x in df.columns if (df[x].dtype=='int64')|(df[x].dtype=='float64')]
print(num_cols)

# countplots of categorical columns except deadline and launched

# top 15 categories
top15cat=df['category'].value_counts()[:15]
top15cat

pct_cat=top15cat/len(df)*100
pct_cat

top15cat.plot.bar(color='r', figsize=(10,5))

"""product design,documetary and music are at the top of number of kickstarters in the dataset"""

# top main categories
top_maincat=df['main_category'].value_counts()
top_maincat

pct_maincat=top_maincat/len(df)*100
pct_maincat

top_maincat.plot.bar(color='darkred', figsize=(10,5))

"""film & videos, music and publishing are at the top in the list of number of kickstarters."""

# currency count
curr=df['currency'].value_counts()
curr

pct_curr=curr/len(df)*100
pct_curr

curr.plot.bar(color='g', figsize=(10,5))

"""~80% of kickstarters have currency exchange in USD"""

# status of kickstarter
status=df['state'].value_counts()
status

pct_stat=status/len(df)
pct_stat

status.plot.bar(color='gray')

"""more than 50% of the kickstarters are failure"""

# countries to which kickstarters belong
cntry=df['country'].value_counts()
cntry

pct_cntry=cntry/len(df)
pct_cntry

cntry.plot.bar(color='black')

"""more than 75 % of kickstarters are from USA"""

# distribution plots of numerical columns

fig, axes=plt.subplots(3,2, figsize=(20,10))
for i,j in enumerate(num_cols):
  ax=axes[int(i/2), i%2]
  sns.kdeplot(df[j], ax=ax)

"""Not much info from the distribution plots beacuse they are pretty skewed"""

df.head(2)

# main category with goal usd
mcat_goalusd=df.groupby('main_category')['usd_goal_real'].sum().sort_values(ascending=False)
mcat_goalusd

mcat_goalusd.plot.bar(color='r', figsize=(10,5))

"""Film & video has goal with highest amount"""

# status with goals
stat_goals=df.groupby('state')['usd_goal_real'].sum().sort_values(ascending=False)
stat_goals

stat_goals.plot.bar()

# country with goals
count_goals=df.groupby('country')['usd_goal_real'].sum().sort_values(ascending=False)
count_goals

count_goals.plot.bar(color='darkblue', figsize=(10,5))

# most of the kickstarters are from usa it will be obvious that most amount of goals are in USA

# success rate of categories
div_0=df[df['state']=='successful']
div_0.head()

div_0['main_category'].value_counts()/len(df)*100

# music category has the highest success rate after that film and video.

# feature engineering

# new features
# deadline
df['d_day']=pd.to_datetime(df['deadline'], format='%Y/%m/%d').dt.day
# launched
df['l_day']=pd.to_datetime(df['launched'], format='%Y/%m/%d').dt.day
df.head(2)

df['state'].unique()

df.head(2)

status={'failed':0, 'canceled':0, 'successful':1, 'live':0, 'undefined':0,
       'suspended':0}

status

df['state']=df['state'].map(status)

df['state']

# preprocessing of dataset

df.head()

# we will drop category, deadline launched columns
df.drop(['category','deadline','launched'], axis=1, inplace=True)

df.head()

# one hot encoding of categorical columns
mcat=pd.get_dummies(df[['main_category']])
crcy=pd.get_dummies(df[['currency']])
ctry=pd.get_dummies(df[['country']])

df_new=pd.concat([df,mcat,crcy,ctry], axis=1)

df_new.head(2)

df_new.drop(['main_category','currency','country'], axis=1, inplace=True)

df_new.head(2)

# boxplots for outliers

box=['goal','pledged','state','backers','usd_pledged_real','usd_goal_real','d_day','l_day']
fig, axes=plt.subplots(4,2, figsize=(20,20))
for i,j in enumerate(box):
  ax=axes[int(i/2), i%2]
  sns.boxplot(df_new[j], ax=ax)

# outliers
df_new=df_new[df_new['goal']<=0.8e8]
df_new=df_new[df_new['pledged']<=1.5e7]
df_new=df_new[df_new['usd_pledged_real']<=1.5e7]
df_new=df_new[df_new['usd_goal_real']<=1.25e8]
df_new.shape

# after outliers boxplots
box=['goal','pledged','state','backers','usd_pledged_real','usd_goal_real','d_day','l_day']
fig, axes=plt.subplots(4,2, figsize=(20,20))
for i,j in enumerate(box):
  ax=axes[int(i/2), i%2]
  sns.boxplot(df_new[j], ax=ax)





y=df_new['state']
X=df_new.drop('state', axis=1)

print(y.shape)
print(X.shape)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
to_change=['goal','pledged','backers','usd_pledged_real','usd_goal_real','d_day','l_day']
X[to_change]=scaler.fit_transform(X[to_change])

X.head()

# model building

from sklearn.model_selection import cross_val_score, train_test_split, RandomizedSearchCV
X_train,X_test, y_train,y_test=train_test_split(X,y, test_size=0.3, random_state=42)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

from sklearn.linear_model import LogisticRegression
lor=LogisticRegression()
lor.fit(X_train,y_train)
y_pred_lor=lor.predict(X_test)
score_lor=cross_val_score(lor, X,y, cv=5)
print(score_lor)

score_lor.mean()

# classification report
from sklearn.metrics import classification_report, confusion_matrix
report_lor=classification_report(y_test,y_pred_lor)
print(report_lor)

# confusion matrix
cm=confusion_matrix(y_test,y_pred_lor)
sns.heatmap(cm, annot=True)

# roc auc curve
from sklearn.metrics import roc_curve, auc
fpr,tpr,threshold=roc_curve(y_test,y_pred_lor)
roc_score=auc(fpr,tpr)
print(roc_score)
plt.plot(fpr,tpr, label = 'AUC = %0.2f' % roc_score)
plt.plot([0,1],[0,1], 'r--')

# decision tree
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier()
dtc.fit(X_train,y_train)
y_pred_dtc=dtc.predict(X_test)
score_dtc=cross_val_score(dtc, X,y, cv=5)
print(score_dtc)

score_dtc.mean()

# randomforest 
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()
rfc.fit(X_train,y_train)
y_pred_rfc=rfc.predict(X_test)
score_rfc=cross_val_score(rfc, X,y, cv=5)
print(score_rfc)

report_rfc=classification_report(y_test,y_pred_rfc)
print(report_rfc)

# confusion matrix
cm_rfc=confusion_matrix(y_test,y_pred_rfc)
sns.heatmap(cm_rfc, annot=True)

# roc auc curve
from sklearn.metrics import roc_curve, auc
fpr,tpr,threshold=roc_curve(y_test,y_pred_rfc)
roc_score=auc(fpr,tpr)
print(roc_score)
plt.plot(fpr,tpr, label = 'AUC = %0.2f' % roc_score)
plt.plot([0,1],[0,1], 'r--')



