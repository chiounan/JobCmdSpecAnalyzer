'''
Created on 2013/1/30

@author: chiounan
'''
from xml.dom.minidom import parse
from jobCmdSpecModules import *

JobAgtCmdSpecXML_Delete = '../xmlfiles/PM_JobAgent_BackupDelete.xml'
xmlFile = openXmlFile(JobAgtCmdSpecXML_Delete) 
xmlRoot = parse(xmlFile)
closeXmlFile(xmlFile)

jobAttributes = parseJob(xmlRoot)
print ('jobAttributes: %s' % jobAttributes)

commandAttributes = parseCommnad(xmlRoot)
print ('commandAttributes: %s' % commandAttributes)

client = xmlRoot.getElementsByTagName('client')[0]
clientId = client.getAttribute('id')
print ('JobAgt ClientId: %s' % clientId)