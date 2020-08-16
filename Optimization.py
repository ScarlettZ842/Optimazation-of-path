from math import sqrt
from itertools import combinations
def get_combination_list():
    input_num = input().split(",")
    n = input_num[0]
    initial_list = []
    for i in range(1,len(input_num)-1):
        initial_list.append((float(input_num[i]),float(input_num[i+1])))

    find_combination = []
    comb = [cmb for x in range(2, len(initial_list) + 1) for cmb in combinations(initial_list, x)]
    for tup in comb:
        if len(tup) < 2 or tup[0] != initial_list[0] or tup[len(tup) - 1] != initial_list[len(initial_list) - 1] or tuple(sorted(tup)) != tup:
            continue
        else:
            find_combination.append(tup)

    print(get_shortest_path(find_combination))
     

def get_shortest_path(combination_list):
    total_dis = 0
    dis_list  = []
    for i in range(len(combination_list)):
        for j in range(len(combination_list[i])-1):
            dis = sqrt((combination_list[i][j][0]-combination_list[i][j+1][0]) ** 2 + (combination_list[i][j][1]-combination_list[i][j+1][1]) ** 2)
            total_dis += dis
            if(dis > 100):
                combination_list[i]=[]
                total_dis = 0
                break
        dis_list.append(total_dis)
        total_dis = 0
    while 0 in dis_list:
        dis_list.remove(0)
    if (dis_list == []):
        total_dis = -1
    else:
        total_dis = '{0:.2f}'.format(min(dis_list))
    return total_dis  


def main():
    while True:
        try:
            get_combination_list()
        except EOFError:
            break

main()           
