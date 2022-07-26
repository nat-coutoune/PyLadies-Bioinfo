
from Bio import SeqIO

max_total = 0
file = SeqIO.parse("test_ros.txt", "fasta")
print(file)

for number, record in enumerate(SeqIO.parse("test_ros.txt", "fasta")):
    G = str(record).count("G")
    C = str(record).count("C")
    A = str(record).count("A")
    T = str(record).count("T")

    total = ((G+C) / (len(record.seq)))*100
    total2 = round(
        (((G+C) / (G+C+T+A)) * 100), 6)


    print(len(record))
    print((G+C+T+A))
    print(G)
    print(C)
    print(A)
    print(T)
    print(total2)
    print(total)
  





'''
if total >= max_total:
    max_total = total
    id = record.id

print(f">{id}")
print(max_total)
'''