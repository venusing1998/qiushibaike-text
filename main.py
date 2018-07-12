import json
import os

import requests
from lxml import etree

# 参数
GROUP_START = 1
GROUP_END = 8
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")


def get_html(page):
    """获取网页源代码
    """
    url = "https://www.qiushibaike.com/text/page/{0}/"
    new_url = url.format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    try:
        response = requests.get(new_url, headers=headers)
        if response.status_code == 200:
            html = response.text
            tree = etree.HTML(html)
            result = tree.xpath(
                '//*[@id="content-left"]/div/a[@class="contentHerf"]/@href')
            return result
    except requests.ConnectionError:
        return None


def print_article(href):
    """文章

    """
    article_url = "https://www.qiushibaike.com" + href
    response = requests.get(article_url)
    html = response.content.decode("utf-8")
    tree = etree.HTML(html)
    result = tree.xpath('//*[@id="single-next-link"]/div//text()')
    return result


def main():
    """主函数
    """
    for href in get_html(1):
        # print(print_article(href))
        sep = ""
        sentence = sep.join(print_article(href))
        new_sentence = sentence[2:-2]
        if new_sentence != "" and os.name == "nt":
            os.system("cls")
            print(new_sentence)
            os.system("pause")
        elif new_sentence !="" and os.name == "posix":
            print("平台暂时不支持")

if __name__ == '__main__':
    print('#'*27, 'begin', '#'*27,)
    print('#')
    print('# Author: Chris')
    print('#')
    print('#'*61)
    main()
    print('#'*28, 'end', '#'*28)
