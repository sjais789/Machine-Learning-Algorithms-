

from sklearn.ensemble import RandomForestRegressor 

c=RandomForestRegressor()

c.fit(boston['data'],boston['target'])

c.score(boston['data'],boston['target'])


# check no. of features
#c.n_feautres_
#boston['data'].shape 


""" row= boston ['data'][20]
row.shape


q=row.reshape(-1,15)

c.predict(q)
boston['target'][20]  """

from sklearn.model_selection import train_test_split

xtrain, ytrain , xtest,ytest=train_test_split(boston['data'],bsoton['target'],test_size(0.4)) 
