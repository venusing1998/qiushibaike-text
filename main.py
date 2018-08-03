import json

import requests
from lxml import etree


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
            result = response.text
            return result
    except requests.ConnectionError:
        return None


def get_data(html):
    """得到每篇文章的链接

    """
    tree = etree.HTML(html)
    result = tree.xpath(
        '//*[@id="content-left"]/div/a[@class="contentHerf"]/@href')
    return result


def print_article(href):
    """打印文章

    """
    article_url = "https://www.qiushibaike.com" + href
    response = requests.get(article_url)
    html = response.text
    tree = etree.HTML(html)
    result = tree.xpath('//*[@id="single-next-link"]/div//text()')
    return result


def main():
    """主函数
    """
    html = get_html(1)
    count = 1
    for href in get_data(html):
        # print(print_article(href))
        sentence = "".join(print_article(href))
        new_sentence = sentence[2:-2]
        print("Article", count, " :\n", new_sentence, "\n\n", sep="")
        count += 1


if __name__ == '__main__':
    main()
