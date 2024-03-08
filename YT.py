import pytube, sys
from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich import print as rprint

from rich import pretty

from rich.text import Text as tekz

pretty.install()

CON=sol()

def banner():

	
	ban=''' ® YOUTUBE DOWNLOADER 

  ####    #####             #####    ####    
 ##  ##   ##  ##            ##  ##   ## ##   
 ##       ##  ##            ##  ##   ##  ##  
  ####    #####    ######   #####    ##  ##  
     ##   ##                ##  ##   ##  ##  
 ##  ##   ##                ##  ##   ## ##   
  ####    ##                #####    ####       
                                             ® MADE BY SP SHAWPON 
'''

	cetak(nel(ban, style='red'))
banner()

try:
	url = input("\033[1;32mYOUR YOUTUBE VIDEO LINK: \033[0m")

	if url == "":
		print("\033[1;31mInvalid URL")
		sys.exit()

	y = pytube.YouTube(url)

	print(y.streams.get_highest_resolution().download("/sdcard"))
	print("\033[1;33m>>> \033[1;32mDownload was successful!\n\033[1;33m>>> \033[1;32m History Save internal storage.")
	print("\033[0m+--------------+")
	print("\033[0m| \033[1;33m>>> \033[1;32mData \033[1;33m<<< \033[0m|")
	print("\033[0m+--------------+")
	print("\033[1;32mFUII NAME : \033[0m",y.title)
	print("\033[1;32mDESCRIPTION : \033[0m",y.description)
	print("\033[1;32mMOST VIEWS : \033[0m",y.views)
	print("\033[1;32mVIDEO LENGTH : \033[0m",y.length)
	print("\033[1;32m PUBLISHED DATE : \033[0m",y.publish_date)
	print("\033[1;32mAGE RESTRICTED : \033[0m",y.age_restricted)
	print("\033[1;32mRATING : \033[0m",y.rating)
	print("\033[1;32mTAG : \033[0m",y.keywords)
	print("\033[1;32mURL THUMBNAIL : \033[0m",y.thumbnail_url)
	print("\033[1;32mCHANEL NAME : \033[0m",y.author)
	print("\033[1;32mCHANEL ID : \033[0m",y.channel_id)
	print("\033[1;32mCHANEL ID : \033[0m",y.channel_url)

except KeyboardInterrupt:
	print("\033[1;33mOk I understand")
	os.system('xdg-open https://facebook.com/groups/black.spammar.bd/')
