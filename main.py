from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


print("Iniciando nosso robô... \n")

driver = webdriver.Chrome("C:/Users/JMTech/Desktop/Robos/chromedriver")

driver.get('https://trends24.in/brazil/')
pesquisa = driver.find_element(By.CLASS_NAME, 'page-content__blurb').text
x = pesquisa.replace("Today's Top Twitter Trending Brazil topics are ", "")
print(x)

y = pesquisa.find("Nazismo")
print(y)
final = x[:y]

print(final)
driver.close()