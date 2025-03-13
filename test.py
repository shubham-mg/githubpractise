def adf_test(self):
    result = adfuller(self.var)
    print('ADF statistic:', result[0])
    print('p value:', result[1])
    if result[1] < 0.05/100:
            print('stationary')
    else:
            print('non stationary')