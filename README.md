# ATC_AssignmentMoksha

def makeautomata(f, n)

input : f: takes input string of z3 formula,n: total no. of variables

output : gives final automata as result

def total_vars(n)
input : integer showing total variables present in z3 formula given in an input
output : list storing all variables x1,x2,....

def getList(f)
input : f: takes input string of z3 formula
output : creates list of atomic formulas

#this function on execution takes value from user for all variables.
def compute(f, n, lst)
input : f: takes input string of z3 formula,n: total no. of variables,lst: list of value of variables given in input
output : compute the satisfiability for given values

def computation(f, n, lst)
input : f: takes input string of z3 formula,n: total no. of variables,lst: list of value of variables given in input
output : gives evaluated formula in form of string

#functionality of this def is it consider formula used for equate(==) used in Presburger Logic
def equate(f, arg1):
input : f: takes input string of z3 formula,arg1: total no. of variables present in formula
output : returns automata stored in dictionary

#functionality of this def is it consider formula used for less than or equal to (<=) used in Presburger Logic
def lessthaneq(f, arg1):
input : f: takes input string of z3 formula,arg1: total no. of variables present in formula
output : returns automata stored in dictionary

def notop(matrix1):
input: matrix1 is dictionary which had stored automata
output: displays pretty table by applying 'not' operation


def andorop(check, arg1, matrix1, matrix2):
input: check is variable which check whether operator is 'and'/'or' ,arg1 : total vars present,matrix1/ matrix2 is automata stored in dictionary for atomic formula1/atomic formula2 between which And/Or operation is to performed.
output : displays pretty table by applying 'and'/'or' operation


__name__ == '__main__': 
string is variable in which z3 formula needs to be passed
arg1 is total number of variables taken from user as an input. 
#for demo currently "And(x1 <= 2, x1 + x2 <= 5)" is passed in string ,that can be changed to whatsoever z3 formula we want and by declaring x1,x2,..variables there,and pass total number of variables.
