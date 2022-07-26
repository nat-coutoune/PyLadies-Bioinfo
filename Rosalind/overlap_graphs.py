

f = open("rosalind_grph.txt","r") 
k = 3
lines = f.readlines()
id = []
seq = []
# Carrego o arquivo txt fornecido por rosalind e meu arquivo .
# Reforma para ajustar os dados de entrada.
def reform(lines):
    for line in lines:
        if line.startswith(">"):
            a = line.replace(">", "")
            a = a.replace("\n", "")
            id.append(a)
        else:
            if len(id) > len(seq):
                line = line.replace("\n","")
                seq.append(line)
            else:
                line = line.replace("\n", "")
                seq[len(id) - 1] = seq[len(id) - 1] + line
    return id , seq
id, seq = reform(lines)

s = []
t = []

for i in range(len(id)):
    for j in range(len(seq)):

        if i != j:
            if seq[i][-k:] == seq[j][:k]:
                s.append(id[i])
                t.append(id[j])

for i in range(len(s)):
    print(s[i] + " " + t[i])

f.close()
