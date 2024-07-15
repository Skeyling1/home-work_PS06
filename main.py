# спарсить данные с сайта divan.ru, (можно использовать либо Scrapy, либо selenium),
# но теперь ещё и сохраните информацию в csv файл.
# # К дз прикрепляем ссылку на репозиторий с файлом csv и кодом.

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.divan.ru/syktyvkar/category/tovary_dla_doma')

ggg = browser.find_elements(By.CLASS_NAME, 'wYUX2')




headings = ['n/n','item_name', 'price', 'link']
with open("goods.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headings)














browser.quit()