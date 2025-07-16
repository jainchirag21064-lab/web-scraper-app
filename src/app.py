
from fastapi import FastAPI
import requests


app = FastAPI()


headers = {
    'X-Retain-Images': 'none',
    'X-Return-Format': 'markdown'
}

@app.get("/health")
async def read_root():
    return {"Message": "Congrats! Proxy is up!"}

@app.get("/scrape")
async def read_root(url:str):
    """
    Fetch the page markdown using jina ai.
    """    
    jina_reader_api = "https://r.jina.ai/"
    try:
        response = requests.get(jina_reader_api.join(url), headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch page. Status code: {response.status_code}")            
    except Exception as e:
            print(f"An error occurred during scraping with playwright: {str(e)}")
            return None            
    return response.text
