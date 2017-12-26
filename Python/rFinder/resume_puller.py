
from getpass import getpass
from splinter import Browser
from bs4 import BeautifulSoup as BS
import re, sys, operator, time, getopt, random, urllib2

#==== Configs ====#
LOGIN_URL = 'https://secure.indeed.com/account/login?'
query = str(raw_input("search term (ie. linux administrator): "))
while True:
    if query:
        query = str(query)
        print "Searching for %s" % query 
        break
    else:
        print "Need to query something, using default(splunk).."
        query = 'splunk'
        break

RESUMES_URL = 'http://www.indeed.com/resumes?q="' + query + '"&co=US'

INDEED_USERNAME = ''
#INDEED_USERNAME = ''

### Filter designed search resumes based on keywords
        
def main():
    filter = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:f", ["help", "output="])
    except getopt.GetoptError as err:
        print str(err)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print """usage: resumeParse.py [-h] [-f] <file>
                     
                 -h : Print this help message and exit
                 -f : Name of file you want to match results to
                 """
            sys.exit()
        elif opt in ("-f", "--filter"):
            filter = sys.argv[2]
        else:
            assert False, "unhandled option"
    INDEED_PASSWORD = getpass('Indeed Password: ')
    #var = raw_input("City, State you want to search(Reston, VA): ")
    var = None
    if var == None:
        SEARCH_LOCATION = ''
    else:
        SEARCH_LOCATION = str(var)

    KEYWORDS = {}
    
    # Open new firefox browser window, login to indeed.com
    #br = Browser('firefox')
    executable_path = {'executable_path':'C:\Users\INSERT_EXE_PATH'}
    br = Browser('chrome', **executable_path)
    br.visit(LOGIN_URL)
    br.fill_form({'__email':INDEED_USERNAME,'__password':INDEED_PASSWORD})
    br.find_by_css('.btn-signin').first.click()
    time.sleep(1)
        
    resume_links = []
    resume_index = 0
    cookie = br.cookies.all()
    print cookie
    while True:
        ##############################################################################
        #TODO make this function work in urllib2, so we don't have to visit the site after we get the cookie
        #getter = urllib2.build_opener()
        #getter.addheaders.append(('Cookie', "; ".join('%s=%s'% (k,v) for k,v in cookie.items())))
        #starting_url = RESUMES_URL + '&start=%d' % resume_index
        #try:
            #p = getter.open(starting_url)
        #except:
            #print "Opening " + starting_url
            #p = urllib2.urlopen(starting_url)
            #e = sys.exc_info()[0]
            #print "Error: %s" % e
            #break

        #slop = BS(p.read(), 'html.parser')
        #links = slop.select(".app_link")
        #print slop
        #print links
        ##############################################################################

        br.visit(RESUMES_URL + '&start=%d' % resume_index)
        links = br.find_by_css('.app_link')

        if len(links) > 0:
            # Iterate over all the links from the search results
            for link in links:
            # Rewrite this. The Browser object cannot find the href value for some reason...
                resume_links.append('http://www.indeed.com' + re.search(r'href=[\'"]?([^\'" >]+)', link.outer_html).group(1))   
            resume_index += 50
            ### This 'if' is used for testing and can be commented out if necessary
            #if resume_index > 2500:
            #   resume_index = 1
            #   break
        else:
            resume_index = 1
            break

    print '[+] Resume Links Found: %d' % len(resume_links)
    
    for resume in resume_links:
        ### Code to test urllib2 cookie capabilities ------------
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', "; ".join('%s=%s' % (k,v) for k,v in cookie.items())))
        #opener.addheaders.append(('Cookie', 'cookiename=cookievalue'))
        try:
            f = opener.open(resume)
        except:
            resume_index +=1
            continue
        #print f.read()
        #---------------------------------------------------------------
        #br.visit(resume)
        int = random.uniform(4,7)
        time.sleep(int)
        
        try:
            #contact = re.search(r'([A-Z].*)\/', br.url).group(1)
            #soup = BS(br.html, 'html.parser')

            soup = BS(f.read(), 'html.parser')
            contact = soup.find(id="resume-contact", class_="fn").get_text()
            text = soup.find(class_="hresume").get_text()
            location = soup.find(class_="locality").get_text()
            title = soup.title.string
            
            if title == "Page not found | Indeed.com":
                resume_index += 1
                continue
            else:
                pees = soup.find_all('p')
                for p in pees:
                    if p.string == "The resume you requested could not be found.":
                        continue
        except:
            resume_index += 1
            e = sys.exc_info()[0]
            #print "Error1: %s" % e
            continue
        
        try:
            f = open(contact + "_" + query + "_" + location, 'w')
        except:
            e = sys.exc_info()[0]
            print "Error3: %s" % e

        try:
            if text:
                f.write(text.encode('utf-8'))
            else:
                print "text not populated"
                pass

            #print "made it here"
            #f.write((br.html).encode('utf-8'))
            f.close()
        except:
            e = sys.exc_info()[0]
            print "Error4: %s" % e
        
        resume_index += 1
        sys.stdout.write('[+] Sanning Resumes: {0:.0f}%\r'.format(float(resume_index)/len(resume_links) * 100))
        sys.stdout.flush()
    
    br.quit()

if __name__ == '__main__':
    main()