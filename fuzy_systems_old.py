import matplotlib.pyplot as plt
import re

'''def parse_fuzzy_sets(file):

    class my_dictionary(dict):

        def __init__(self):
            self = dict()

        def add(self, key, value):
            self[key] = value

    f = open(file, "r")
    lines = f.read()
    elements = lines.splitlines()

    for items in elements:
        if items == '':
            elements.remove(items)

    separated_list = []
    blank_list = []
    for items in elements:
        if re.search(r'=', items):
            blank_list.append(items)
        if '=' not in items:
            if blank_list != []:
                separated_list.append(blank_list)
                blank_list = []
    separated_list.append(blank_list)

    value_list = []
    for items in separated_list:
        dict_obj = my_dictionary()
        for item in items:
            x = item.split('=')
            dict_obj.add(x[0],x[1])
        value_list.append(dict_obj)
    #print(value_list)

    key_list = []
    for items in elements:
        if '=' not in items:
            key_list.append(items)
    #print(key_list)

    dict_of_dict = my_dictionary()
    for i, j in zip(key_list,value_list):
        dict_of_dict.add(i,j)
    return dict_of_dict

file = 'fuzzy_sets.txt'
dictionary = parse_fuzzy_sets(file)
print(dictionary)

def graph_range(values):
    #values = list[values]
    a = values[0]
    b = values[1]
    alpha = values[2]
    beta = values[3]
    starting_point = a - alpha
    end_point = b + beta
    x = [starting_point, a, b, end_point]
    y = [0, 1, 1, 0]
    return x, y


dictionary_HR = {
    'very_low': (40, 40, 0, 20),
    'low': (60, 60, 20, 10),
    'normal': (70, 90, 10, 10),
    'high': (100, 100, 10, 20),
    'very high': (120, 120, 20, 0)
}
dictionary_R = {
    'low': (0, 3, 0, 3),
    'normal': (6, 8, 3, 2),
    'high': (10, 12, 2, 0)
}
dictionary_D = {
    'very_small': (0, 0, 0, 2),
    'small': (2, 2, 2, 2),
    'moderate': (4, 4, 2, 2),
    'average': (6, 6, 2, 2),
    'high': (8, 8, 2, 2),
    'very high': (10, 10, 2, 2)
}
plot_graphs = []
for value in dictionary_HR.values():
    plot_graph = graph_range(value)
    plot_graphs.append(plot_graph)

plt.xlim([0, plot_graphs[4][0][3] + plot_graphs[0][0][0]])
plt.ylim([0, 1])
plt.plot(plot_graphs[0][0], plot_graphs[0][1], 'r', linewidth =2, label = 'very low')
plt.plot(plot_graphs[1][0], plot_graphs[1][1], 'b', linewidth =2, label = 'low')
plt.plot(plot_graphs[2][0], plot_graphs[2][1], 'g', linewidth =2, label = 'normal')
plt.plot(plot_graphs[3][0], plot_graphs[3][1], 'c', linewidth =2, label = 'high')
plt.plot(plot_graphs[4][0], plot_graphs[4][1], 'm', linewidth =2, label = 'very high')
plt.legend()
plt.show()

def membership_function(x,a,b,alpha,beta):
    if x <= (a - alpha):
        membership_degree = 0
    elif (a - alpha) < x < a:
        membership_degree = (x - a + alpha)/alpha
    elif a <= x <= b:
        membership_degree = 1
    elif b < x < (b + beta):
        membership_degree = (b + beta - x)/beta
    elif x >= (b + beta):
        membership_degree = 0
    return membership_degree

#print(membership_function(63,60,60,20,10))'''