# спарсить данные с сайта divan.ru, (можно использовать либо Scrapy, либо selenium),
# но теперь ещё и сохраните информацию в csv файл.
# # К дз прикрепляем ссылку на репозиторий с файлом csv и кодом.

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.divan.ru/syktyvkar/category/tovary_dla_doma')


sorted_data = []
headings = ['nn','item_name', 'price', 'link']
nn = 0
with open("goods.csv", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headings)
    for i in browser.find_elements(By.CLASS_NAME, 'wYUX2'):
        nn += 1
        #item_name = i.find_element(By.CLASS_NAME,'wYUX2')
        #print(item_name)

        #price = i.find_element(By.CLASS_NAME, 'span.ui-LD-ZU.KIkOH').text

        sorted_data.append([nn, ])
    writer.writerows(sorted_data)



browser.quit()