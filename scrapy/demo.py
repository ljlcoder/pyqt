
import requests
import BeautifulSoup
import re
def get_chapter(url):
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})
    if response.status_code != 200:
        return None
    soup=BeautifulSoup(res.text,"html.parse")
    data=[]
    for dd in soup.find_all("dd"):
        a=dd.find("a")
        href=a.get("href","")
        if re.match(r"/html/\d+/\d+\.html",href):
            data.append({
                "href":"https://www.biququ.com"+href,
                "title":a.get_text()
            })
    return data
def get_content(url):
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'})
    if response.status_code != 200:
        return None
    soup=BeautifulSoup(res.text,"html.parse")
    content=soup.find("div",id="content")
    return content.get_text("\n","")
if __name__ == "__main__":
    res=get_chapter('https://www.biququ.com/html/21627/')
    data=get_content(res[0]["href"])
    print(data)