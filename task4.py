from task2 import jainsall  # HVORFOR GÅR DENNE LINJEN INN I task2.py????
# import task2

with open("fil2.txt") as fil:
    liste = []
    for i in fil:
        if "Kbps" in i:
            liste.append(int(i.split()[0])/1000)
        else:
            liste.append(int(i.split()[0]))

print("Task 4:")
jainsall(liste)
