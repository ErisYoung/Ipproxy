import re
import requests as rq





def crawl_xicidaili(self):
    for i in range(1, 3):
        start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRjYzc5MmM1MTBiMDMzYTUzNTZjNzA4NjBhNWRjZjliBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUp6S2tXT3g5a0FCT01ndzlmWWZqRVJNek1WanRuUDBCbTJUN21GMTBKd3M9BjsARg%3D%3D--2a69429cb2115c6a0cc9a86e0ebe2800c0d471b3',
            'Host': 'www.xicidaili.com',
            'Referer': 'http://www.xicidaili.com/nn/3',
            'Upgrade-Insecure-Requests': '1',
        }
        html = get_page(start_url, header=headers)
        if html:
            find_trs = re.compile('<tr class.*?>(.*?)</tr>', re.S)
            trs = find_trs.findall(html)
            for tr in trs:
                find_ip = re.compile('<td>(\d+\.\d+\.\d+\.\d+)</td>')
                re_ip_address = find_ip.findall(tr)
                find_port = re.compile('<td>(\d+)</td>')
                re_port = find_port.findall(tr)
                for address, port in zip(re_ip_address, re_port):
                    address_port = address + ':' + port
                    yield address_port.replace(' ', '')







def crawl_data5u(self):
    start_url = 'http://www.data5u.com/free/gngn/index.shtml'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=47AA0C887112A2D83EE040405F837A86',
        'Host': 'www.data5u.com',
        'Referer': 'http://www.data5u.com/free/index.shtml',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    }
    html = get_page(start_url, header=headers)
    if html:
        ip_address = re.compile('<span><li>(\d+\.\d+\.\d+\.\d+)</li>.*?<li class=\"port.*?>(\d+)</li>', re.S)
        re_ip_address = ip_address.findall(html)
        for address, port in re_ip_address:
            result = address + ':' + port
            yield result.replace(' ', '')



base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

def get_page(url,header={}):

    headers=dict(base_headers,**header)
    print("正在抓取",url)
    try:
        res=rq.get(url,headers=headers)
        print(res.headers['User-Agent'])
        print("抓取成功", url,res.status_code)
        if res.status_code==200:
            return res.text
    except ConnectionError:
        print("连接失败",url)
        return None

for i in crawl_data5u(1):
    print(i)



