a = int #number of character in alphabet#
q = int #number of states
I = int #initial state position
T = int
Q = []

f = open("automate_1", "r")
a = f.readline()
p = f.readline()
I = f.readline()
T = f.readline()
print(a, "is the number of character in the alphabet of this automata\n")
print(p, "is the number of states\n")
q = int(p)
for i in range(0 , q):
    Q.append(i)
print("Q = ", Q)
print(a, "is the number of character in the alphabet of this automata\n")
f.close()