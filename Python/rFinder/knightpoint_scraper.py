import re
import time
import urllib2
import requests
from bs4 import BeautifulSoup as BS
from doc_scrape import plain_text
from doc_scrape import html

#==== Configs ====#
JOB_LISTING = 'https://careers-knightpoint.icims.com/jobs/search?pr='

KNIGHTPOINT_USERNAME = ''
# User Agent strings
ChromLatest = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
ChromeOlder = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36"
Firefox = "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
    
def spider(links):
    for link in links:
        response = requests.get(link)
        soup = BS(response.content, "html.parser")
        page_text = str(soup.find_all('li')) + str(soup.find_all('p'))
        for_charlie = re.search(r'-\s(.*)<\/title>', str(soup.title)).group(1)
        #qual = soup.find_all(text=True)
        qual = soup.find_all(attrs={'class': re.compile(r'.*\biCIMS_Expandable_Text\b.*')})
        
        text = re.split('; |< |> |  |, |; |: |\w+', page_text)
        
        just_text = []
        for word in text:
            just_text.append(word)
        
        for i in qual:
            for x in range(3):
                stringorbuffer = i.contents[x]
                try:
                    filt = re.search(r'\<.*\>', stringorbuffer)
                    print html(i.contents[x])
                    #print filt
                except:
                    print html(i.contents[x])
                
        print for_charlie + ":\n"
        #print plain_text(page_text)-\s(.*)<\/title>
        
        
def search_iframes(xiter):
    job_listing = JOB_LISTING + str(xiter)
    response = requests.get(job_listing)
    soup = BS(response.content, "html.parser")
    linksOdd = soup.find_all('iframe')
    if linksOdd:
        destination = []
        for frame in linksOdd:
            response = urllib2.urlopen(frame.attrs['src'])
            iframe_soup = BS(response, "html.parser")

            for element in (iframe_soup.find_all('a')):
                link = re.search(r'(https?:\/\/?[\da-z\.-]+\/\w+\/\d+\/.*iframe=1)', str(element))
                try:
                    destination.append(link.group(0))
                    #print link.group(0)
                except AttributeError:
                    pass
            spider(destination)
    else:
        print "Didn't find any links.."
        
def main():
    for x in range(4):
        search_iframes(x)
    

        
    
if __name__ == '__main__':
    main()