import sys
import string
from plot import *

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
    name = col_name[col_name.find(',') + 1:]
    data = getCol(fileName, col)
    return (name,data)

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

def assignColors(pl):

    colors = ['blue', 'red', 'green', 'cyan', 'magenta', 'yellow', 'black']
    colorIndex = 0
    for ind in range(len(pl.y_data)):
        newTuple = (pl.y_data[ind][0], pl.y_data[ind][1], colors[colorIndex])
        pl.y_data[ind] = newTuple
        colorIndex = (colorIndex + 1) % len(colors)
    return pl

def main():
    """Main function used as a driver."""

    if len(sys.argv) != 2:
        raise IOError("Error: incorrect input: splot <filename>")
    else:
        data = readFile(sys.argv[1])
        plot = parseInput(data)
        plot = assignColors(plot)
        #assign colors to graphs
        print plot
        plotData(plot)

if __name__ == '__main__':
    main()
