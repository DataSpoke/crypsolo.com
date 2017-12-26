#!/usr/bin/python
#Authors: Cyle DeLucca, Kaleb Patterson, Joy Wietz
#Company: iSenpai, LLC

import json, time, sys, getopt
from indeed import IndeedClient

client = IndeedClient(6530305070078808)

filter = dict(
    snippet='snippet',
    city='city',
    company='company',
    jobtitle='jobtitle',
    jobkey='jobkey',
    arl='url',
)

params = {
    'l' : "virginia",
    'q' : "python, splunk",
    'userip' : "1.2.3.4",
    'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)",
    'format' : "json",
    'limit' : "50",
}

def unique_list(list):
    myset = set(list)
    return myset

def job_deets(job_key):
    return client.jobs(jobkeys = job_key)
    
##Options for inline -i word search, file with -f, and -l for location 
def main(argv):
    count = 0
    inline = ''
    fileList = ''
    try:
        opts, args = getopt.getopt(argv,"hi:l:f")
    except getopt.GetopError:
        print """indeedAPI-Job_Search.py -i <string> -l <location> -f <file>
            <string> : comma separated list or single term
            <location> : city, state, or zip
            <file> : query using a file of search terms"""
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print """indeedAPI-Job_Search.py -i <string> -l <location> -f <file>
            <string> : comma separated list or single term
            <location> : city, state, or zip
            <file> : query using a file of search terms"""
            sys.exit()
        elif opt in ("-i"):
            params["q"] = arg
        elif opt in ("-f"):
            fileList = arg
        elif opt in ("-l"):
            params["l"] = arg
            
    ##Output to file option with default of $datetime.results
    filename = time.strftime("%y%m%d-%H%M%S") + '-' + params['q'] + '-' + params['l']
    outputFile = open(filename, 'w')

    search_response = client.search(**params)
    jayson = json.dumps(search_response)
    #print json.dumps(search_response, indent=4, sort_keys=True)
    jason = json.loads(jayson)
    keys_job = []

    for para in jason["results"]:
        #print para
        if filter['snippet'] in para:
            for key, value in filter.iteritems():
                ##Format results
                outputFile.write(value + " : ")
                outputFile.write(para[value].encode('utf-8'))
                outputFile.write('\n')
                keys_job.append(para[filter['jobkey']])
                #print value + " : " + para[value].encode('utf-8')
            #print '---------------\n'
            outputFile.write('-------------\n')
            count += 1  
    outputFile.close()
    uniq_keys = list(unique_list(keys_job))

    
    for deets in (job_deets(uniq_keys)['results']):
        print deets

    print "Job finished.. ", count, "results found!"
    print "Filename.." + " " + filename + "\n"
    
    #Prints a sample output from the file we write to
    #with open(filename, 'r') as f:
    #    head = [next(f) for x in xrange(6)]
    #print head
    #f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
        

#--------------------------------------------------------------------------------
#Retrieving Job Details
#--------------------------------------------------------------------------------
#from indeed import IndeedClient

#client = IndeedClient('YOUR_PUBLISHER_NUMBER')

#job_response = client.jobs(jobkeys = ("5898e9d8f5c0593f", "c2c41f024581eae5"))