We can use a grid search to find the best parameters for this model. Lets try
#Define a list of parameters for the models
#params = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
 #              'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
params = {'C': [1, 10, 100],
               'gamma': [1, 10, 100]}


#We can build Grid Search model using the above parameters.
#cv=5 means cross validation with 5 folds
print("Finding the best parameters...", end = '')
lsvm = GridSearchCV(SVC(random_state=0), params, cv=2, n_jobs=1)
print("Done.")

print("Training the model the best parameters...", end = '')
lsvm.fit(onehot_enc.transform(X_train), y_train)
print("Done.")
print("Best parameters set found on development set:")
print()
print(lsvm.best_params_)
#print("train score - " + str(lsvm.score(onehot_enc.transform(X_train), y_train)))
#print("test score - " + str(lsvm.score(onehot_enc.transform(X_train), y_test)))
