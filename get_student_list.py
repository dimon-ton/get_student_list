from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from chromedriver_autoinstaller.utils import get_chromedriver_path
from chromedriver_autoinstaller.utils import get_chrome_version
from chromedriver_autoinstaller import install

import time
import csv

install()

path = '{}/{}/chromedriver.exe'.format(get_chromedriver_path(), get_chrome_version()[:3])

service = Service(path)
driver = webdriver.Chrome(service=service)


def writetocsv(data, filename='data.csv'):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)

def auth():
    driver.get('https://portal.bopp-obec.info/obec65/auth/login')

    with open('auth.txt', 'r') as file:
        username = file.readline().strip()
        password = file.readline().strip()


    username_inpurt = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/form/div[1]/div/input').send_keys(username)
    password_input = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/form/div[2]/div/input').send_keys(password)

    login_submit = driver.find_element(By.ID,'btnSubmit').click()


def get_student_data():
    student_path_list = ['https://portal.bopp-obec.info/obec65/student/?schoolCode=21020024&studentNo=&code=&cifNo=&cifType=&educationYear=2565&levelDtlCode=&classroom=&firstNameTh=&lastNameTh=&fatherFirstNameTh=&fatherLastNameTh=&motherFirstNameTh=&motherLastNameTh=&parentFirstNameTh=&parentLastNameTh=&homelessCode=&occasionCode=&deformityCode=&poorBookFlag=false&poorFoodFlag=false&poorStationeryFlag=false&poorUniformFlag=false&action=search&page.page=1',
    'https://portal.bopp-obec.info/obec65/student/?schoolCode=21020024&studentNo=&code=&cifNo=&cifType=&educationYear=2565&levelDtlCode=&classroom=&firstNameTh=&lastNameTh=&fatherFirstNameTh=&fatherLastNameTh=&motherFirstNameTh=&motherLastNameTh=&parentFirstNameTh=&parentLastNameTh=&homelessCode=&occasionCode=&deformityCode=&poorBookFlag=false&poorFoodFlag=false&poorStationeryFlag=false&poorUniformFlag=false&action=search&page.page=2',
    'https://portal.bopp-obec.info/obec65/student/?schoolCode=21020024&studentNo=&code=&cifNo=&cifType=&educationYear=2565&levelDtlCode=&classroom=&firstNameTh=&lastNameTh=&fatherFirstNameTh=&fatherLastNameTh=&motherFirstNameTh=&motherLastNameTh=&parentFirstNameTh=&parentLastNameTh=&homelessCode=&occasionCode=&deformityCode=&poorBookFlag=false&poorFoodFlag=false&poorStationeryFlag=false&poorUniformFlag=false&action=search&page.page=3']

    

    all_student = []

    for p in student_path_list:
        driver.get(p)

        try:
            for i in range(1, 61):
                one_student = {}

                id_number = driver.find_element(By.XPATH ,'/html/body/div/div/div/div/form/div/table/tbody/tr[{}]/td[8]'.format(i)).text
                prename = driver.find_element(By.XPATH ,'/html/body/div/div/div/div/form/div/table/tbody/tr[{}]/td[10]'.format(i)).text
                fname = driver.find_element(By.XPATH ,'/html/body/div/div/div/div/form/div/table/tbody/tr[{}]/td[11]'.format(i)).text
                lname = driver.find_element(By.XPATH ,'/html/body/div/div/div/div/form/div/table/tbody/tr[{}]/td[13]'.format(i)).text
                class_s = driver.find_element(By.XPATH ,'/html/body/div/div/div/div/form/div/table/tbody/tr[{}]/td[5]'.format(i)).text
                
                one_student['id_number'] = id_number
                one_student['prename'] = prename
                one_student['name'] = fname
                one_student['lastname'] = lname
                one_student['class'] = class_s

                all_student.append(one_student)


    
        except:
            pass
  

    return all_student
    


auth()
get_student_data()

# write to csv

all_s = get_student_data()

for i, row in enumerate(all_s):
    id_name = all_s[i].get('id_number')
    prename = all_s[i].get('prename')
    name = all_s[i].get('name')
    lastname = all_s[i].get('lastname')
    class_s = all_s[i].get('class')

    writetocsv([id_name, prename, name, lastname, class_s])

driver.quit()