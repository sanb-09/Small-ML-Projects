

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
train = pd.read_csv("E://ML//Kaggle Titanic//train.csv")
test = pd.read_csv("E://ML//Kaggle Titanic//test.csv")
train = train.drop(['Name','Cabin','Ticket'],axis = 1)
test = test.drop(['Name','Cabin','Ticket'],axis = 1)
train["Age"].fillna( method ='ffill', inplace = True)
#print(train.isna().sum())
test["Age"].fillna( method ='ffill', inplace = True)
train.dropna()
test.dropna()

from sklearn.preprocessing import StandardScaler
replacement = {
    'S': 0,
    'Q': 1,
    'C': 2
}

train['Embarked'] = train['Embarked'].apply(lambda x: replacement.get(x))
train['Embarked'] = StandardScaler().fit_transform(train['Embarked'].values.reshape(-1, 1))
test['Embarked'] = test['Embarked'].apply(lambda x: replacement.get(x))
test['Embarked'] = StandardScaler().fit_transform(test['Embarked'].values.reshape(-1, 1))

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()
train['Sex'] = label_encoder.fit_transform(train['Sex'])

#train['Embarked'] = onehot_encoder.fit_transform(train['Embarked'].value.reshape(1,-1))
train.dropna()
test['Sex'] = label_encoder.fit_transform(test['Sex'])
#test['Embarked'] = onehot_encoder.fit_transform(test['Embarked'])
test.dropna()
print(test.isna().sum())
y = train.iloc[:,1].values
train = train.drop(['Survived'],axis = 1)
x = train.iloc[:,:].values

from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression()
regressor.fit(x, y)
pred = regressor.predict(test)

from sklearn.metrics import accuracy_score

#print(len(test['PassengerId'])," ",len(pred))
df = pd.DataFrame({'PassengerId':test['PassengerId'],'Survived':pred})
df.to_csv("E:\ML\Kaggle Titanic//Final_Pred_new1.csv", index = False)
