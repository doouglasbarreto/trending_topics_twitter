import os
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from selenium import webdriver
from selenium.webdriver.common.by import By

print("Iniciando nosso robô... \n")
dir_path = os.getcwd()
chromedriver = os.path.join(dir_path, "chromedriver.exe")
driver = webdriver.Chrome(chromedriver)

driver.get('https://trends24.in/brazil/')
pesquisa = driver.find_element(By.CLASS_NAME, 'page-content__blurb').text
aux = "".join(pesquisa.splitlines())
x = aux.replace("Today's Top Twitter Trending Brazil topics are ", "")

y = x.find(". Tweet")
final = x[:y]

final2 = final.split(",")
final2[0] = " " + final2[0]

contador = 0
meufinal = ""
for a in final2:
    contador += 1
    meufinal += str(contador) + "º -" + str(a) + "\n"

print(meufinal)


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    windowExample.setFixedWidth(300)
    windowExample.setFixedHeight(300)
    windowExample.setWindowTitle('Trending Topics')
    windowExample.label = QLabel(meufinal, windowExample)
    windowExample.show()
    sys.exit(app.exec_())

driver.close()
basicWindow()

