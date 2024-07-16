# спарсить данные с сайта divan.ru, (можно использовать либо Scrapy, либо selenium),
# но теперь ещё и сохраните информацию в csv файл.
# # К дз прикрепляем ссылку на репозиторий с файлом csv и кодом.

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.divan.ru/syktyvkar/category/tovary_dla_doma')


sorted_data = []
data_row = []
headings = ['nn','item_name', 'price', 'link']
nn = 0

with open("goods.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    for i in browser.find_elements(By.CLASS_NAME, 'wYUX2'):
        name = i.find_element(By.TAG_NAME, 'span')
        price = i.find_element(By.CLASS_NAME, 'ui-LD-ZU.KIkOH')
        for element in i.find_elements(By.TAG_NAME, 'a'):
            link = element.get_attribute("href")
        #print(name.text)
        #print(price.text)
        #print(link)
        nn += 1
        data_row = [nn, name.text, price.text, link]
        sorted_data.append(data_row)
    writer.writerows(sorted_data)


browser.quit()