# спарсить данные с сайта divan.ru, (можно использовать либо Scrapy, либо selenium),
# но теперь ещё и сохраните информацию в csv файл.
# # К дз прикрепляем ссылку на репозиторий с файлом csv и кодом.

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.divan.ru/syktyvkar/category/tovary_dla_doma')

ggg = browser.find_elements(By.CLASS_NAME, 'wYUX2')
sorted_data = []
headings = ['nn','item_name', 'price', 'link']
nn = 0
with open("goods.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    for i in ggg:
        nn += 1
        item_name = i.get_attribute('name')

        price = i.find_element(By.CLASS_NAME, 'span.ui-LD-ZU.KIkOH').text



        link = i.get_attribute('href')
        sorted_data.append([nn, item_name, price, link])
    writer.writerows(sorted_data)



browser.quit()