from urllib2 import urlopen, URLError
import re
import os, errno, sys

blackurls = ["t.co", "bit.ly","goo.gl","tinyurl.com", "is.gd"]

def changeurl(url):
    global blackurls
    found = 0
    for whiteurl in blackurls:
        if url.find(whiteurl)>=0:
            found = 1
    if found == 0:
        return url
    p = url.find("://")
    if p <0:
        return url
    return url[p+3:]

def shortenurlfromshorl(url):
    global blackurls
    for whiteurl in blackurls:
        if url.find(whiteurl)>=0:
            return url
    url1="http://shorl.com/create.php?url="+url+"&go=Shorlify!"
    sock = urlopen(url1)
    s = sock.read()
    sock.close()
#    s = 'riginal <span class="caps">URL</span>: http://www.nba.com<br>    Shorl: <a href="http://shorl.com/hupryprygafadra" rel="nofollow">http://shorl.com/hupryprygafadra</a></a><br>'
    regexpr = "Shorl: <a href=\".*\" "
    p=re.compile(regexpr)
    m = p.search(s)
    if m:
        surl = m.group()
        surl = surl.rstrip("\" ")
        surl = surl.replace('Shorl: <a href="','')
        return surl
    else:
        return ""


if __name__ == '__main__':
    surl = shortenurlfromshorl("http://www.nba.com")
    print(surl)
