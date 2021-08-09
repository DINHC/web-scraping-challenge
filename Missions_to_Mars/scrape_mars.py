#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect



app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)


db = client.marsDB
collection = db.marsdata
def scrape():
    mars_data = {}
# In[2]:

    url = "https://redplanetscience.com"
# mars_request = requests.get(url)
    executable_path = {'executable_path': 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe'}
    browser = Browser('chrome', executable_path = 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe', headless=False)
    browser.visit(url) 
    html= browser.html   
    


# In[3]:


    soup = BeautifulSoup(html, 'html.parser')
    print(soup.body.prettify())


# In[4]:



    news_title = soup.find('div', class_='content_title')
    print(news_title)


# In[5]:


    news_p = soup.find('div', class_='article_teaser_body')
    print(news_p)

    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p


# In[6]:


    recent_title = "3 Things We've Learned From NASA's Mars InSight" 
    recent_news_p = "Scientists are finding new mysteries since the geophysics mission landed two years ago."


# In[7]:

    url = 'https://spaceimages-mars.com/'
    executable_path = {'executable_path': 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe'}
    browser = Browser('chrome', executable_path = "C:/Users/dinhc/OneDrive/Documents/chromedriver.exe", headless=False)
    browser.visit(url)
    img_html=browser.html


# In[8]:


    image_soup = BeautifulSoup(img_html, 'html.parser')
    print(image_soup)


# In[9]:


    image = image_soup.find_all('div', class_='thmbgroup')
    image


# In[10]:


    image_a = image_soup.find_all('a', class_='fancybox-thumbs')
    image_a


# In[11]:


    image_path = image_soup.find('img', class_='thumbimg')['src']
    image_path


# In[12]:


    featured_image_url = f'https://spaceimages-mars.com/{image_path}'
    print(featured_image_url)

    mars_data['featured_image_url'] = featured_image_url

# In[13]:

    fact_url = 'https://galaxyfacts-mars.com/'
    execetable_path = {'executable_path': 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe'}
    browser = Browser('chrome', executable_path = "C:/Users/dinhc/OneDrive/Documents/chromedriver.exe", headless=False)
    browser.visit(fact_url)
    mars_fact=browser.html


# In[14]:


    fact_soup = BeautifulSoup(mars_fact,'html.parser')
    fact_soup


# In[15]:


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

    mars_data['mars_facts'] = mars_facts_html

# In[16]:

    hemi_url = 'https://marshemispheres.com/'
    execetable_path = {'executable_path': 'C:/Users/dinhc/OneDrive/Documents/chromedriver.exe'}
    browser = Browser('chrome', executable_path = "C:/Users/dinhc/OneDrive/Documents/chromedriver.exe", headless=False)
    browser.visit(hemi_url)
    mars_hemi=browser.html


# In[17]:


    hemi_soup = BeautifulSoup(mars_hemi,'html.parser')


# In[18]:


    print(hemi_soup.body.prettify())


# In[19]:


    items = hemi_soup.find_all('div', class_='item')
    items
    


# In[20]:


    hemi_image_urls = []


# In[21]:


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

    mars_data['hemisphere_imgs'] = hemi_image_urls


# In[22]:


# jupyter nbconvert to script mission_to_mars.ipynb --output scrape_mars

    return mars_data