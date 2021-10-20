import itertools
import queue

from z3 import *
from prettytable import PrettyTable
import math

atomic_formulas_list = []
automata_list = []
op = []
unknown_var = []


def total_vars(n):
    for i in range(1, n+1):
        unknown_var.append(eval('x'+str(i)))




def getList(f):
    if str(f.decl()) == '<=' or str(f.decl()) == '==':
        atomic_formulas_list.append(f)
        return
    elif str(f.decl()) == 'Not':
        getList(f.arg(0))
        op.append(f.decl())
    else:
        getList(f.arg(0))
        getList(f.arg(1))
        op.append(f.decl())
        return


def compute(f, n, lst):
    if str(f.decl()) == '<=':
        value = computation(f, n, lst)
        if value:
            return True
        else:
            return False
    elif str(f.decl()) == '==':
        value = computation(f, n, lst)
        if value:
            return True
        else:
            return False
    if str(f.decl()) == 'And':
        return compute(f.arg(0), n, lst) and compute(f.arg(1), n, lst)
    elif str(f.decl()) == 'Or':
        return compute(f.arg(0), n, lst) or compute(f.arg(1), n, lst)
    elif str(f.decl()) == 'Not':
        return not compute(f.arg(0), n, lst)


def computation(f, n, lst):
    value = []
    for i in range(0, n):
        value.append((unknown_var[i], IntVal(lst[i])))
    result = substitute(f, value)
    return eval(str(result))



def equate(f, arg1):
    lst = [list(i) for i in itertools.product([0, 1], repeat=arg1)]
    matrix = {}
    dict = {}
    totalcomb = int(math.pow(2, arg1))
    c = f.arg(1).as_long()
    show = []
    row = []
    queu = []
    dict[c] = 1
    queu.append(c)
    t = PrettyTable(['State'])
    column = []
    for j in range(0, totalcomb):
        ele = ''
        for k in range(0, arg1):
            ele = ele + str(lst[j][k])
        column.append(ele)
    for i in range(0, len(column)):
        t.add_column(column[i], [''])
    t.del_row(0)
    initial = 1
    while len(queu):
        key = queu.pop(0)
        value = dict[key]
        if value == 1:
            num = key
            # num1 = key
            flag = 0
            dict[num] = 0
            if num == c and initial:
                show.append(str(num) + 'IF')
                flag = 1
                initial = 0
            elif num == c:
                show.append(str(num) + 'F')
            else:
                show.append(str(num))

            for i in range(0, totalcomb):
                if str(num) != 'Err':
                    num1 = num - computation(f.arg(0), arg1, lst[i])
                    l = num1 / 2
                    if (math.floor(l) is not math.ceil(l)):
                        l = 'Err'
                    else:
                        l = int(l)
                else:
                    l = 'Err'

                num1 = num
                show.append(str(l))
                row.append(l)
                if not l in dict:
                    dict[l] = 1
                    queu.append(l)
            if flag:
                num1 = str(num1) + 'F'
            else:
                num1 = str(num1)
            matrix[num1] = row[:]
            t.add_row(show)
            show.clear()
            row.clear()
            print(t)
    return matrix


def lessthaneq(f, arg1):
    lst = [list(i) for i in itertools.product([0, 1], repeat=arg1)]
    print(f)
    matrix = {}
    dict = {}
    totalcomb = int(math.pow(2, arg1))
    c = f.arg(1).as_long()
    show = []
    row = []
    queu = []
    dict[c] = 1
    queu.append(c)
    t = PrettyTable(['State'])
    column = []
    for j in range(0, totalcomb):
        ele = ''
        for k in range(0, arg1):
            ele = ele + str(lst[j][k])
        column.append(ele)
    for i in range(0, len(column)):
        t.add_column(column[i], [''])
    t.del_row(0)
    initial = 1
    while len(queu) > 0:
        key = queu.pop(0)
        value = dict[key]
        if value == 1:
            num = key
            dict[num] = 0
            if num >= 0 and initial:
                show.append(str(num) + 'IF')
                initial = 0
            elif num >= 0:
                show.append(str(num) + 'F')
            else:
                show.append(str(num))

            for i in range(0, totalcomb):
                num1 = num - computation(f.arg(0), arg1, lst[i])
                l = math.floor(num1/2)
                num1 = num
                show.append(str(l))
                row.append(l)
                if not l in dict:
                    dict[l] = 1
                    queu.append(l)
            if num1 >= 0:
                num1 = str(num1) + 'F'
            else:
                num1 = str(num1)
            matrix[num1] = row[:]
            t.add_row(show)
            show.clear()
            row.clear()
            # print("a")
            print(t)
    return matrix


def notop(matrix1):
    lst = [list(i) for i in itertools.product([0, 1], repeat=arg1)]
    matrix = {}
    dict = {}
    intial = 1
    initial = 1
    totalcomb = int(math.pow(2, arg1))
    show = []
    t = PrettyTable(['State'])
    column = []
    for j in range(0, totalcomb):
        ele = ''
        for k in range(0, arg1):
            ele = ele + str(lst[j][k])
        column.append(ele)
    for i in range(0, len(column)):
        t.add_column(column[i], [''])
    t.del_row(0)
    final_state1 = []
    for i in (matrix1.keys()):
        if str(i[-1]) == 'F':
            final_state1.append(str(i))
    for i in matrix1:
        # print(i)
        if i not in final_state1:
            matrix[str(i) + 'F'] = matrix1[i]
        else:
            matrix[str(i[:-1])] = matrix1[i]
    for i in range(0, len(matrix1)):
        if str(list(matrix1.keys())[i]) in final_state1:
            if initial:
                show.append(str(list(matrix1.keys())[i])[:-1] + 'I')
                initial = 0
            else:
                show.append(str(list(matrix1.keys())[i])[:-1])
        else:
            show.append(str(list(matrix1.keys())[i]) + 'F')
        for rowelement in (matrix1[list(matrix1.keys())[i]]):
            show.append(rowelement)
        t.add_row(show)
        show.clear()
    print(t)
    return matrix


def andorop(check, arg1, matrix1, matrix2):
    lst = [list(i) for i in itertools.product([0, 1], repeat=arg1)]
    totalcomb = int(math.pow(2, arg1))
    t4 = PrettyTable(['State'])
    row = []
    column = []
    for j in range(0, totalcomb):
        ele = ''
        for k in range(0, arg1):
            ele = ele + str(lst[j][k])
        column.append(ele)
    for i in range(0, len(column)):
        t4.add_column(column[i], [''])
    t4.del_row(0)
    queu1 = []
    matrix = {}
    show = []
    dict3 = {}
    c = list(matrix1.keys())[0]
    length = len(c)
    if str(c[-1]) == 'F':
        c = c[:-1]
    c2 = list(matrix2.keys())[0]
    if str(c2[-1]) == 'F':
        c2 = c2[:-1]
    final_state1 = []
    final_state2 = []
    final_state = []

    for i in (matrix1.keys()):
        if str(i[-1]) == 'F':
            final_state1.append(i[:- 1])
    for i in (matrix2.keys()):
        if i[-1] == 'F':
            final_state2.append(i[: - 1])

    dict3[(c, c2)] = 1
    pair = (c, c2)
    queu1.append(pair)
    initial = 1
    while len(queu1):
        key = queu1.pop(0)
        value = dict3[key]
        if value == 1:
            num = key
            val_1 = list(num)[0]
            val_2 = list(num)[1]
            flag = 0
            if val_1 in final_state1 and val_2 in final_state2 and check == 'And':
                if initial:
                    show.append('<' + str(num) + '>IF')
                    initial = 0
                elif initial == 0:
                    show.append('<' + str(num) + '>F')
                final_state.append(key)
                flag = 1
            elif check == 'Or':
                if val_1 in final_state1 or val_2 in final_state2:
                    if initial:
                        show.append('<' + str(num) + '>IF')
                        initial = 0
                    elif initial == 0:
                        show.append('<' + str(num) + '>F')
                    final_state.append(key)
                    flag = 1
            else:
                if initial:
                    initial = 0
                    show.append('<' + str(num) + '>I')
                else:
                    show.append('<' + str(num) + '>')
            dict3[num] = 0

            for i in range(0, totalcomb):
                if val_1 in final_state1:
                    val_1 = val_1 + 'F'
                if val_2 in final_state2:
                    val_2 = val_2 + 'F'

                row_ele_1 = matrix1[val_1][i]
                row_ele_2 = matrix2[val_2][i]
                l = (str(row_ele_1), str(row_ele_2))
                row.append(l)
                show.append('<' + str(l) + '>')
                if not l in dict3:
                    queu1.append(l)
                    dict3[l] = 1
            t4.add_row(show)
            if flag:
                num = str(num) + 'F'
            else:
                num = str(num)
            matrix[num] = row[:]
            show.clear()
            print(t4)
    return matrix





def makeautomata(f, n):
    string = str(f)
    getList(f)
    arg1 = n
    solver = Solver()
    final_state = []
    total_vars(arg1)
    k = 0
    for i in atomic_formulas_list:
        no_of_arg = arg1
        if str(i.decl()) == '==':
            automata_list.append(equate(atomic_formulas_list[k], no_of_arg))
        else:
            automata_list.append(lessthaneq(atomic_formulas_list[k], no_of_arg))
        k = k + 1

    k = 0
    result_table = automata_list[0]
    for i in op:
        if str(i) == 'And' or str(i) == 'Or':
            result_table = andorop(str(i), arg1, result_table, automata_list[k + 1])
        elif str(i) == 'Not':
            result_table = notop(result_table)
    lst = []
    for i in range(0, arg1):
        x = int(input())
        lst.append(x)
    evaluate_expression = compute(f, arg1, lst)
    if evaluate_expression:
        string = string + "is True"
        print(string)
    else:
        string = string + "is False"
        print(string)

if __name__ == '__main__':
    x1 = Int('x1')
    x2 = Int('x2')
    x3 = Int('x3')
    string = "And(x1 <= 2, x1 + x2 <= 5)"
    arg1 = int(input())
    f = eval(string)
    makeautomata(f, arg1)
