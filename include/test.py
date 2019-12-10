import requests
from bs4 import BeautifulSoup as bs
import urllib.request


headers = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}

base_url = 'https://makler.md/ro/real-estate/real-estate-for-sale/apartments-for-sale/an/680734'

def parse_makler(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers = headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        div_header = soup.find_all('div', attrs={'class': 'title clrfix'})
        post_title = div_header[0].find('strong', attrs={'id': 'anNameData'}).text
        post_price = div_header[0].find('div', attrs={'class': 'item_title_price'}).text
        currency = post_price[-1:]
        post_price = post_price[:-1].strip()
        post_price = post_price.replace(' ', '')
        print('Denumirea: ' + post_title + "\nPretul: " + post_price)


        categories = soup.find_all('li', attrs={'class': 'pl'})
        list_cat = []
        for category in categories[1:]:
            list_cat.append(category.find('a').text.strip())


        print("\n\nImaginile: \n")
        div_image = soup.find('div', id = "anItemData").find('div', attrs={'class': 'itmedia'})
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)

        i = 0
        for a in div_image.find_all("a"):
            print(a['href'])
            urllib.request.urlretrieve(a['href'], "img/{}.jpg".format(str(i)))
            i += 1
            img_count = i
        content = soup.find('div', attrs={'class', 'ittext'}).text.strip()
        print(content)

        print("\n\nCaracteristica - Valoarea \n")
        uls = soup.find_all('ul', attrs={'class': 'itemtable box-columns'})
        specifications = {}
        for ul in uls:
            for li in ul.find_all('li'):
                title = li.find("div", attrs={"class": "fields"}).text.strip()
                value = li.find("div", attrs={"class": "values"}).text.strip()
                specifications[title] = value
                print(title + ' - ' + value)
            print('------')

        phone = soup.find("ul", attrs={'class', 'hlist clrfix'}).text.strip()
        print(phone)
        city = soup.find('div', attrs={'class', 'item_title_info'}).find_all('span')[0].text
        print(city)
        return post_title, post_price, list_cat, content, currency, city, img_count, specifications, phone
    else:
        print("Error")

post_title, post_price, list_cat, content, currency, city, img_count, specifications, phone  = parse_makler(base_url, headers)