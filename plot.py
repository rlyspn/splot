import matplotlib.pyplot as p

class Plot:
    """Class representing information about the plot to be generated."""

    def __init__(self):
        '''Initialization function for Plot.'''

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

    def __str__(self):
        st = 'logscale=%s\n' % self.log
        st += ('title=%s\nx label=%s\ny label=%s\n' % (self.title, self.x_label, self.y_label))
        st += ('y data = ' + str(self.y_data))
        st += '\n'
        st += ('x data = ' + str(self.x_data))
        return st

def plotData(plot):
    p.title(plot.title)
    p.xlabel(plot.x_label)
    p.ylabel(plot.y_label)
    
    for i in plot.y_data:
        print i
        if plot.log:
            p.loglog(plot.x_data, i[1], color=i[2], linestyle='solid', marker='o', label=i[0])
        else:
            p.plot(plot.x_data, i[1], color=i[3], linestyle='solid', marker='o', label=i[0])

    p.savefig("test.png")
