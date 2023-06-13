# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.chrome.options import Options
import time
import os

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

browser = webdriver.Chrome(options=options)
browser.maximize_window()
try:
    # Переход на https://sbis.ru/
    browser.get('https://sbis.ru/')
    time.sleep(2)
    # В Footer'e нходит "Скачать СБИС"
    sbis_download = browser.find_element(By.LINK_TEXT, "Скачать СБИС")
    time.sleep(3)
    # Переход по ссылке
    sbis_download.location_once_scrolled_into_view
    sbis_download.click()
    time.sleep(3)
    # Скачивание СБИС Плагин в папку с данным тестом
    tab_plugin = browser.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    tab_plugin.click()
    time.sleep(2)
    sbis_plugin = browser.find_element(By.XPATH, '//a[contains(@href, "setup-web.exe")]')
    link_sbis_plugin = sbis_plugin.get_attribute("href")
    browser.get(link_sbis_plugin)
    time.sleep(10)

    # Убедиться, что плагин скачался
    filename = Path(link_sbis_plugin).name
    plugin_path = os.path.join(os.getcwd(), filename, )
    assert os.path.exists(plugin_path), 'Плагин не скачан'

    # Вывести на печать размер скачанного файла в мегабайтах
    print(f'Размер скачанного файла = {round(os.path.getsize(plugin_path) / 1024 ** 2, 2)} Mb')
finally:
    browser.quit()
    