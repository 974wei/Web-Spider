from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
chrome_option.add_argument('--window-size=1920,1080')  # 必须指定

path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_option.binary_location = path

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service= service, options=chrome_option)

url = 'https://www.baidu.com/'
browser.get(url)
browser.save_screenshot('baidu.png')
browser.quit()

