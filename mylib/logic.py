"""_summary_
This module is built using wikiepdia api 
Returns:
    _str_: returns wikipedia api outputs 
"""

import wikipedia

def wiki(name="War Godesses"):
    """ This is wikipedia fetcher """    
    my_wiki = wikipedia.search(query=name, results=10)
    return my_wiki

if __name__ == '__main__':
    result = wiki()
    print(result)
    