"""_summary_
This module is built using wikiepdia api 
Returns:
    _str_: returns wikipedia api outputs 
"""

import wikipedia

def wiki(name="War Godesses",count=0):
    """ This is wikipedia fetcher """    
    my_wiki = wikipedia.search(query=name, results=count)
    return my_wiki

def summary(query, lines=2):
    results = wikipedia.summary(query,sentences=lines)
    return results

if __name__ == '__main__':
    result = wiki()
    summary_response = summary('Newton')
    # print(result)
    