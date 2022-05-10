import urllib.request, urllib.error, socket, requests, multiprocessing, re, sys, random, time, lxml
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool
from PyQt5 import QtWidgets

WEBPAGE = 'https://www.cardmarket.com/en'
TIMEOUT = 10
FINISH = False

### TODO :
# https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=4350&country=all&ssl=all&anonymity=all&simplified=true
# but needs to download the file
# https://proxylist.geonode.com/api/proxy-list?limit=700&page=1&sort_by=lastChecked&sort_type=desc
# but needs some scraping, it's json, plus it's not https only
# solves the https problem :
# https://proxylist.geonode.com/api/proxy-list?limit=700&page=1&sort_by=lastChecked&sort_type=desc&protocols=http%2Chttps
# https://spys.one/en/https-ssl-proxy/
# needs scraping
class proxyClass():
    def __init__(self, proxyPoolSize, website, timeout, scraping, givenProxyList, gui=True, signals=None, output=""):
        self.nProcess = proxyPoolSize
        self.signals = signals
        self.useGUI = gui
        self.printOutput = output

        global WEBPAGE
        global TIMEOUT
        WEBPAGE = website
        TIMEOUT = int(timeout)
        self.currentText = ""
        self.proxyList = []
        if scraping == True:
            self.initWebScrape()
        if givenProxyList != []:
            self.proxyList.extend(givenProxyList)
        # Delete content of output :
        if output != "":
            with open(output, 'w') as f:
                print("", file=f)

        # random.shuffle(self.proxyList)
        
    def consoleEmit(self, string, backToLine=True):
        if self.useGUI :
            self.signals.console.emit(string)
        else :
            if backToLine :
                print("[{}] - {}".format(time.ctime(), string))
            else :
                print("\r[{}] - {}".format(time.ctime(), string), end='')

    def progressEmit(self, value):
        if self.useGUI :
            self.signals.progress.emit(value)

    def proxiesEmit(self, value, mode):
        if self.useGUI :
            self.signals.proxies.emit(value)
        else :
            if mode == 1 :
                print("[{}] - Scraped Proxies :".format(time.ctime()))
                for elem in value :
                    print(elem)
            if mode == 2 :
                print("\n")
                if self.printOutput != "" :
                    f = open(self.printOutput, 'a')
                    print("[{}] - Working Proxies printed in {}".format(time.ctime(), self.printOutput))
                else :
                    f = sys.stdout
                    print("[{}] - Working Proxies :".format(time.ctime()))
                with open(self.printOutput, 'a') as f :
                    for elem in value :
                        print(elem, file=f)


    def initWebScrape(self):
        # I'm keeping this overly complicated version in case of needing to know if it's http or https
        def freeProxyListNet():
            page = requests.get("https://free-proxy-list.net/")
            soup = BeautifulSoup(page.content, "lxml")

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
            self.currentText = "found {} proxies at https://free-proxy-list.net/".format(len(self.proxyList))
            self.consoleEmit(self.currentText)

        def openProxySpace():
            page = requests.get("https://openproxy.space/list/http")
            soup = BeautifulSoup(page.content, "lxml")

            proxies = re.findall(r',items:\[(.*?)\],active:a},{code:"',str(soup))
            # proxies contains [[dict of proxies 1], [dict of proxies 2], ...]
            tot = 0
            for elem in proxies:
                proxyListNoQuotes = re.sub('(")', r'', elem)
                proxies = proxyListNoQuotes.split(",")
                for prox in proxies:
                    self.proxyList.append(prox)
                    tot = tot + 1
            self.currentText = "found {} proxies at https://openproxy.space/list/http".format(tot)
            self.consoleEmit(self.currentText)

        freeProxyListNet()
        openProxySpace()

        httpLinks = [
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt",
            "https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/http%2Bs.txt",
        ]
        for link in httpLinks:
            r = requests.get(link, allow_redirects=True)
            out = r.content.decode("utf8").splitlines()
            self.proxyList = self.proxyList+out
            self.currentText = "found {} proxies at {}".format(len(out),link)
            self.consoleEmit(self.currentText)
        self.currentText = "found {} proxies in total".format(len(self.proxyList))
        self.proxyList = sorted(set(self.proxyList))
        self.currentText = "Total proxies after removing doubles : {}\n".format(len(self.proxyList))
        self.consoleEmit(self.currentText)
        # Print all the scraped proxies (disactivated because looks messy)
        self.proxiesEmit(self.proxyList, 1)

    def getProxies(self):
        return self.proxyList

    def TheType(self, typeP):
        outlist = []
        for elem in self.proxyList:
            sp = elem.split(":")
            if len(sp) == 4:
                elem = "{}://{}:{}@{}:{}".format(typeP,sp[2],sp[3],sp[0],sp[1])
            else:
                elem = "{}://{}:{}".format(typeP,sp[0],sp[1])
            #print("{}".format(elem))
            outlist.append(elem)
        self.proxyList = outlist

    def randomProxy(self):
        return random.choice(self.proxyList)

    def checkProxy(self, pip):
        if not FINISH:
            try:
                proxy_handler = urllib.request.ProxyHandler({'http': pip,'https': pip})
                opener = urllib.request.build_opener(proxy_handler)
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                urllib.request.install_opener(opener)
                req=urllib.request.Request(WEBPAGE)  # change the URL to test here
                sock=urllib.request.urlopen(req)
                
            except Exception as detail:
                # print("ERROR:", detail)
                return -1
            return pip

    def checkProxies(self):
        startTime = time.time()
        socket.setdefaulttimeout(TIMEOUT)
        self.pool = ThreadPool(self.nProcess)
        #pool = multiprocessing.Pool(processes=self.nProcess)
        iterator = 0
        working = 0
        output = []
        self.consoleEmit("Setting up multithreading for proxies check ...")
        lenProxyList = len(self.proxyList)
        try:
            vals = self.pool.imap(self.checkProxy, self.proxyList)
            for result in vals:
                text = "Checking Proxies : [{}/{}] - Working : {}".format((iterator),lenProxyList, working)
                #self.progressBar.setValue(round(float(iterator+1)/lenProxyList*100))
                self.progressEmit(round(float(iterator+1)/lenProxyList*100))

                self.consoleEmit(text, backToLine=False)
                #print(text, end="\r", flush=True)
                if result != -1:
                    output.append(result)
                    working+=1
                iterator+=1
            self.proxyList = output
        except:
            global FINISH
            FINISH = True
        self.progressEmit(-3)
        self.proxiesEmit(output, 2)
        return output 

    def terminate(self):
        self.consoleEmit("Terminating ProxyClass Threadpool")
        self.pool.terminate()
