'''
Created on 2013/1/30

@author: chiounan
'''
from xml.dom.minidom import parse
from jobCmdSpecModules import *

JobAgtCmdSpecXML_Snapshot = '../xmlfiles/PM_JobAgent_BackupSnapshot.xml'
xmlFile = openXmlFile(JobAgtCmdSpecXML_Snapshot) 
xmlRoot = parse(xmlFile)
closeXmlFile(xmlFile)

jobAttributes = parseJob(xmlRoot)
print ('jobAttributes: %s' % jobAttributes)

commandAttributes = parseCommnad(xmlRoot)
print ('commandAttributes: %s' % commandAttributes)

client = xmlRoot.getElementsByTagName('client')[0]
clientId = client.getAttribute('id')
print ('JobAgt ClientId: %s' % clientId)