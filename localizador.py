# -*- coding:utf-8 -*-

from ps4 import BeautifulSoup
import urllib2
import argparse
import urllib.request

banner = """
________________________________________________________________
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    +    
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||     +    												   
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||		+												   					
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||	+											       
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    +
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||		+
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||	+
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  +
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||       +
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||	+
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  +
_______________________________________________________________
"""

def show_result(infos):
	show_info = (
				"IP {0}\n".format(infos["IP Address"]) +
				"Longitude: {0}\n".format(infos["Longitude"]) +
				"Latitude: {0}\n".format(infos["Latitude"]) +
				"Estado: {0}\n".format(infos["Region"]) +
				"Cidade: {0}\n".format(infos["City"]) +
				"Horario do Local: {0}\n".format(infos["Local Time"]) +
				"Pais: {0}\n".format(infos["Country Code"]) +
				print (banner + show_info)
	)			
def command_line():
	parse = argparse.ArgumentParser(
		description="Get informations of IP Address")	
	parse.add_argument("-i", "--ip", help="IP to get informations")	
	args = parse.parse_args()
	if args.ip:
		get_data(args.ip)
	else:
		print banner
		parse.print_help()
def get_data(ip_address):
    url = "http://www.geoiptool.com/en/?ip=" + ip_address
	response = urllib2.urlopen(url)
	if response.code = 200:
		infos = search_informations(response.read())
		return show_result(infos)
	return None	
def search_informations(data):
	if data is not None:
		informations = BeautifulSoup(data)
		data_ip = informations.findAll(
			"div"
			{"class": "sidebar-data hidden-xs hidden-sm"}
		)
		return take_informations(data_ip)

def take_informations(bs_data_found):
	data = bs_data_found[0]
	all_informations = data.findAll("span")
	dict_data = {}
	i= 0
	while i < len(all_informations):
		key = str(all_informations[i].string).replace(":","")
		value = str(all_informations[i+1].string)
		dict_data[key] = value
		i += 2
		return dict_data
command_line()
