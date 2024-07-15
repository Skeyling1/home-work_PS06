# спарсить данные с сайта divan.ru, (можно использовать либо Scrapy, либо selenium),
# но теперь ещё и сохраните информацию в csv файл.
# # К дз прикрепляем ссылку на репозиторий с файлом csv и кодом.

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.divan.ru/syktyvkar/category/dekor')


