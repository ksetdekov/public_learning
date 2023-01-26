import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import scipy
from sklearn.base import BaseEstimator, TransformerMixin

example_df = pd.DataFrame({
    'Car_model': ['BMW 5', 'Renault 21', 'BMW 5', 'Hyunday Santro'],
    'Engine_Model': ['type A', 'type B', np.NaN, 'type C']
})


class WithinGroupModeImputer(BaseEstimator, TransformerMixin):
    def __init__(self, group_var):
        self.group_var = group_var

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # the copy leaves the original dataframe intact
        X_ = X.copy()
        for col in X_.columns:
            if X_[col].dtypes == 'object':
                X_.loc[(X[col].isna()) & X_[self.group_var].notna(), col] = X_[self.group_var].map(
                    X_.groupby(self.group_var)[col].agg(lambda x: scipy.stats.mode(x, keepdims=False)[0]))
                X_[col] = X_[col].fillna(X_[col].agg(
                    lambda x: scipy.stats.mode(x, keepdims=False)[0]))
        return X_


imp = WithinGroupModeImputer(group_var='Car_model')
imp.fit(example_df)
print(imp.transform(example_df))
