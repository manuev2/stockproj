from predict import predict
from coinbaseapihandler import dataextraction
from arraysplitter import arraysplitter
def main():
    x = []
    y = []
    #Retrieve Data from Coinbase API
    data = dataextraction()
    #Loop through List and retrieve prices from Price objects
    for price in range(len(data)):
        x.append(getattr(data[price], 'time'))
        y.append(float(getattr(data[price], 'price')))
    #Reverse Data
    x = x[::-1]
    y = y[::-1]

    #splitarray = arraysplitter(y, 4)
    #Predict and Plot
    predict(x, y)

if __name__ == "__main__":
    main()