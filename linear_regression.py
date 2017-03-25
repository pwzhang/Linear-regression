import numpy as np
from numpy import dot
from numpy import transpose
path = 'detroit_data.txt'
def generate_array(path):
    fwrite = open(path)
    x = []
    y = []
# put x and y of the data in to array
    for line in fwrite:
        line = line.split()
        for item in range(len(line)):
            line[item] = float(line[item])
        x.append(line[:-1])
        y.append(line[-1:])
    for i in range(len(x)):
        x[i].insert(0,1)
    x = np.array(x)
    y = np.array(y)
    return x,y

def data_manipulate(x):
    aver_list = []
    x_list = [0] * 9
    s = []
# find the maximum and minimum number in each column.
    for i in range(9):
        tempmin = x[1][i]
        tempmax = tempmin
        for j in range(13):
            x_list[i] += x[j][i+1] / 13
            if tempmin> x[j][i+1]:
                tempmin = x[j][i+1]
            if tempmax < x[j][i+1]:
                tempmax = x[j][i+1]
# find average and the range of each column.
        aver_list.append(x_list[i])
        s.append((tempmax-tempmin))
    return aver_list,s

def linear_regression(path):
    (x, y)=generate_array(path)
    (aver_list, s) = data_manipulate(x)
    for i in range(13):
# process feature scaling with each column.
        for j in range(9):
            x[i][j+1] = (x[i][j+1] - aver_list[j]) / s[j]
    # initially set condition of Theta
    theta = [900]+ [-1]*9
    for j in range(1000):
        temp = [0] * 10
    # replace Theta with new Theta each round of regression.
        for i in range(len(theta)):
            temp[i] = float(theta[i] - (1 / 13) * (dot((dot(theta, transpose(x)) - transpose(y)), transpose(transpose(x)[i])))-(2/13)*theta[i]/abs(theta[i]))
        theta = temp
    print(theta)




linear_regression(path)