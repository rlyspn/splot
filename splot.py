import sys

class Plot:
    """Class representing information about the plot to be generated."""

    def __init__():
        #if log scale is on
        self.log = False
        #title for the graph
        self.title = ''
        #label for the x axis
        self.x_label = ''
        #label for the y axis
        self.y_label = ''
        #array of x data points
        self.x_data = []
        #{y_data_label:[y_data]} 
        self.y_data = []

def main():
    """Main function used as a driver."""
    if len(sys.argv) != 2:
        raise IOError("Error: incorrect input: splot <filename>")
    else:
        print "cool"


if __name__ == '__main__':
    main()
