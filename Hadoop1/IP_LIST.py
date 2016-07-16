import re,commands,os,socket

def GET_IP():
	pattern_1='[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/[0-9]+'

	pattern_2='[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'

	MAIN_IP=socket.gethostbyname(socket.gethostname())

	IP_AD=re.findall(pattern_1,commands.getoutput(" ip -f inet -o addr " ))

	for i in range(len(IP_AD)):
		if (IP_AD[i].split('/'))[0]== MAIN_IP:
			IP_MASK=IP_AD[i]

	IP_ADS=re.findall(pattern_2,commands.getoutput(" nmap -sP "+IP_MASK+" -n | grep 'report' "))
	IP_LIST=IP_ADS[1:]
	
	return IP_LIST,MAIN_IP

