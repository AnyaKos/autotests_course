# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import time

browser = webdriver.Chrome()
browser.maximize_window()
try:
    browser.get("https://fix-online.sbis.ru/")
    time.sleep(1)
    # Авторизация на сайте https://fix-online.sbis.ru/
    user_login, user_password = 'testov_ivan', 'Jensov123'
    login = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    time.sleep(2)
    password = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)
    time.sleep(5)
    # Переход в реестр Контакты
    contacts = browser.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    contacts.click()
    time.sleep(2)
    contacts_button = browser.find_element(By.CSS_SELECTOR,
                                           '[data-qa="NavigationPanels-SubMenu__head"] [data-qa="Контакты"]')
    contacts_button.click()
    time.sleep(2)
    plus_but = browser.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    plus_but.click()
    time.sleep(2)
    search = browser.find_element(By.CSS_SELECTOR, '[data-qa="controls-Render__field"] .controls-InputBase__nativeField')
    search.send_keys('Тестовый', Keys.ENTER)
    time.sleep(2)
    search.send_keys(Keys.ENTER)
    time.sleep(2)
    # Отправка сообщение самому себе
    text_message = browser.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    text_message.send_keys("Сообщение для автотеста")
    time.sleep(2)
    send_message = browser.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_message.click()
    time.sleep(5)
    # Сообщение появилось в реестре
    all_message = browser.find_elements(By.CSS_SELECTOR, '.controls-MasterDetail_details .controls-ListViewV')
    action_chains = ActionChains(browser)
    time.sleep(2)
    action_chains.context_click(all_message[0]).perform()
    time.sleep(3)
    context_menu = browser.find_element(By.CSS_SELECTOR, '.controls-Popup')
    # Удаление этого сообщения
    del_msg = browser.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
    del_msg.click()
    time.sleep(3)
finally:
    browser.quit()
