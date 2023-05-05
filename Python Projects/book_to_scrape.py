from bs4 import BeautifulSoup
import requests, openpyxl
import pandas as pd

books_details = []

for i in range(1,51):
    try:
        source = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
        source.raise_for_status()

        soup = BeautifulSoup(source.text,'html.parser')

        # genre_html = soup.find('ul',class_='nav nav-list').find_all('li')

        # # genre_list = []

        # # for genre in genre_html:
        # #     genre_list.append(genre.a.get_text(strip=True))
            
        # # print(genre_list)

        books_row = soup.find('ol', class_='row').find_all('li')
        for book in books_row:
            image = book.find('img')
            title = book.find('img').attrs['alt']
            price = book.find('p', class_='price_color').text.split("£")[1]
            price = float(price)
            rating = book.find('p')['class'][1]
            # title = image.
            # print(title,'-->',price,'-->',rating)

            books_details.append([title,price,rating])
        # print(books_details)
        pass
    except Exception as e:
        print(e)

# for i in books_details:
#     print(i)

df = pd.DataFrame(books_details, columns=['Books Title','Price in Euros','Rating(Out of Five)'] )
df.to_csv('books.csv')