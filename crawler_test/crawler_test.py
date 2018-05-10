# 导入模块
import re
import requests
url = "http://www.cae.cn/cae/html/main/col48/column_48_1.html"
# 请求数据  获取网页源代码
html = requests.get(url)
html.encoding = 'utf-8'   # 指定网页格式，用于正确显示网页编码

# print(html.status_code)  # 网页状态代码   200正常   404错误   500(服务器内部错误)
# print(html)
# print(html.text)  # 返回文本信息

# print(html.url)     # 返回请求的网址
# print(html.cookies)  # 返回cookies值
# print(html.headers)  # 返回头部信息
# print(html.content)     # 返回的是字节流的形式（图片）

# 提取文本信息
num = re.findall('/cae/html/main/colys/(\d+).html" target="_blank">', html.text)
# num = re.findall('/cae/html/main/colys/(.*?).html" target="_blank">', html.text)
# print(num)

# 拼接网址
# for n in num:       # 取全部数据
for n in num[:3]:    # 取前3个数据
    # nextUrl = 'http://www.cae.cn/cae/html/main/colys/'+n+'.html'   # 字符串拼接
    nextUrl = 'http://www.cae.cn/cae/html/main/colys/{}.html'.format(n)
    # 再次请求网址
    nextHtml = requests.get(nextUrl)
    nextHtml.encoding = "utf-8"
    print(nextHtml)
    # 提取数据
    data = re.findall('<div class="intro">(.*?)</div>', nextHtml.text, re.S)
    # print(data)
    deal_data = re.sub(r'&ensp;|<p>|&nbsp;|</p>', '', data[0]).strip()
    print(deal_data)
    with open('cae.txt', 'a+') as f:
        # mode = 'a+' 可读可写，若文件不存在，创建文件，不会覆盖，追加写
        f.write(deal_data + '\n' * 2)

"""
文件读写模式
mode = 'r'  只能读，  若文件不存在，报错
mode = 'r+' 可读可写，若文件不存在，报错，     文件内容：会覆盖
mode = 'w'  可读可写，若文件不存在，创建文件，          会覆盖
mode = 'w+' 可读可写，若文件不存在，创建文件，          会覆盖
mode = 'a'  可读可写，若文件不存在，创建文件，          不会覆盖，追加写
mode = 'a+' 可读可写，若文件不存在，创建文件，          不会覆盖，追加写
"""
