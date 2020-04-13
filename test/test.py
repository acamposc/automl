import os
import h2o
import pandas as pd

from h2o.automl import H2OAutoML

# initialize clusters
h2o.init(nthreads=-1, max_mem_size=8)
h2o.connect()

# data loading
# dataset: https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls
# needs to be transformed to csv
# be wary of the header
df = h2o.import_file('test/uci.csv', header=1, sep=',')
df = df.drop('ID')
print(df.columns)

# definition of independent and dependent variables
y = 'default payment next month'
x = list(df.columns).remove(y)

# check whether our y has 1s and 0s
print(df[y].type)
# turn y into categorical
df[y] = df[y].asfactor()

# h2o-3 dataset partition function 
splits = df.split_frame(ratios=[0.7,0.15], seed=1)

# splits outcome division into 3 new variables
train, valid, test  = splits
print(train.nrow, valid.nrow, test.nrow)


# automl estimator
aml = H2OAutoML(
    max_models = 5,
    max_runtime_secs = 300,
    seed = 1
)

aml.train(
    x = x,
    y = y,
    training_frame = train
)

# performance evaluation: leaderboard
lb = aml.leaderboard
print(
    lb.head(rows = lb.nrows)
)

# predict with the leader
yhat = aml.leader.predict(test)
auc = aml.leader.auc()
conf = aml.leader.confusion_matrix()

print(yhat)
print(auc)
print(conf)

# download best model
h2o.download_model(model = aml.leader, path = 'test/output/')

h2o.cluster().shutdown()