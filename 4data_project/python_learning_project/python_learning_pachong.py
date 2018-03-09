# 爬虫
# https://www.jianshu.com/p/85f4624485b9

from requests_html import HTMLSession
session=HTMLSession()
url = 'https://www.jianshu.com/p/85f4624485b9'
r=session.get(url)
# print(r.html.text)
# print(r.html.links)
# print(r.html.absolute_links)

sel="body > div.note > div.post > div.article > div.show-content > div > p:nth-child(4) > a"
results=r.html.find(sel)
# print(results)
print(results[0])
print(results[0].text)
# print(results[0].absolute_links)
# print(list(results[0].absolute_links)[0])


def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext, mylink))
        return mylist
    except:
        return None

print(get_text_link_from_sel(sel))

sel1 = 'body > div.note > div.post > div.article > div.show-content > div > p:nth-child(6) > a'
print(get_text_link_from_sel(sel1))


sel2 = 'body > div.note > div.post > div.article > div.show-content > div > p > a'
print(get_text_link_from_sel(sel2))

# import pandas as pd
# df=pd.DataFrame(get_text_link_from_sel(sel2))
# print(df)
# df.columns=['text', 'link']
# print(df)
#
# df.to_csv('output.csv', encoding='gbk', index=False)