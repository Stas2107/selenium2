from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def search_wikipedia(query):
    # Настраиваем драйвер браузера
    driver = webdriver.Chrome()
    driver.get("https://ru.wikipedia.org")

    # Вводим запрос в поисковую строку
    search_input = driver.find_element(By.NAME, "search")
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)

    # Ждем загрузки страницы
    time.sleep(2)

    while True:
        # Получаем список параграфов
        paragraphs = driver.find_elements(By.CSS_SELECTOR, 'div.mw-parser-output > p')
        # Действия пользователя
        print("\nЧто вы хотите сделать далее?")
        print("1: Просмотреть параграфы текущей статьи")
        print("2: Перейти на связанную страницу")
        print("3: Выйти из программы")
        choice = input("Введите ваш выбор (1, 2 или 3): ")

        if choice == '1':
            # Печатаем параграфы
            for i, paragraph in enumerate(paragraphs):
                print(f"\nПараграф {i+1}:")
                print(paragraph.text)
        elif choice == '2':
            # Получаем связанные статьи
            links = driver.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p > a")
            print("\nДоступные связанные статьи:")
            for i, link in enumerate(links):
                print(f"{i+1}: {link.get_attribute('title')}")

            link_choice = int(input("Выберите статью для перехода: ")) - 1
            if 0 <= link_choice < len(links):
                links[link_choice].click()
                time.sleep(2)
            else:
                print("Неверный выбор.")
        elif choice == '3':
            print("Выход из программы...")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")

    driver.quit()

# Начало программы
if __name__ == "__main__":
    initial_query = input("Введите ваш запрос для поиска на Википедии: ")
    search_wikipedia(initial_query)
