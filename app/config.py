class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_URL='https://newsapi.org/v2/sources?apiKey={}'
    HEADLINES_API_URL="https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    SEARCH_SOURCES='https://newsapi.org/v2/everything?q=Apple&from=2021-06-06&sortBy=popularity&apiKey={}'
    

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

    

