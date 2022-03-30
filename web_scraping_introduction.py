from bs4 import BeautifulSoup

with open('Save a document in HTML format.html','r',encoding="utf8") as html_file:
    content=html_file.read()
    #print(content)

    soup=BeautifulSoup(content,'lxml')
    #print(soup.prettify) # to make it look pretty

    # we want to collect all the tags that are there as <p> tags tags
    # find method finds only the first instance , to change that , use find_all
    para_html_tags=soup.find_all('p')
    #print(para_html_tags)

    for paragraph in para_html_tags:
        #print(paragraph.text,'\n')
        pass

    ## anyways we will try to print all the points of th 1,2,3 of this web page

    points_cards=soup.find_all('li',class_='li') # to mention the class in html page , use class_

    for points in points_cards:
        #print(points) # to print only the text , print ( points.p.text) as used above
        main_points=points.p.text

        print(main_points)
