from matplotlib import pyplot
from matplotlib import style
import sys
import csv

style.use('ggplot')

x_axis = []
x_axis_labels= []
y_axis = []


with open(sys.argv[1], "r", encoding='utf=8') as f:
    reader = csv.reader(f, delimiter=":")
    for idx, line in enumerate(reader):
        x_axis.append(idx)
        x_axis_labels.append(line[0])
        y_axis.append(line[1])


pyplot.bar(x_axis, y_axis, align='center')
pyplot.xticks(x_axis, x_axis_labels, rotation=90)
pyplot.show()
