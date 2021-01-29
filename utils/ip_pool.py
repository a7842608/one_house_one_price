import requests
import re


class IpPool(object):
    '''极光ip代理'''

    def __init__(self):
        # self.url = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.tiqu_api_url&packid=1&fa=0&dt=&groupid=0&fetch_key=&qty=1&time=1&port=1&format=json&ss=5&css=&dt=&pro=&city=&usertype=6'
        self.url = 'http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.tiqu_api_url&packid=0&fa=0&dt=0&groupid=0&fetch_key=&qty=1&time=1&port=1&format=json&ss=5&css=&dt=0&pro=%E5%B1%B1%E4%B8%9C%E7%9C%81&city=&usertype=6'

    def ip_pool(self):  # 需传入
        # targetUrl = targetUrl     # 请求地址
        # print(targetUrl, '请求地址被调用')
        # targetUrl = "http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.tiqu_api_url&packid=1&fa=0&dt=&groupid=0&fetch_key=&qty=1&time=1&port=1&format=txt&ss=1&css=&dt=&pro=&city=&usertype=6"
        # s = '{"code":0,"success":"true","msg":"","data":[{"IP":"113.64.92.50","Port":37840}]}'
        resp = requests.get(self.url)
        # statue = resp.status_code
        if resp.status_code != 200:
            statue = {'Code': 400, 'Message': '请求失败, ip并未返回'}
            return statue
        data = resp.text
        try:
            # s_l = re.split('\[|\]|\{|\}', s)
            s_l = re.split('\[|\]|\{|\}', data)
            n_l = [i for i in s_l if i != ""][-1]
            nn_l = n_l.split(',')
            ip_x = nn_l[0].split('"')
            nip_x = [i for i in ip_x if i != '']
            ip = nip_x[-1]  # ip
            po_x = nn_l[-1].split(':')
            port = po_x[-1]  # port
        except Exception as e:
            statue = {'Code': 400, 'Message': '解析失败, 返回可能为空', 'Data': e}
            return statue

        ip_pool = ip + ':' + port
        # ip_pool = {
        # 'IP': ip,
        # 'http': ip,
        # 'Port': port
        # }

        print('ip池被调用', ip_pool)
        # print(ip_pool, 'ippond')
        return ip_pool


if __name__ == '__main__':
    a = IpPool()
    print(a.ip_pool())
    pass
