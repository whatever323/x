from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem
from pickle import*
from numpy import*



#1 2
def saisir():
    n=w.L1.text()
    if(n.isdecimal()==False):
        QMessageBox.information(w,"ereur","invalide")
    N=int(n)
    if not (1<N<50):
        QMessageBox.information(w,"ereur","il faut 1<n<50")
        
    if not(distinct(n)):
        QMessageBox.critical(w,"ok","n gotta be distinct")
    else:
        QMessageBox.information(w,"ereur","it is distinct")
        
    f = open("terme.txt", "a")
    if exist(n) == False:
        f.write(str(n)+"\n")
        f.close()
        QMessageBox.information(w, "OK", "Ajout avec succès")
    else:
        f.close()
        QMessageBox.critical(w, "Erreur", "n déjà existe")
        
#4       
def save():

    if not w.RB.isChecked() and not w.RB1.isChecked():
        QMessageBox.critical(w, "Erreur", "Choisir votre suite 1 ou 2")

    if w.CB.currentText() == "choisir":
        QMessageBox.critical(w, "Erreur", "Mode d'affichage ?")

    QMessageBox.information(w, "Succès", "Le fichier a été recréé")

    f1 = open("suites.dat", "wb")
    f = open("terme.txt", "r")

    w.tab.setRowCount(0)

    sudo_x = w.CB.currentText()
    typeS = "suite1"
    if w.RB1.isChecked():
        typeS = "suite2"
    x=f.readline()

    while(x!=""):
        X = int(x.strip())
        if sudo_x == "n":
            if typeS == "suite1":
                value = suite1(X)
            else:
                value = suite2_rec(X)

            e= {
                "rang": X,
                "valeur": value,
                "type_suite": typeS
            }

            dump(e, f1)
            print("Saved:", e)
        x=f.readline()

    f.close()
    f1.close()

    
        
    
def afficher():
    f1=open("suites.dat","rb")
    w.tab.setRowCount(0)
    k=0
    test=True
    while(test):
        try:
            e=load(f1)
            w.tab.insertRow(k)
            w.tab.setItem(k,0,QTableWidgetItem(str(e["rang"])))
            w.tab.setItem(k,1,QTableWidgetItem(str(e["valeur"])))
            w.tab.setItem(k,2,QTableWidgetItem(e["type_suite"]))
            k=k+1
        except:
            test=False
    f1.close()
    

        
def effacer():
    w.L1.clear()
    w.RB.setChecked(False)
    w.RB1.setChecked(False)
    w.tab.clear()
    w.CB.setCurrentText("choisir")        

#suite
#3
def suite1(N):
    u=2
    for i in range(2,N+1):
        u=2*u+1
        return u
        
def suite1_rec(N):
    if N==1:
        return 2
    else:
        return 2*suite1_rec(N)+1
    
def suite2(N):
    u1=1
    u2=1
    for i in range(3,N):
        U=u1+u2
        u1=u2
        u2=U
        return u2
        
def suite2_rec(N):
    if N==1 or N==2:
        return 1
    else:
        return suite2_rec(N-1)+suite2_rec(N-2)
    



#saisir
#1 2
def exist(n):
    f = open("terme.txt", "r")
    n = str(n)
    test = False

    ch = f.readline()
    while ch != "" and not(test):
        if ch.strip() == n:
            test = True
        ch = f.readline()

    f.close()
    return test
       
def distinct(n):
    s = n
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


app = QApplication([])
w = loadUi("projet.ui")
w.show()
w.B1.clicked.connect(saisir)
w.B2.clicked.connect(save)
w.B3.clicked.connect(afficher)
w.B4.clicked.connect(effacer)
app.exec_()