from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import multiprocessing, time, requests, random
from requests.adapters import HTTPAdapter

from scrapeAndCheck import *

headers_list = [{
		'Host': 'www.cardmarket.com',
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'Sec-Fetch-Dest': 'document',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-Site': 'none',
		'Sec-Fetch-User': '?1',
	},{
		'Host': 'www.cardmarket.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'Sec-Fetch-Dest': 'document',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-Site': 'none',
		'Sec-Fetch-User': '?1',
	},{
		'Host': 'www.cardmarket.com',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'Sec-Fetch-Dest': 'document',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-Site': 'none',
		'Sec-Fetch-User': '?1',
	},{
		'Host': 'www.cardmarket.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Connection': 'keep-alive',
		'Upgrade-Insecure-Requests': '1',
		'Sec-Fetch-Dest': 'document',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-Site': 'none',
		'Sec-Fetch-User': '?1',
	}]

url = 'https://www.cardmarket.com/en'
prox = proxyClass(False)
prox.checkProxies()

def fun1(arg):
	while True:
		try:
			proxy = prox.randomProxy()
			proxyDict = {'http':proxy,'https':proxy}
			#Pick a random header
			headers = random.choice(headers_list)
			#Make the request
			response = requests.get(url,headers=headers, proxies=proxyDict, timeout=5)
			print("[{}] - Status_code : {} - proxy : {}".format(arg,response.status_code,proxy))
		except:
			continue
		break

def multiProcessMap():

	with Pool(5) as p:
		p.map(fun1, range(60))

def multiThreadMap():
	with ThreadPool(20) as p:
		for a in p.map(fun1, range(100)):
			print(a)


def main():
	start = time.time()
	print("-------MP MAP--------")
	multiThreadMap()
	print("---------------------")
	print("Elapsed time : {} seconds".format(time.time()-start))

main()
