# See reference.txt for explanation of url encoding for Yahoo Finance API
import urllib
import time
import datetime

dt1 = datetime.datetime.now()

def is_nasdaq_open(dt1):
	if (dt1.month == 1 and (dt1.day == 1 or dt1.day == 18)):	# NASDAQ is closed on New Year's and MLK B-day
		return False
	elif (dt1.month == 2 and dt1.day == 15):		# NASDAQ is closed for President's Day
		return False
	elif (dt1.month == 3 and dt1.day == 25):		# NASDAQ is closed for Good Friday
		return False
	elif (dt1.month == 5 and dt1.day == 30):		# NASDAQ is closed for Memorial Day
		return False
	elif (dt1.month == 7 and dt1.day == 4):		# NASDAQ is closed for Independence Day
		return False
	elif (dt1.month == 9 and dt1.day == 5):		# NASDAQ is closed for Labor Day
		return False
	elif (dt1.month == 11 and (dt1.day == 24 or dt.day == 25)):		# NASDAQ is closed for Thanksgiving
		return False
	elif (dt1.month == 12 and dt1.day == 25):		# NASDAQ is closed only on Xmas Day, but not Xmas Eve, lulz
		return False
	else:
		return True

symbol_file = open("/home2/greyhau1/scraper/py/stock.csv")
symbol_list = symbol_file.read()
new_symbol_list = symbol_list.split(",")
symbol_file.close()

if (is_nasdaq_open(dt1) == True):
	dt1 = datetime.datetime.now()
	print "Date: " + str(dt1.year) + "-" + str(dt1.month) + "-" + str(dt1.day)
	print "Time: " + str(dt1.hour) + ":" + str(dt1.minute) + ":" + str(dt1.second)
	print "Running scraper routine..."
	for i in range(0, len(new_symbol_list)):
		url = "http://download.finance.yahoo.com/d/quotes.csv?s=" +new_symbol_list[i] + "&f=e1aa2a5bb4b6cc1dd1ee7e8e9f6ghjj1j2j4j5j6kk3k4k5l1mm3m4m5m6m7m8opp2p5p6qrr1r5r6r7ss6s7t1t8vwxyn=.csv"
		htmlfile = urllib.urlopen(url)
		htmltext = htmlfile.read()
		price_file = open("/home2/greyhau1/scraper/st_log/" +new_symbol_list[i] +".csv", 'a+')
		price_file.write(str(dt1.year) + "-" + str(dt1.month) + "-" + str(dt1.day) + "," + htmltext)
		price_file.close()
		i +=1
		time.sleep(3)
		
	
	dt2 = datetime.datetime.now()
	print "[done]"
	print "Time: " + str(dt2.hour) + ":" + str(dt2.minute) + ":" + str(dt2.second)
	hour_diff = dt2.hour - dt1.hour
	min_diff = dt2.minute - dt1.minute
	sec_diff = dt2.second - dt2.second
	print "Scraper total runtime: " + str(hour_diff) + ":" + str(min_diff) + ":" + str(sec_diff)
	min_diff = (hour_diff * 60) + min_diff
	sec_diff = (min_diff * 60) + sec_diff
	print "runtime in seconds: " + str(sec_diff)
	length = len(new_symbol_list)
	print "Total stocks recorded: " + str(length)
	average = sec_diff / len(symbol_list)
	print "Average number of seconds per request: " + str(average)
	average = 3600 / sec_diff
	print "Average number of requests per hour: " + str(average)
	