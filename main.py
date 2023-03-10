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
    tab = [[[0 for i in range(a)] for j in range(a)] for k in range(p)]
    pprint.pprint(tab)



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


def main():
    f = menu()
    show_info(f)
    showtab(f)
    return 0
main()
