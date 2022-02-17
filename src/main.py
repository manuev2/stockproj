from predict import predict
from coinbaseapihandler import dataextraction
from arraysplitter import arraysplitter
def main():
    x = []
    y = []
    splitnum = 4

    #Retrieve Data from Coinbase API
    data = dataextraction()
    #Loop through List and retrieve prices from Price objects
    for price in range(len(data)):
        x.append(getattr(data[price], 'time'))
        y.append(float(getattr(data[price], 'price')))
    #Reverse Data
    x = x[::-1]
    y = y[::-1]
    #Split Data into sub arrays
    valuesplit = arraysplitter(y, splitnum)
    datesplit = arraysplitter(x, splitnum)
    #Predict and Plot
    predict(datesplit, valuesplit, splitnum)

if __name__ == "__main__":
    main()