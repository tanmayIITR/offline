def dothis(urlin,count):
	import download_webpage
	download_webpage.core(urlin,count)
file=open('output.txt','r')
i=1
for link in file:
	print ("Downloading "+link.rstrip())
	dothis(link.rstrip(),i)
	i+=1
