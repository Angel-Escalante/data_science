from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Always needed
s = Service(ChromeDriverManager().install())
# Options variable to establish common options like window size
# without it, selenium will use the default options
options = Options()
# options.add_argument("--window-size = 1200, 1020")
# Makes everything at background
# options.add_argument("--headless")


def get_explorer(desired_options):
    for option in desired_options:
        options.add_argument(option)

    return webdriver.Chrome(service=s, options=options)
