from app import app
import urllib.request,json
from .models import source,article
Source = source.Source
Article = article.Article

#Getting api key
api_Key = app.config["NEWS_API_KEY"]

#Getting the news base url
highlights_url = app.config["SOURCE_API_URL"]
sources_url = app.config["HEADLINES_API_URL"]
search_url = app.config["SEARCH_SOURCES"]

def process_sources(sources_list):
    sources_results = []
    for source in sources_list:
        id = source.get("id")
        name = source.get("name")
        description = source.get("description")
        language = source.get("language")

        source_object = Source(id,name,description,language)
        sources_results.append(source_object)

    return sources_results

def get_sources():
    """Function that gets the json response to our url request"""
    get_sources_url = highlights_url.format(api_Key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response["sources"]:
            sources_results_list = get_sources_response["sources"]
            sources_results = process_sources(sources_results_list)
    return sources_results

def process_articles(articles_list):
    article_results = []
    for article in articles_list:
        name = article.get("source")["name"]
        author =article.get("author")
        source = article.get("source")
        #name= source["name"]
        title = article.get("title")
        description = article.get("description")
        url = article.get("url")
        urlToImage = article.get("urlToImage")
        publishedAt = article.get("publishedAt")
        content = article.get("content")

        article_object = Article(author,title,description,url,urlToImage,publishedAt,content)

        article_results.append(article_object)
    return article_results


def get_article(id):
    """Function that returns articles from a source"""
    get_article_url = sources_url.format(id,api_Key)

    with urllib.request.urlopen(get_article_url) as url:
        article_details_data =url.read()
        article_details_response = json.loads(article_details_data)

        article_results = None
        if article_details_response["articles"]:
            article_results_list = article_details_response["articles"]
            article_results = process_articles(article_results_list)

    return  article_results 
        