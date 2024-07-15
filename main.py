# спарсить данные с сайта divan.ru, (можно использовать либо Scrapy, либо selenium),
# но теперь ещё и сохраните информацию в csv файл.
# # К дз прикрепляем ссылку на репозиторий с файлом csv и кодом.

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.divan.ru/syktyvkar/category/tovary_dla_doma')

ggg = browser.find_elements(By.CLASS_NAME, 'wYUX2')




headings = ['no.','item_name', 'price', 'link']
no = 0
with open("goods.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    for i in ggg:
        no += 1
        item_name = i.get_attribute('name')
        price = i.get_attribute('price')
        print(price)
        print(item_name)
















browser.quit()