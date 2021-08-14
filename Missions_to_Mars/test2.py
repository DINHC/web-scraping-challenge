import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup

def scrape3():
    url = "https://redplanetscience.com"

    executable_path = {'executable_path': 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe'}
    browser = Browser('chrome', executable_path = 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe', headless=False)
    browser.visit(url) 
    html= browser.html   
    
    
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.body.prettify())


    news_title = soup.find('div', class_='content_title')
    print(news_title)


    news_p = soup.find('div', class_='article_teaser_body')
    print(news_p)

    # mars_data['news_title'] = news_title
    # mars_data['news_p'] = news_p


    recent_title = "3 Things We've Learned From NASA's Mars InSight" 
    recent_news_p = "Scientists are finding new mysteries since the geophysics mission landed two years ago."

    url = 'https://spaceimages-mars.com/'
    executable_path = {'executable_path': 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe'}
    browser = Browser('chrome', executable_path = "C:/Users/dinhc/OneDrive/Documents/chromedriver.exe", headless=False)
    browser.visit(url)
    img_html=browser.html



    image_soup = BeautifulSoup(img_html, 'html.parser')
    print(image_soup)



    image = image_soup.find_all('div', class_='thmbgroup')
    image



    image_a = image_soup.find_all('a', class_='fancybox-thumbs')
    image_a


    image_path = image_soup.find('img', class_='thumbimg')['src']
    image_path



    featured_image_url = f'https://spaceimages-mars.com/{image_path}'
    print(featured_image_url)

    # mars_data['featured_image_url'] = featured_image_url


    fact_url = 'https://galaxyfacts-mars.com/'
    execetable_path = {'executable_path': 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe'}
    browser = Browser('chrome', executable_path = "C:/Users/dinhc/OneDrive/Documents/chromedriver.exe", headless=False)
    browser.visit(fact_url)
    mars_fact=browser.html



    fact_soup = BeautifulSoup(mars_fact,'html.parser')
    fact_soup


    fact_table = fact_soup.find('table', class_='table table-striped')
    column1 = fact_table.find_all('th')
    column2 = fact_table.find_all('td')

    descriptions = []
    values = []

    for row in column1:
        description = row.text.strip()
        descriptions.append(description)
    
    for row in column2:
        value = row.text.strip()
        values.append(value)
    
    mars_facts = pd.DataFrame({
        "Description":descriptions,
        "Value":values
        })

    mars_facts_html = mars_facts.to_html()
    mars_facts

    # mars_data['mars_facts'] = mars_facts_html

    hemi_url = 'https://marshemispheres.com/'
    execetable_path = {'executable_path': 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe'}
    browser = Browser('chrome', executable_path = "C:/Users/dinhc/OneDrive/Documents/chromedriver.exe", headless=False)
    browser.visit(hemi_url)
    mars_hemi=browser.html



    hemi_soup = BeautifulSoup(mars_hemi,'html.parser')



    print(hemi_soup.body.prettify())


    items = hemi_soup.find_all('div', class_='item')
    items
    

    hemi_image_urls = []

    for img in items:
        title = img.find('h3').text
        image_url = img.find('a', class_='itemLink product-item')['href']
        browser.visit(hemi_url + image_url)
        image_url = browser.html    
        image_soup = BeautifulSoup(image_url, 'html.parser')
        hemi_img_path = image_soup.find('img', class_='wide-image')['src']
        full_img_url = f'https://marshemispheres.com/{hemi_img_path}'
        hemi_image_urls.append({
            "title": title,
            "full_image_url": full_img_url
        })
    hemi_image_urls

    # mars_data['hemisphere_imgs'] = hemi_image_urls

    data = {
       "news_title": news_title,
       "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_facts,
        "mars_hemi":mars_hemi
    }
    return data
    # return mars_data