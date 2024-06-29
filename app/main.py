import pathlib
# pathlib.Pathを使って、staticディレクトリの絶対パスを取得
PATH_STATIC = str(pathlib.Path(__file__).resolve().parent / "static")
# pathlib.Pathを使って、pagesディレクトリの絶対パスを取得
PATH_PAGES = str(pathlib.Path(__file__).resolve().parent / "pages")

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Union

app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="/work/app/static"), name="static")

templates = Jinja2Templates(directory="/work/app/pages")
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# from bs4 import BeautifulSoup
# # import math
# # import sys
# html_doc = """
# <html>
#   <head>
#     <title>
#       The Dormouse's story
#     </title>
#  </head>
#  <body>
#     <p class="title">
#       <b>
#         The Dormouse's story
#       </b>
#     </p>
#     <p class="story">
#       Once upon a time there were three little sisters; and their names were
#       <a class="sister" href="http://example.com/elsie" id="link1">
#         Elsie
#       </a>
#       <a class="sister" href="http://example.com/lacie" id="link2">
#         Lacie
#       </a>
#       <a class="sister" href="http://example.com/tillie" id="link3">
#         Tillie
#       </a>
#       and they lived at the bottom of a well.
#     </p>
#     <p class="story">
#       ...
#     </p>
#   </body>
# </html>
# """
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

# def main():
#   print("こんにちは")

# if __name__ == "__main__":
#   main()

