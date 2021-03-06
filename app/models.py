class Source:
    '''
    source Class to define source Objects
    '''
    def __init__(self,id,name,url,description):
        self.id = id
        self.name = name
        self.description= description
        self.url = url

class Article :
    '''
    Article class to define Article Objects
    '''
    def __init__(self,id,name,urlToImage,description,title,url,publishedAt,source):
        self.id=id
        self.name=name
        self.urlToImage=urlToImage
        self.description=description
        self.title=title
        self.url=url
        self.publishedAt=publishedAt
        self.source=source