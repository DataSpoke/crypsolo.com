import re, sys, operator
from splinter import Browser
from getpass import getpass
from bs4 import BeautifulSoup as BS

#==== Configs ====#
LOGIN_URL   = 'https://secure.indeed.com/account/login?'
RESUMES_URL = 'http://www.indeed.com/resumes?f=contacted'

INDEED_USERNAME = ''
INDEED_PASSWORD = getpass('Indeed Password: ')

KEYWORDS = {}

def gen_comword_list():
    with open('thousandwords.txt', 'r') as f:
        return map(lambda s: s.strip(), f.readlines())
        
def parse_resume_words(html, common_words):
    unique_words = []
    s = BS(html, 'html.parser')
    resume_body = s.find('div', {'id':'resume_body'})
    for child in resume_body.children:
        for word in child.text.replace('-', ' ').replace('.', ' ').replace('(', '').replace(',', '').replace(')', '').split():
            if not word.lower() in unique_words and not word in common_words:
                unique_words.append(word.lower())
            else:
                pass
    return unique_words
            
        
def main():
    # Open new firefox browser window, login to indeed.com
    br = Browser('firefox')
    br.visit(LOGIN_URL)
    br.fill_form({'__email':INDEED_USERNAME,'__password':INDEED_PASSWORD})
    br.find_by_css('.btn-signin').first.click()   
    
    resume_links = []
    resume_index = 0
    
    while True:
        br.visit(RESUMES_URL + '&start=%d' % resume_index)
        links = br.find_by_css('.app_link')
        if len(links) > 0:
            for link in links:
            # Rewrite this. The Browser object cannot find the href value for some reason...
                resume_links.append('http://www.indeed.com' + re.search(r'href=[\'"]?([^\'" >]+)', link.outer_html).group(1))   
            resume_index += 50
        else:
            resume_index = 1
            break

    print '[+] Resume Links Found: %d' % len(resume_links)
    
    # Load the 1,000 most commonly used words into common_words
    sys.stdout.write('[+] Loading Common Word List [    ]')
    common_words = gen_comword_list()
    sys.stdout.flush()
    sys.stdout.write('\r[+] Loading Common Word List [DONE]\n')   
    
    for resume in resume_links:
        br.visit(resume)
        try:
            #print '[+] Scanning %s\'s Resume...' % br.find_by_id("resume-contact").text        
            resume_words = parse_resume_words(br.html, common_words) 
            #print '\tUnique Words Found: %d' % len(resume_words)
            for word in resume_words:
                if not word in KEYWORDS:
                    KEYWORDS[word] = 1
                else:
                    KEYWORDS[word] += 1      
        except:
            pass
        sys.stdout.write('[+] Sanning Resumes: {0:.0f}%\r'.format(float(resume_index)/len(resume_links) * 100))
        sys.stdout.flush()
        resume_index += 1  
            
    print '\n[+] Total Unique Keywords Found: %d' % len(KEYWORDS.keys())
    print '============\nTOP 20 WORDS\n============'
    for pair in sorted(KEYWORDS.items(), key=operator.itemgetter(1), reverse=True)[:20]:
        print '%s: %d' % (pair[0], pair[1])
    
if __name__ == '__main__':
    main()