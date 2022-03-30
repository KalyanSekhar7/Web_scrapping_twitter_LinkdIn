from bs4 import BeautifulSoup
# published job advertisements from website
import requests

# requesting an information from the website
html_text=requests.get('https://in.linkedin.com/jobs/data-science-intern-jobs?keywords=Data%20Science%20Intern&location=India&locationId=&geoId=102713980&f_TPR=&f_E=1&position=1&pageNum=0').text
#print(html_text)
# 200 response in web means that the access is successful ( in web applications )
soup=BeautifulSoup(html_text,'lxml')
# the developmental stage
#job=soup.find('ul',class_='jobs-search__results-list')
job=soup.find('ul',class_='jobs-search__results-list')
#print(job)
position=job.find('h3',class_='base-search-card__title').text.replace(' ','')
print(position) # we can see that we have som white spaces , and we want it to remove(replace it with nothing)
company_name=job.find('a',class_='hidden-nested-link').text.replace(' ','')
print(company_name)