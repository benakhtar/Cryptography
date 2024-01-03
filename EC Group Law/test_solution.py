from solution import *

def test_add1():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 33227206799745974112838855428403975028
    yP = 280118436162424571832678322380561219983
    xQ = 223163296791121639203572946539964643516
    yQ = 278177692610883241496556396767842945629
    P = (xP, yP)
    Q = (xQ, yQ)
    assert add(P,Q,A,B,p) == (294516489680224657840123244275561844835,235587176374220745000182467632786269435)

def test_add2():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 33227206799745974112838855428403975028
    yP = 280118436162424571832678322380561219983
    P = (xP,yP)
    assert add(P,None,A,B,p) == P

def test_add3():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 33227206799745974112838855428403975028
    yP = 280118436162424571832678322380561219983
    P = (xP,yP)
    assert add(None,P,A,B,p) == P

def test_add4():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 33227206799745974112838855428403975028
    yP = 280118436162424571832678322380561219983
    P = (xP,yP)
    assert add(P,(xP,60163930758513891630696285051206991524),A,B,p) == None
def test_dbl():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 113862812304360361264986269199922369645
    yP = 311116554897176068902406699961155123436
    P = (xP, yP)
    assert dbl(P,A,B,p) == (195471863250563985204036528553770218482,137603684255177465133474131270146963323)

def test_neg():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 113862812304360361264986269199922369645
    yP = 311116554897176068902406699961155123436
    P = (xP, yP)
    assert neg(P,p)[0] == P[0] and neg(P,p)[1] == ((-P[1])%p)

def test_smul1():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 68692703456160136042464563679376820376
    yP = 130544953344972447178452211243139673091
    P = (xP, yP)
    n = 73601158533265639
    assert smul(n,P,A,B,p) == (90474951937153459050709482902870269560, 188616914752362793381546788473546992736)

def test_smul2():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 68692703456160136042464563679376820376
    yP = 130544953344972447178452211243139673091
    P = (xP, yP)
    n = 340282366920938463494251139727355310047
    assert smul(n,P,A,B,p) == None

def test_smul3():
    p = 340282366920938463463374607431768211507
    A = 45103086313416866932931723356576649487
    B = 170368493225177264668154842245814352889
    xP = 68692703456160136042464563679376820376
    yP = 130544953344972447178452211243139673091
    P = (xP, yP)
    n = -5
    assert smul(n,P,A,B,p) == (108571879462990973771781298283614265196, 150172160280183644524387988315227478709)