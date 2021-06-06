from selenium import webdriver

#Function that gets the pokemon moveset data
#Returns the pokemon class object

def GetPokemon(pokemon):
    smogon_link = "https://www.smogon.com/dex/ss/pokemon/" + pokemon

    chrome_driver_path = "C:\Development\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(smogon_link)

    pokemon_name = driver.find_element_by_xpath('//*[@id="container"]/div/main/div/h1').text

    #check if has moveset
    try:
        #if pokemon has a moveset
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

    driver.close()

    #Return True if there is a valid moveset
    #Return false if there is no moveset
    if success:
        pokemon_moveset = {
            "name": pokemon_name,
            "move_one": move_one,
            "move_two": move_two,
            "move_three": move_three,
            "move_four": move_four,
            "nature": nature,
            "ability": ability,
            "item": item,
            "evs": evs
        }
        return [True, f"{pokemon_name} does have a moveset available in SwSh", pokemon_moveset]
    else:
        return [False, f"{pokemon_name} does not have a moveset in SwSh", {}]


