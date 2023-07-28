import wikipedia

def wiki(name="War Godesses", length=1):
    """ This is wikipedia fetcher """
    
    my_wiki = wikipedia.search(query=name, results=10)
    return my_wiki

if __name__ == '__main__':
    result = wiki()
    print(result)
    
