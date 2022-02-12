import matplotlib.pyplot as plt

def plot(x, y, scatterX, scatterY):
    # plotting the points
    plt.scatter(scatterX, scatterY)
    plt.plot(x, y)
    #plt.scatter
    # naming the x axis
    plt.xlabel('time')
    # naming the y axis
    plt.ylabel('price')
    # giving a title to my graph
    plt.title('ETH Historical Data')
    # function to show the plot
    plt.show()
