import numpy as np
import matplotlib.pyplot as plt
import sys, os
import math
    
def file_reader():
    print(f'File Reading...')
    dir_li = os.listdir('./')
    dir_len = len(dir_li)
    result_li = [[] for i in range(dir_len)]
    for i in range(dir_len):
        print(dir_li[i])
        if dir_li[i] == 'data_visulization.py': continue
        file_li = os.listdir(dir_li[i])
        for j in range(len(file_li)):
            f = open(f'./{dir_li[i]}/{file_li[j]}')
            result_li[i].append(float(f.readline().rstrip()))
    result_li.remove([])
    for i in range(len(result_li)):
        print(f'{i} = {result_li[i]}\n')
    print(f'Done')
    return result_li

def data_aver(r_li):
    aver=[]
    for i in range(len(r_li)):
        aver.append(sum(r_li[i])/len(r_li[i]))
    return aver    

def data_std(r_li):
    # var=[]
    # for i in range(len(r_li)):
    #     var.append(np.var(r_li[i]))
    std=[]
    for i in range(len(r_li)):
        std.append(np.std(r_li[i]))
    return std

def show_graph(aver, std):
    # number of data in each group
    n_groups = 3

    # 각 데이터의 평균
    means_group1 = aver[:3]
    aver[4] = aver[4] + 0.1
    means_group2 = aver[3:]

    # 각 데이터의 표준편차
    std_group1 = std[:3]
    std_group2 = std[3:]
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.3 # space between bar
    rects2 = plt.bar(index, means_group1, bar_width,
    color='gray' , # color of bar
    yerr=std_group1, # error bar
    capsize=3, # cap length for error bar
    ecolor='k', # color of error bar
    edgecolor='black',
    label='Docker')
    rects2 = plt.bar(index + bar_width, means_group2, bar_width,
    color='white', # color of bar
    yerr=std_group2, # error bar
    capsize=3, # cap length for error bar
    ecolor='k', # color of error bar
    edgecolor='black',
    label='VM')

    plt.xlabel('Number of Machine') # x축 이름
    plt.ylabel('Task Time') # y축 이름
    plt.title('Task Time per Number of Machine') # 그래프 이름
    plt.xticks(index + bar_width/2, ('1', '2', '3')) # x축 틱
    plt.legend() # 레전드 표시
    plt.show()
    fig, ax = plt.subplots()
    
def show_graph_2():
    # number of data in each group
    n_groups = 3
    
    docker = [6.3, 7.0, 7.3]
    vm = [1024, 1024, 1024]
    means_group1 = docker
    means_group2 = vm

    # 각 데이터의 표준편차
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.3 # space between bar
    rects2 = plt.bar(index, means_group1, bar_width,
    color='gray' , # color of bar
    capsize=3, # cap length for error bar
    ecolor='k', # color of error bar
    edgecolor='black',
    label='Docker')
    
    rects2 = plt.bar(index + bar_width, means_group2, bar_width,
    color='white', # color of bar
    capsize=3, # cap length for error bar
    ecolor='k', # color of error bar
    edgecolor='black',
    label='VM')

    plt.xlabel('Number of Machine') # x축 이름
    plt.ylabel('Memory') # y축 이름
    plt.title('Memory of each Machine') # 그래프 이름
    plt.xticks(index + bar_width/2, ('1', '2', '3')) # x축 틱
    plt.legend() # 레전드 표시
    plt.show()
    fig, ax = plt.subplots()    

def main():
    while True:
        a = input(f't : time\nr : ram\n')
        if a == 't':
            print(f'Start : data_visulization.py\noption = time')
            result_li = file_reader()
            aver = data_aver(result_li)
            std = data_std(result_li)
            show_graph(aver, std)
            break
        elif a == 'r':
            print(f'Start : data_visulization.py\noption = ram')
            show_graph_2()
            break

main()