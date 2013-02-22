'''
Created on 2013/1/30

@author: chiounan
'''
from xml.dom.minidom import parse
from jobCmdSpecModules import openXmlFile
from jobCmdSpecModules import closeXmlFile
from jobCmdSpecModules import parseJob
from jobCmdSpecModules import parseOption

JobAgtCmdSpecXML_Update = '../xmlfiles/PM_JobAgent_BackupUpdate.xml'
xmlFile = openXmlFile(JobAgtCmdSpecXML_Update) 
xmlRoot = parse(xmlFile)
closeXmlFile(xmlFile)

jobAttributes = parseJob(xmlRoot)
print ('jobAttributes: %s' % jobAttributes)

client = xmlRoot.getElementsByTagName('client')[0]
clientId = client.getAttribute('id')
print ('JobAgt ClientId: %s' % clientId)