#  发送请求



# %%
import requests
from lxml import etree
import matplotlib
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
r = requests.get('https://www.qb5.tw/top/monthvisit/', headers=headers)
# 接收服务器给的响应
e = etree.HTML(r.text)
books_types = e.xpath('//*[@id="articlelist"]/ul[2]/li/span[1]/text()')
books_names = e.xpath('//*[@id="articlelist"]/ul[2]/li/span[2]/a/text()')
books_authors = e.xpath('//*[@id="articlelist"]/ul[2]/li/span[3]/text()')
books_LatestChapter = e.xpath('//*[@id="articlelist"]/ul/li/span[4]/a/text()')
books_counts = e.xpath('//*[@id="articlelist"]/ul[2]/li/span[5]/text()')
books_goodCount = e.xpath('//*[@id="articlelist"]/ul[2]/li/span[6]/text()')
books_updateTime = e.xpath('//*[@id="articlelist"]/ul[2]/li/span[7]/text()')
# %%
#  处理数据

datas = []
for types, names, authors, LatestChapter, counts, goodCount, updateTime in zip(books_types, books_names, books_authors,
                                                                               books_LatestChapter, books_counts,
                                                                               books_goodCount, books_updateTime):
    datas.append([types, names, authors, LatestChapter, counts[:-1], goodCount, updateTime])
# %%
import pandas as pd

df = pd.DataFrame(datas, columns=['类型', '书名', '作者', '最新章节', '总字数', '推荐数', '最后更新时间'])

# %%
df.describe()
# %%
df.groupby('类型').count()
# %%
df.类型.hist()



# %%
sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
# %%
df[df.类型 == '玄幻魔法'].sort_values(by='推荐')
# %%
df['推荐'] = df['推荐'].astype('int')
# %%
