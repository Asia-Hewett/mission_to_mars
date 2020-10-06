#!/usr/bin/env python
# coding: utf-8

# In[21]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import pandas as pd
import requests
import os
from pprint import pprint


# In[22]:


URL = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
result = requests.get(URL) 

# Explored using the following parser

soup = bs(result.text, "html.parser")
# pprint(soup)


# In[23]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA Mars News

# In[8]:


news_title = soup.find('div', class_="content_title").find('a').text
print(f'The latest NASA article is titled: {news_title}')


# In[9]:


news_p = soup.find('div', class_="rollover_description_inner").text
print(f'{news_p}')


# # JPL Mars Space Images - Featured Image

# In[84]:


executable_path = {'executable_path': 'C:/Users/asiah/Documents/git_repos/mission_to_mars/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[25]:


mars_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(mars_url)


# In[43]:


featured_image = browser.find_by_id("full_image")
featured_image.click()


# In[73]:


src = browser.find_by_css('article')['style']
print(src)


# In[78]:


background_image_url = "/spaceimages/images/wallpaper/PIA17448-1920x1200.jpg"


# In[81]:


featured_image_url = mars_url + background_image_url
featured_image_url


# # Mars Facts

# In[194]:


mars_facts_url = "https://space-facts.com/mars/"


# In[204]:


mars_facts_html = pd.read_html(mars_facts_url)

mars_facts_df = mars_facts_html[0]

mars_facts_df.columns = ['Description', 'Value']

mars_facts_df


# In[207]:


# mars_facts_table = mars_facts_df.to_html('mars_facts_table.html')


# # Mars Hemispheres

# In[135]:


mars_hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemi_url)


# In[136]:


# Cerberus
cerberus_hemisphere = browser.find_by_tag("h3")
cerberus_hemisphere.click()


# In[137]:


open_button = browser.find_by_id("wide-image-toggle")
open_button.click()


# In[138]:


c_url = browser.find_by_tag('img[class="wide-image"]')['src']
print(c_url)


# In[140]:


# Schiaparelli
schiaparelli_hemisphere = browser.find_by_tag("h3")[1]
schiaparelli_hemisphere.click()


# In[141]:


open_button = browser.find_by_id("wide-image-toggle")
open_button.click()


# In[142]:


s_url = browser.find_by_tag('img[class="wide-image"]')['src']
print(s_url)


# In[144]:


# Syrtis Major
syrtis_major_hemisphere = browser.find_by_tag("h3")[2]
syrtis_major_hemisphere.click()


# In[145]:


open_button = browser.find_by_id("wide-image-toggle")
open_button.click()


# In[146]:


sm_url = browser.find_by_tag('img[class="wide-image"]')['src']
print(sm_url)


# In[147]:


# Valles Marineris 
valles_marineris_hemisphere = browser.find_by_tag("h3")[3]
valles_marineris_hemisphere.click()


# In[148]:


open_button = browser.find_by_id("wide-image-toggle")
open_button.click()


# In[149]:


vm_url = browser.find_by_tag('img[class="wide-image"]')['src']
print(vm_url)


# In[150]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": vm_url},
    {"title": "Cerberus Hemisphere", "img_url": c_url},
    {"title": "Schiaparelli Hemisphere", "img_url": s_url},
    {"title": "Syrtis Major Hemisphere", "img_url": sm_url},
]

hemisphere_image_urls

