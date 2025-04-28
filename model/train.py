# %%
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri('http://127.0.0.1:5000/')
mlflow.set_experiment(experiment_id=418684678139257596)
# %%
df = pd.read_csv('C:\\Users\\souza\\Downloads\\projeto credito\\data\\dataset_cluster.csv')
df.duplicated().value_counts()
df = df.drop_duplicates()
# %%
x = df.drop('target', axis=1)
y = df['target']
# %%
#split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42, stratify=y)
# %%
x_train.shape, y_train.shape, x_test.shape, y_test.shape
# %%
#separaçao colunas cat num e column tranform para pipe
num_atribs = ['FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'CNT_CHILDREN', 'AMT_INCOME_TOTAL',
        'DAYS_BIRTH', 'DAYS_EMPLOYED', 'FLAG_MOBIL', 'FLAG_WORK_PHONE',
        'FLAG_PHONE', 'FLAG_EMAIL', 'CNT_FAM_MEMBERS', 'MONTHS_BALANCE']

cat_atribs = ['CODE_GENDER', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE',
        'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'OCCUPATION_TREATED',
        'STATUS']
column_transf = ColumnTransformer([('scaler', StandardScaler(),num_atribs),
                                ('one_hot', OneHotEncoder(), cat_atribs)
                                ])
# %%
#pipeline
pipe_clf = Pipeline(steps=[('transform', column_transf),
                        ('PCA', PCA(n_components=2)),
                        ('model', DecisionTreeClassifier(
                            max_depth=4, min_samples_leaf=5, min_samples_split=10, random_state=42))])

# %%
#oversampling
x_train_res, y_train_res = RandomOverSampler(sampling_strategy=0.5, random_state=0).fit_resample(x_train, y_train)
# %%
#treino e metricas de treino 
with mlflow.start_run():
    mlflow.sklearn.autolog()
    modelo = pipe_clf.fit(x_train_res,y_train_res)
    #metricas treino 
    y_train_pred = modelo.predict(x_train)
    print('acuracia_train:', accuracy_score(y_train, y_train_pred))
    print('precision_train:', precision_score(y_train, y_train_pred))
    print('recall_train:', recall_score(y_train, y_train_pred))
    print('f1_train', f1_score(y_train, y_train_pred))

    acc_train = accuracy_score(y_train, y_train_pred)
    acc_test = accuracy_score(y_test, y_pred)
    #logar metricas no mlflow
    mlflow.log_metrics({'acc_train':acc_train,
                        'acc_test':acc_test
        })
    # %%
    #prediçao e metricas
    y_pred = modelo.predict(x_test)
    print('acuraccy_test:', accuracy_score(y_test, y_pred))
    print('precision_test:', precision_score(y_test, y_pred))
    print('recall_test:', recall_score(y_test, y_pred))
    print('f1_test', f1_score(y_test, y_pred))
# %%
