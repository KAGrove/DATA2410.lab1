from task2 import jainsall  # HVORFOR GÅR DENNE LINJEN INN I task2.py????
# import task2

with open("fil.txt") as fil:
    liste = []
    for i in fil:
        liste.append(int(i.split()[0]))

print("Task 3:")
jainsall(liste)
