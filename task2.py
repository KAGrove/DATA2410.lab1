def jainsall(liste):
    teller = nevner = 0

    for i in liste:
        teller += i
        nevner += i**2

    teller = teller**2
    nevner = len(liste)*nevner

    print('JFI er: ', teller / nevner)


liste1 = [1,6,9]
jainsall(liste1)