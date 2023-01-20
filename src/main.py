from predict import predict
from coinbaseapihandler import dataextraction
from arraysplitter import arraysplitter
def main():
    time = []
    price = []
    splitnum = 4

    # Retrieve Data from Coinbase API
    data = dataextraction()
    
    # Loop through List and retrieve prices from Price objects
    for idx in range(len(data)):
        time.append(getattr(data[idx], 'time'))
        price.append(float(getattr(data[idx], 'price')))
    
    # Reverse Data
    time = time[::-1]
    price = price[::-1]
    
    # Split Data into sub arrays
    valuesplit = arraysplitter(price, splitnum)
    datesplit = arraysplitter(time, splitnum)
    print("Test")
    # Predict and Plot
    predict(datesplit, valuesplit, splitnum)

if __name__ == "__main__":
    main()