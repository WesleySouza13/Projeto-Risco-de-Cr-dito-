# %%
import mlflow
import pandas as pd

mlflow.set_tracking_uri('http://127.0.0.1:5000/')
model = mlflow.sklearn.load_model('models:/modelo-risco-de-credito-arvore/1')
# %%
model.feature_names_in_

# %%
df = pd.read_csv('C:\\Users\\souza\\Downloads\\projeto credito\\data\\dataset_cluster.csv')
x = df.head(10)[model.feature_names_in_]
x
# %%
predict = model.predict_proba(x).round(2)
predict
# %%
