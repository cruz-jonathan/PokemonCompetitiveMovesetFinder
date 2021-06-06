from selenium import webdriver
import requests

pokemon = input("What Pokemon are you looking for?")

smogon_link = "https://www.smogon.com/dex/ss/pokemon/" + pokemon

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(smogon_link)

pokemon_name = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/h1').text

#check if has moveset
try:
    moveset = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div')
    #if pokemon has a moveset
    print(pokemon_name + " has an available moveset")
    success = True
    
    #Get Data from moveset
    move_one = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr[1]/td/ul/li/a/span').text
    move_two = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td/ul/li/a/span').text
    move_three = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr[3]/td/ul/li[1]/a/span').text
    move_four = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr[4]/td/ul/li[1]/a/span').text
    nature = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div/div/div[2]/table/tbody/tr[3]/td/ul/li/abbr').text
    ability = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div/div/div[2]/table/tbody/tr[2]/td/ul/li/a/span').text
    item = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td/ul/li/a/span/span[3]').text
    evs = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/section/section[2]/div/div[2]/div[2]/div/div/div/div[2]/table/tbody/tr[4]/td/ul').text

except:
    #if pokemon does not have a moveset
    success = False
    print(pokemon_name + " does not have an available moveset")

if success:
    print(move_one)
    print(move_two)
    print(move_three)
    print(move_four)
    print(ability)
    print(nature)
    print(item)
    print(evs)

driver.close()