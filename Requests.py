from bs4 import BeautifulSoup
from selenium import webdriver


def get_url(search_term):
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_term = search_term.replace(' ', '+')
    url = template.format(search_term)
    return url


# initial variables
url = 'https://www.amazon.com'
products = {}
driver = webdriver.Chrome('/Users/<USERNAME>/Desktop/Coding/YiMian/chromedriver')
driver.minimize_window()
driver.get(get_url(input('Keyword: ')))
soup = BeautifulSoup(driver.page_source, 'html.parser')


# amazon products
results = soup.find_all('div', {'data-component-type': 's-search-result'})
price = soup.find_all('span', {'class': 'a-price-whole'})
item = results[0]

# loop through products
for i in range(len(results)):
    item = results[i]
    price_parent = item.find('span', 'a-price')
    price = price_parent.find('span', 'a-offscreen').text
    atag = item.h2.a
    description = atag.text.strip()
    products[description] = price

# visual affects
products = str(products).replace('{', '')
products = products.replace('}', '')
products = products.replace('\', \'', '\n\n\033[1;33;40m|\033[1;31;40m!\033[1;33;40m|\033[1;37;40m')
products = products.replace('\'', '\033[1;33;40m|\033[1;31;40m!\033[1;33;40m|\033[1;37;40m')
products = products.replace('$', '\033[1;36;40m$')

# finalize
print(products)
driver.quit()
