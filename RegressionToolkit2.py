import pandas as pd
from statsmodels.tsa.stattools import adfuller
import numpy as np

class RegressionToolkit:
    def __init__(self, var):
        self.var = var  # Convert to pandas Series
    
    def adf_test(self):
        result = adfuller(self.var)
        print('ADF statistic:', result[0])
        print('p value:', result[1])
        if result[1] < 0.05:
            print('stationary')
        else:
            print('non stationary')
    
    def Transform(self, transform):
        if transform == 'log':
            return np.log(self.var)
        elif transform == '1stDiff':
            return self.var.diff().dropna()
        elif transform == '2ndDiff':
            return self.var.diff().diff().dropna()
        elif transform == '%chg':
            return self.var.pct_change().dropna()
        elif transform == 'std trsfm':
            return (self.var - self.var.mean()) / self.var.std()
        else:
            pass  # Handle other cases gracefully if needed
            return self.var
    
    def chkStationarity(self):
        transforms = ['log', '%chg', 'std trsfm', '1stDiff', '2ndDiff']
        for tf in transforms:
            var_transformed = self.Transform(tf)  # Use self.Transform() to transform self.var
            self.adf_test()  # Use adf_test() to perform ADF test on transformed data
            print(tf)

def setStationarity(var):
        transforms = ['log', '%chg', 'std trsfm', '1stDiff', '2ndDiff']
        statn_var = []
        tfm = []
        for tf in transforms:
            var_transformed = RegressionToolkit(var).Transform(tf)
            result = adfuller(var_transformed)
            if result[1] < 0.05:
                statn_var.append(var_transformed)
                tfm.append(tf)
                break  # Assuming we stop at the first stationary transformation found
        return statn_var