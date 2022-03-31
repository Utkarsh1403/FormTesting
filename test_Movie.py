import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp():
    global driver,name,yor,dirname,dist,prod
    name = input("Enter the movie Name: ")
    yor = int(input("Enter the year of Release: "))
    dirname = input("Enter the Director Name: ")
    dist = input("Enter the Distributor: ")
    prod = input("Enter the Producer: ")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_Movies(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(name)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(yor)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(dirname)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(dist)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(prod)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(1)
