#1 - Blir alltid 1
def jains(N, xi):
    teller = 0
    nevner = 0
    JFI = 0
    tellerN = N
    nevnerN = N
    nevnerNN = N
    while tellerN > 0:
        teller += xi
        tellerN -= 1
    teller = teller**2
    while nevnerN > 0:
        nevner += xi**2
        nevnerN -= 1
    nevner = nevner*N
    JFI = teller/nevner
    return JFI

print(jains(5,70))