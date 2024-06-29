from bs4 import BeautifulSoup
# import math
# import sys
html_doc = """
<html>
  <head>
    <title>
      The Dormouse's story
    </title>
 </head>
 <body>
    <p class="title">
      <b>
        The Dormouse's story
      </b>
    </p>
    <p class="story">
      Once upon a time there were three little sisters; and their names were
      <a class="sister" href="http://example.com/elsie" id="link1">
        Elsie
      </a>
      <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
      </a>
      <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
      </a>
      and they lived at the bottom of a well.
    </p>
    <p class="story">
      ...
    </p>
  </body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

# def main():
#   print("こんにちは")

# if __name__ == "__main__":
#   main()
