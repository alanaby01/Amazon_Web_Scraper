import requests
from bs4 import BeautifulSoup
def shorten_url(url):
    if url.find("www.amazon.in")!=-1:
        index=url.find("/dp/")
        if index!=-1:
            index2=index+14
            url="https://www.amazon.in"+url[index:index2]
        else:
            index=url.find("/gp/")
            if(index!=-1):
                index2=index+22
                url="https://www.amazon.in"+url[index:index2]
            else:
                url=None
    else:
        url=None
    return url

headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

def price_convertor(price):
    stripped_price=price.strip()
    new_price=stripped_price[2:]
    replaced_price=new_price.replace(",","")
    find_dot=replaced_price.find(".")
    to_convert_price=replaced_price[0:find_dot]
    converted_price=int(to_convert_price)

    return converted_price

def get_product_details(url):
    headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
    details={"Name":"","price":0,"deal":True,"url":""}
    _url = shorten_url(url)
    if _url =="":
        details = None
    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")
        if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["deal"] = False
        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = price_convertor(price.get_text())
            details["url"] = _url
        else:
            return None
    return details
print(get_product_details("https://www.amazon.in/dp/B07HGJJ58K"))

