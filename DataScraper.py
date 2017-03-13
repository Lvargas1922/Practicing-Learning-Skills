# import bs4 as bs
# import urllib.request
# import pandas as pd
#
# # source = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
# #
# # soup = bs.BeautifulSoup(source, 'lxml')
#
# # This prints out all the <p tags(paragraphs) in the unicode>
# # print(soup.find_all('p'))
#
#
# # for paragraph in soup.find_all('p'):
# #    print(paragraph.text)
#
# # print(soup.get_text())
#
# # # To get all the url's
# # for url in soup.find_all('a'):
# #     print(url.get('href'))
#
# # To get the urls in the navigation bar.
# # nav = soup.nav
# #
# # for url in nav.find_all('a'):
# #     print(url.get('href'))
#
# # To get all the data in between the paragraphs as-well.
# # for div in soup.find_all("div", class_='body'):
# #     print(div.text)
#
# # Scrapping tables with URllib and BS4.
# # table = soup.find('table')
# #
# # table_rows = table.find_all('tr')
# #
# # for tr in table_rows:
# #     td = tr.find_all('td')
# #     row = [i.text for i in td]
# #     print(row)
#
# # Using Pandas for DataFrame Manipulation (for tables).
# # dfs = pd.read_html("https://pythonprogramming.net/parsememcparseface/", header=0)
# #
# # for df in dfs:
# #     print(df)
#
# # XML files/Site maps.
# # Find the sitemap first and use as source link.
# source = urllib.request.urlopen("https://pythonprogramming.net/sitemap.xml").read()
#
# soup = bs.BeautifulSoup(source, 'lxml')
# # for url in soup.find_all('loc'):
# #     print(url.text)
#
