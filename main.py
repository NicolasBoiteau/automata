import pprint

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

    pprint.pprint(tab)
    print(deterministic,standard)
    return tab,deterministic,standard


def menu():
    m = int(input(" Pick an automaton to use : \n-----1-----\n-----2-----\n-----3-----\n-----4-----\n"))
    if m ==1:
        f = open("automate_1")
    if m ==2:
        f = open("automate_2")
    return f


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


def main():
    f = menu()
    show_info(f)
    x =showtab(f)
    print_tab(f,x[0],x[1])
    return 0
main()
