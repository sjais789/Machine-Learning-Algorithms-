

from sklearn.ensemble import RandomForestRegressor 

c=RandomForestRegressor()

c.fit(boston['data'],boston['target'])

c.score(boston['data'],boston['target'])


# check no. of features
#c.n_feautres_
#boston['data'].shape 


"""row= boston ['data'][20]
row.shape


q=row.reshape(-1,15)

c.predict(q)
boston['target'][20] """


