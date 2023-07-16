from modules import *
''' ================================
### FOR WEBSITE XSS INJECTION ###
### THIS IS A PROTOTYPE PROJECT ###
### FOR MY FUTURE USE ONLY ###
================================ ''' 

#load data.yaml data   
def data():
    with open('resources/data.yaml') as file:
        load = yaml.load(file, Loader=yaml.FullLoader)
    
    return load

#webdriver setup
@pytest.fixture(scope="function")       
def setup():
    options = Options()
    options.add_argument("--hide-scrollbars")
    
    print("TEST START")
    yield webdriver.Chrome(options=options)
    print("TEST TEARDOWN")

#main method to call the test
def main(setup):
    setup.get(data()['main']['page'])
    setup.maximize_window()
    
    xssData(setup)

#navigates to login page
def nav(setup, xss):
    #sends a data to login text field 
    setup.find_element(By.CSS_SELECTOR, data()['main']['id']).send_keys(f"{xss}")
    sleep(1.5)
    #clicks submit button after delay
    submit = setup.find_element(By.CSS_SELECTOR, data()['main']['btn'])
    submit.click()
    sleep(2)
    #clears the login text field after sumbission
    clear = setup.find_element(By.CSS_SELECTOR, data()['main']['id'])
    clear.clear()

#loops xss scripts to the choosen element
def xssData(setup):
    encoding = 'utf-8'
    with open('resources/xss-payload.txt', 'r', encoding=encoding) as file:
        for i in file:
            data = i.strip()
            nav(setup, data)


    
