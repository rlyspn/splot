import sys
import string

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

def readFile(fileName):
    '''Returns a string containing the contents of a file.'''
    
    contents = open(fileName).read()
    return contents

def getLogScale(line):
    data = line.split('=')
    if data[1] == 'true':
        return True
    else:
        return False

def parseTitle(line):
    return line[len('title='):]

def parseXLabel(line):
    return line[len('x_label='):]

def parseYLabel(line):
    return line[len('y_label='):]

def parseDataFile(line):
    return line[len('file='):]

def getCol(fileName, col):
    returnData = []
    data = readFile(fileName).split('\n')
    for line in data:
        if len(line) > 0:
            returnData.append(float(line.split(' ')[col]))
    return returnData


def parseYData(line, fileName):
    col_name = line[len('y_data='):]
    col = int(col_name[:col_name.find(',')])
    name = col_name[col_name.find(','):]
    data = getCol(fileName, col)
    return {name:data}

def parseXData(line, fileName):
    col = int(line[len('x_data='):])
    data = getCol(fileName, col)
    return data

def parseInput(inputData):
    '''@param inputData - copy of the data from the splot input file.
    @return-returns an instance of the plot object'''

    p = Plot()
    data = inputData.split('\n')
    for line in data:
        if line.find('logscale') == 0:
            p.log = getLogScale(line)
        elif line.find('title') == 0:
            p.title = parseTitle(line)
        elif line.find('x_label') == 0:
            p.x_label = parseXLabel(line)
        elif line.find('y_label') == 0:
            p.y_label = parseYLabel(line)
        #get file
        elif line.find('file') == 0:
            dataFile = parseDataFile(line)
        elif line.find('y_data') == 0:
            p.y_data.append(parseYData(line, dataFile))
        elif line.find('x_data') == 0:
            p.x_data = parseXData(line, dataFile)
        else:
            print 'Error: %s is an unknown command. Ignoring.' % line
    return p

def main():
    """Main function used as a driver."""

    if len(sys.argv) != 2:
        raise IOError("Error: incorrect input: splot <filename>")
    else:
        data = readFile(sys.argv[1])
        plot = parseInput(data)
        print plot


if __name__ == '__main__':
    main()
