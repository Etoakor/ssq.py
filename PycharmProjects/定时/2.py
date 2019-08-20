#!/usr/local/bin/python2.7
  # coding:utf-8
import datetime
import codecs
import requests
import os
import time
from pyquery import PyQuery as pq
    #git操作 推送到远程repo
def git_add_commit_push(date, filename):
    cmd_git_add = 'git add .'
    cmd_git_commit = 'git commit -m "{date}"'.format(date=date)
    cmd_git_push = 'git push -u origin master'
    os.system(cmd_git_add)
    os.system(cmd_git_commit)
    os.system(cmd_git_push)
def createMarkdown(date, filename):
    with open(filename, 'w') as f:
        f.write("###" + date + "\n")
def scrape(language, filename):
    HEADERS = {
        'User-Agent'        : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'    : 'gzip,deflate,sdch',
        'Accept-Language'    : 'zh-CN,zh;q=0.8'
    }
    url = 'https://github.com/trending/{language}'.format(language=language)
    r = requests.get(url, headers=HEADERS)
    assert r.status_code == 200
    # print(r.encoding)
    d = pq(r.content)
    items = d('ol.repo-list li')
    # codecs to solve the problem utf-8 codec like chinese
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n##{language}\n'.format(language=language))
        for item in items:
            i = pq(item)
            title = i("h3 a").text()
            owner = i("span.prefix").text()
            description = i("p.col-9").text()
            url = i("h3 a").attr("href")
            url = "https://github.com" + url
            # ownerImg = i("p.repo-list-meta a img").attr("src")
            # print(ownerImg)
            f.write(u"* [{title}]({url}):{description}\n".format(title=title, url=url, description=description))
    #定时爬取对应语言的并写入到markdown文本中
def job():
    strdate = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = '{date}.md'.format(date=strdate)
    # create markdown file
    createMarkdown(strdate, filename)
    # write markdown
    scrape('python', filename)
    scrape('swift', filename)
    scrape('javascript', filename)
    scrape('go', filename)
    scrape('Objective-C', filename)
    scrape('Java', filename)
    scrape('C++', filename)
    scrape('C#', filename)
    # git add commit push
    git_add_commit_push(strdate, filename)
    #主函数
if __name__ == '__main__':
    job()
'''   
    while True:
        job()
        time.sleep(12 * 60 * 60)
'''