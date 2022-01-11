import urllib.request, urllib.error, socket, requests, multiprocessing, re
from bs4 import BeautifulSoup

class proxyClass():
    def __init__(self):
        # I'm keeping this overly complicated version in case of needing to know if it's http or https
        def freeProxyListNet():
            page = requests.get("https://free-proxy-list.net/")
            soup = BeautifulSoup(page.content, "html.parser")

            name_uncut = soup.find("table", class_="table table-striped table-bordered")
            #print(name_uncut)
            name = re.findall(r'<td(?: class="(?:hm|hx)")?>(.*?)<\/td>',str(name_uncut))
            #print(name)
            current = 0
            temp = ""
            for elem in name:
                val = current%8
                if val == 0:
                    temp = elem
                elif val == 1:
                    temp = temp+":"+elem
                    self.proxyList.append(temp)
                current += 1
            print("found {} proxies at https://free-proxy-list.net/".format(len(self.proxyList)))

        self.proxyList = []
        freeProxyListNet()

        httpLinks = [
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt"
        ]
        for link in httpLinks:
            r = requests.get(link, allow_redirects=True)
            out = r.content.decode("utf8").splitlines()
            self.proxyList = self.proxyList+out
            print("found {} proxies at {}".format(len(out),link))

        #print("\n".join(self.proxyList))

    def getProxies(self):
        return self.proxyList

# This comes from : https://stackoverflow.com/a/765436
def is_bad_proxy(pip):    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': pip,'https': pip})
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        req=urllib.request.Request('https://www.cardmarket.com/en')  # change the URL to test here
        sock=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        #print('Error code: ', e.code)
        return -1
    except Exception as detail:
        #print("ERROR:", detail)
        return -1
    return pip

# Enhanced version of what's from stackoverflow with multiprocessing
def main(nProcess, timeout):
    socket.setdefaulttimeout(int(timeout))

    # two sample proxy IPs
    p = proxyClass()
    proxyList = p.getProxies()
    pool = multiprocessing.Pool(processes=nProcess)
    vals = pool.imap(is_bad_proxy, proxyList)
    iterator = 0
    working = 0
    output = []
    print("Checking which proxies are working ... (might take some time)")
    for result in vals:
        print("[{}/{}] - Working : {}".format((iterator+1),len(proxyList), working), end="\r", flush=True)
        if result != -1:
            output.append(result)
            working+=1
        iterator+=1
    strOut = "\n".join(output)
    print("Working Proxies : \n{}".format(strOut))

# Search for free proxies and check which one are working, on google, with a timeout of 5s, on 8 threads
main(8,5)