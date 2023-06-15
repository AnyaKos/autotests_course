# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
try:
    browser.get("https://sbis.ru/")
    time.sleep(1)
    # Поиск кнопки Контакты
    btn_contacts = browser.find_element(By.CSS_SELECTOR, "[href='/contacts']")
    # Переход в раздел "Контакты"
    btn_contacts.click()
    time.sleep(1)
    # Поиск баннера Тензор
    btn_tensor = browser.find_element(By.CSS_SELECTOR, '[href="https://tensor.ru/"]')
    # Клик по баннеру Тензор
    btn_tensor.click()
    time.sleep(1)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    # Проверка на то, что есть блок новости "Сила в людях"
    block_sila = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-Index__card-title')
    assert block_sila.text == 'Сила в людях', 'Нет блока "Сила в людях"'
    time.sleep(2)
    # Переход в этом блоке в "Подробнее"
    btn_about = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg [href="/about"]')
    btn_about.location_once_scrolled_into_view
    btn_about.click()
    time.sleep(3)
    #  Проверка на то, что открывается https://tensor.ru/about
    assert browser.current_url == "https://tensor.ru/about", 'Открыт другой сайт'
finally:
    browser.quit()

