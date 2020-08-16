def find(value_list, second_line, vertex): #parent nodes must be the operation values
    if second_line[vertex] not in ['*','+']:
       return int (second_line[vertex])

    if second_line[vertex] == '+':
        ans = 0 # initial value of addtion should be 0

    elif second_line[vertex] == '*':
        ans =1  # initial value of multiplication shoule be 1

    for i in range(len(value_list[vertex])) :
        if second_line[vertex] == '+':
            ans = ans + find(value_list, second_line, value_list[vertex][i]) # do the recursion for addition parent
        elif second_line[vertex] == '*':
            ans = ans* find(value_list, second_line, value_list[vertex][i]) # do the recursion for multiplication parent
    return ans


def get_ansresult():
    value_list = list()
    line_a = input()
    line_b = input()
    a = line_a.split(',')
    b = line_b.split(',')
    a = [int(x) for x in a]

    for n in range(len(a)) :
       value_list.append(list())

    root = 0
    for n in range(len(a)) :
        if a[n] == -1:
            root = n
        else:
            value_list[a[n]].append(n)
    print(str(find(value_list, b, root)))

def main():
    while True:
        try:
            get_ansresult()
        except EOFError:
            break
        

main()
