import numpy as np
from sklearn.linear_model import LinearRegression
from dateparser import dateparser
from plot import plot
from sklearn.metrics import mean_squared_error, r2_score

def predict(x, y, splitnum):
    for n in range(splitnum):
        # Time in String to Time in Gregorian for easier calculations, 2d array for linear regression model
        gregorianX = [dateparser(x[n])]
        #Linear X and Y
        linearX = np.array(gregorianX).reshape((-1, 1))
        linearY = np.array(y[n])
        #Model for linear regression with X & Y vals
        model = LinearRegression()
        model.fit(linearX, linearY)
        #Prediction for Price using Gregorian Date Value

        predlinearY = model.predict(linearX)
        #Plotting Scatter of real data, and Line of Prediction
        print("Coefficients: \n", model.coef_)
        # The mean squared error
        print("Mean squared error: %.2f" % mean_squared_error(y[n], predlinearY))
        # The coefficient of determination: 1 is perfect prediction
        print("Coefficient of determination: %.2f" % r2_score(y[n], predlinearY))
        plt = plot(linearX, predlinearY, gregorianX, y[n])
    plt.show()
