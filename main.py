import pprint
from tabulate import tabulate
a = int #number of character in alphabet#
q = int #number of states
I = int #initial state position
T = int
Q = []

def showtab(f):
    f.seek(0)
    a = int(f.readline())
    p = int(f.readline())
    init = f.readline()
    term = f.readline()
    x = int(f.readline())
    kar = " "
    tab = [[[kar for i in range(a)] for j in range(a)] for k in range(p)]
     # x est la ligne y la colone et z la sous colone

    temp= []
    standard =True
    deterministic = True
    for u in range(0,x):
        carrier = 0
        temp = f.readline()
        tempo = 0
        if temp[1] == "a":
            tempo = 0
        if temp[1] == "b":
            tempo = 1
        if temp[1] == "c":
            tempo = 2
        if tab[int(temp[0])][tempo][carrier]!= " ":
            carrier = 1
            deterministic = False

        if int(temp[0])<=x:
            tab[int(temp[0])][tempo][carrier] = int(temp[2])

        for i in range(2,int(init[0])*2+1,2):

            if temp[2] == init[i]:
                standard = False
                print("there is a transisition coming on initial state: the transition",temp[0],"->",temp[1],"->",temp[2],"\n the initial state is",init[i])
    if int(init[0]) > 1:
        standard = False
        deterministic = False
        print("There are more than on initial state so the automata is not standard and not deterministic")


    if standard:
        print("\nthis automaton is standard")
    if deterministic:
        print("\nthis Automata is deterministic")
    else:
        print("\nthis automaton is not deterministic")
    return tab,deterministic,standard


def menu():
    m = int(input(" Pick an automaton to use, from 1 to 44\n"))

    file = "int3-6-"
    file_open = file+str(m)+".txt"
    print(file_open,"\n\n")
    f = open(file_open,'r')
    return f,m


def show_info(f):
    a = f.readline()
    p = f.readline()
    I = f.readline()
    T = f.readline()
    print(a, "is the number of character in the alphabet of this automata\n")
    print(p, "is the number of states\n")
    q = int(p)
    for i in range(0, q):
        Q.append(i)
    print("Q = ", Q)
    print(a, "is the number of character in the alphabet of this automata\n")
    nb_init = int(I[0])
    print("there is/are ",nb_init," initial state(s)")
    set_init = []
    for i in range(2,2*nb_init + 1,2):

        set_init.append(I[i])
    set_terminal = []
    nb_teminal = int(T[0])
    for i in range(2, 2 * nb_teminal + 1, 2):
        set_terminal.append(T[i])

    print("the position of the initial state(s) are : ", set_init)
    print("the position of the terminal state(s) are : ",set_terminal)


def print_tab(f,tab,deterministic):
    f.seek(0)
    a = int(f.readline())
    p = int(f.readline())
    init = f.readline()
    term = f.readline()
    nb_init = int(init[0])
    nb_term = int(term[0])
    set_init = []
    set_term = []
    counter =0
    x=0
    for k in range(2, 2 * nb_init + 1, 2):
        set_init.append(init[k])

    for k in range(2, 2 * nb_term + 1, 2):
        set_term.append(term[k])
    if deterministic:
        print("        |____a____|____b____|")
    else:
        print("        |_____a_____|_____b_____|")
    for i in range(0,p):
        if i<nb_term:
            vf = int(set_term[i])
        if i<nb_init:
            vb = int(set_init[i])
        if vf ==i and vb!=i:
            print("<- ", end="")

        if vb == i and vf:
            print("-> ",end="")
        if vb!=i and vf!=i:
            print("   ",end="")
        if vb == i == vf:
            print("<->",end="")
        if deterministic:
            print(" ",i," |   ",tab[i][0][0],"   |   ",tab[i][1][0],"   |")
        if deterministic == False:
            if tab[i][0][1] != " ":
                print(" ", i, " |  ", tab[i][0][0],",",tab[i][0][1], "  |    ", tab[i][1][0], "    |")
            else:
                print(" ", i, " |    ", tab[i][0][0], "    |    ", tab[i][1][0], "    |")
    print(set_term," end")
    return tab

def standardisation(f,tab,standard,m):
    f.seek(0)
    a = int(f.readline())
    p = int(f.readline())
    init = f.readline()
    term = f.readline()
    nb_init = int(init[0])
    nb_term = int(term[0])
    set_init = []
    set_term = []
    set_init.append("I")
    kar = " "
    counterx = 0
    countery = 0
    nb_transi = int(f.readline())
    new_Init_states = [[kar for i in range(3)] for j in range(nb_transi)]
    new_inputx = []

    new_inputy = []

    for k in range(2, 2 * nb_init + 1, 2):
        set_init.append(init[k])

    for k in range(2, 2 * nb_term + 1, 2):
        set_term.append(term[k])

    print("new transition : \n")
    for i in range(0,nb_transi):

        transi = f.readline()
        if transi[0] in set_init:
            print("I",transi[1],transi[2])
            new_Init_states[i][0] = "I"
            new_Init_states[i][1] = transi[1]
            new_Init_states[i][2] = transi[2]
            stringer = str(new_Init_states[i][0]+new_Init_states[i][1]+new_Init_states[i][2])
            print(stringer)
            if transi[1] =='a':
                new_inputx.insert(0,int(transi[2]))
                countery += 1
            if transi[1] == 'b':
                new_inputy.insert(0,int(transi[2]))


    last_inset=[new_inputx,new_inputy]
    tab.insert(0, last_inset)
    pprint.pprint(tab)
    return tab



    #récupérer les transitions des état initiaux.

        # create transition from I to the transition of past Initial states
def print_tab_from_tab(f,tab,standardised):
    f.seek(0)
    a = f.readline()
    q = f.readline()
    q = int(q)
    print(a,"\n")
    a = int(a)
    init = f.readline()
    term = f.readline()
    nb_init = int(init[0])
    nb_term = int(term[0])
    set_init = []
    set_term = []
    counter = 0
    x = 0
    for k in range(2, 2 * nb_init + 1, 2):
        set_init.append(init[k])

    for k in range(2, 2 * nb_term + 1, 2):
        set_term.append(term[k])
    print("      ",end="")
    for i in range(97,97+a):

        print("_____",chr(i),"_____|",end="")
    print(" ")
    for i in range(0,q+1):
        if i<nb_term:
            vf = int(set_term[i])
        if i<nb_init:
            vb = int(set_init[i])
        if vf ==i and vb!=i:
            print("<- ", end="")

        if vb == i and vf:
            print("-> ",end="")
        if vb!=i and vf!=i:
            print("   ",end="")
        if vb == i == vf:
            print("<->",end="")
        if standardised:
            if i==0:
                print("I",end="   | ")
            else:
                print(i-1,end="   | ")
        for k in range(0,a):
            print(end="   ")
            for r in range(0,a):
                if tab[i][k][r]== " ":
                    print("",end="")
                else:
                    print(tab[i][k][r],end=",")
                if r ==a-1 :
                    print(end="    |")
            print(end="   ")
        print(" ")









def main():
    f = menu()

    show_info(f[0])
    x =showtab(f[0])
    tab =print_tab(f[0],x[0],x[1])
    if x[2] == False:
        standardisation(f[0],tab,x[2],f[1])
        stanardized = True
        print_tab_from_tab(f[0],tab,stanardized)

    print(tabulate(tab, headers='a b c', tablefmt='fancy_grid'))
    return 0

main()
