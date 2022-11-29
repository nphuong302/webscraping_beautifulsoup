from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def shopping_list():
    print('Please choose category: ')
    category = input('>')
    html = requests.get('https://libeworkshop.com/collections/newlookbook')
    url = html.url
    data = html.text
    soup = BeautifulSoup(data, 'lxml')
    item_img = soup.find_all('div', class_ ='product-img')
    item_info = soup.find_all('div', class_ = 'product-detail clearfix')

    for index, img in enumerate(item_img):
        name = item_info[index].find('h3', class_ = 'pro-name').text.strip()
        if category.lower() in name.lower():
            href = img.a['href']
            link = urljoin(url, href)
            name = item_info[index].find('h3', class_ = 'pro-name').text.strip()
            price = item_info[index].find('div', class_ = 'box-pro-prices').text.strip()
            # tag = img.find('div', class_ = 'labeltag')
            print(f'{name} costs {price}')
            print(f'More info: {link}\n')

if __name__ == '__main__':
    shopping_list()
    