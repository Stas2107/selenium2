from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

# Настройка драйвера и переход на нужную страницу
browser = webdriver.Chrome()
browser.get('https://phdays.com/forum/program/?date=2024%2F5%2F23&filterType=location')
time.sleep(5)  # Даем время для полной загрузки страницы

# Находим все элементы с нужным классом
doclades = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl and "TalkCard_content-area" in cl:
        doclades.append(element.text)

# Создаем новую книгу Excel
wb = Workbook()
ws = wb.active

# Записываем данные в первый столбец
for idx, doclade in enumerate(doclades, 1):
    ws[f'A{idx}'] = doclade

# Сохраняем книгу
wb.save("doclades.xlsx")

# Закрываем браузер
browser.quit()