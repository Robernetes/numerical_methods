from math import *
import pandas as pd 
from tabulate import tabulate

#fun = 'cos(2*x)'
#fun_sol = 'sin(2*x)/2'

fun = input('Enter the functions: ')
option = input('The function has solution function? y/n: ')
if option == 'y':
    fun_sol = input('Enter function solution: ')
else:
    fun_sol = ''


x_0 = 0  # x sub cero
y_0 = 0  #condicion inicial
x_n = 2  
h = 0.125

x_i = []
y_i = []
fx = []
er = []

laps = int(x_n/h)

fn = lambda x,y: eval(fun) #PRINCIPAL FUNCTION
fn_sol = lambda x: eval(fun_sol) #SOLUTION FUNCTION
eum = lambda x,y,h: y + h * ((fn(x,y) + fn(x + h, y + h * fn(x,y)))/2) #

j = 0
x = 0
y = 0

for item in range(laps+1):
    if item == 0:
        x_i.append(x_0)
        y_i.append(y_0)
        fx.append(item)
        er.append(item)
    if item > 0:
        x_i.append(j)
        x = x_i[item-1]
        y = y_i[item-1]
        y_i.append(eum(x,y,h))
        if option == 'y':
            fx.append(fn_sol(j))
            er.append(abs(((fx[item]-y_i[item])/fx[item])))
    j+=h


if option == y:
    datafinal = pd.DataFrame(list(zip(x_i,y_i,fx,er)), columns=['x_i','y_i','Funtion Sol','error'])
    #print(tabulate(datafinal,))
else:
    datafinal = pd.DataFrame(list(zip(x_i,y_i)), columns=['x_i','y_i'])
    print(tabulate(datafinal, headers = 'keys', tablefmt = 'psql'))
