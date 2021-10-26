from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import selenium
df=pd.read_csv("Make_My_Trip.csv",index_col=False)
nam=df.Name
frm=df.From
to=df.To
df['Date Of Journey']= pd.to_datetime(df['Date Of Journey'])
mont = df['Date Of Journey'].dt.strftime('%B')
driver = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.makemytrip.com/')

time.sleep(2)



#from part

from1=driver.find_element_by_id("fromCity")
time.sleep(2)
from1.send_keys(frm)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input").send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input").send_keys(Keys.ENTER)

#done
time.sleep(2)
#to
to1=driver.find_element_by_id("toCity")

select=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/input")
select.send_keys(to)
time.sleep(3)
select.send_keys(Keys.ARROW_DOWN)
select.send_keys(Keys.ENTER)



#done
# journey date under-process

caln = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[3]/label")
caln.send_keys(Keys.ENTER)

dt_tab=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]")
dt_tab2=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]")
import re
s=list(mont)

#mon=re.sub(r'[0-9]+','',mon).strip()

s=s[0]
'''


mon=str(mon)
print(type(mon))
print(mon)

'''

flag="False"
while flag=="False":
    m_nam=dt_tab.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div")
    nam1=m_nam.text

    m_nam1=dt_tab2.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div")
    nam2=m_nam1.text

    if nam1.startswith(s):
        dt1=dt_tab.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[5]")
        #print(dt1.text)
        dt1.send_keys(Keys.ENTER)

        flag = "True"

    elif nam2.startswith(s):
        dt2=dt_tab2.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div[5]")
        dt2.send_keys(Keys.ENTER)
        flag = "True"
    else:
        nxt_click=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]")
        nxt_click.send_keys(Keys.ENTER)
#search btn


ss = driver.find_element_by_xpath("//a[contains(text(),'Search')]")
driver.execute_script("arguments[0].click();", ss)
time.sleep(5)
newt = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div/span")
newt.click()


next_proces=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]")
pric=next_proces.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/label[1]/span")


tab_nam=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div[1]")
nam=tab_nam.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/span")


#print(f"Flight name :-{nam.text} And price :-{pric.text}")

a=nam.text
price=pric.text
df["Flight_Name"]=a
df["Fare"]=price
df["Status"]="Successfull"
df.to_csv('Updated_MMT.csv')

driver.quit()

print("Ticket Booked...")
