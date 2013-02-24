'''
Created on 2013/1/30

@author: chiounan
'''
from xml.dom.minidom import parse
from jobCmdSpecModules import *


JobAgtCmdSpecXML_Update = '../xmlfiles/PM_JobAgent_BackupUpdate.xml'
xmlFile = openXmlFile(JobAgtCmdSpecXML_Update) 
xmlRoot = parse(xmlFile)
closeXmlFile(xmlFile)

jobAttributes = parseJob(xmlRoot)
#print ('jobAttributes: %s' % jobAttributes)

clientAttributes = parseClient(xmlRoot)
#print ('clientAttributes: %s' % clientAttributes)

client = xmlRoot.getElementsByTagName('client')[0]
clientId = client.getAttribute('id')
#print ('JobAgt ClientId: %s' % clientId)

disk_id = parseXAttributes(xmlRoot, 'disk', 'id')
