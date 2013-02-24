'''
Created on 2013/1/30

@author: chiounan
'''
from xml.dom.minidom import parse
from jobCmdSpecModules import *

JobAgtCmdSpecXML_Create = '../xmlfiles/PM_JobAgent_BackupCreate.xml'
xmlFile = openXmlFile(JobAgtCmdSpecXML_Create) 
xmlRoot = parse(xmlFile)
closeXmlFile(xmlFile)

jobAttributes = parseJob(xmlRoot)
#print ('jobAttributes: %s' % jobAttributes)

commandAttributes = parseCommnad(xmlRoot)
#print ('commandAttributes: %s' % commandAttributes)

optionAttributes = parseOption(xmlRoot)
#print ('optionAttributes: %s' % optionAttributes)

clientAttributes = parseClient(xmlRoot)
#print ('clientAttributes: %s' % clientAttributes)

client = xmlRoot.getElementsByTagName('client')[0]
clientId = client.getAttribute('id')
clientHostName = client.getAttribute('hostName')
#print ('JobAgt ClientId: %s' % clientId)
#print ('JobAgt ClientHostName: %s' % clientHostName)

client_id = parseXAttributes(xmlRoot, 'client', 'id')
diskId = parseXAttributes(xmlRoot, 'disk', 'id')
disk_id = parseXAttributes(xmlRoot, 'disk', 'id')
#for i in range(len(diskId)):
#    print ('diskId[%d]:%s' % (i, diskId[i]))

sourcedisk_uniqueName = parseXAttributes(xmlRoot, 'sourcedisk', 'uniqueName')
sourcedisk_signature = parseXAttributes(xmlRoot, 'sourcedisk', 'signature')
sourcedisk_guid = parseXAttributes(xmlRoot, 'sourcedisk', 'guid')
#print (sourcedisk_uniqueName)
#print (sourcedisk_signature)
#print (sourcedisk_guid)

targetdisk_serverName = parseXAttributes(xmlRoot, 'targetdisk', 'serverName')
targetdisk_vid = parseXAttributes(xmlRoot, 'targetdisk', 'vid')
targetdisk_isNewAllocation = parseXAttributes(xmlRoot, 'targetdisk', 'isNewAllocation')
targetdisk_isExpanded = parseXAttributes(xmlRoot, 'targetdisk', 'isExpanded')

diskAttributes = []
for i in range(len(targetdisk_serverName)):
    targetdiskAttributes = {}
    targetdiskAttributes['serverName'] = targetdisk_serverName[i]
    targetdiskAttributes['vid'] = targetdisk_vid[i]
    targetdiskAttributes['isNewAllocation'] = targetdisk_isNewAllocation[i]
    targetdiskAttributes['isExpanded'] = targetdisk_isExpanded[i]
    diskAttributes.append(targetdiskAttributes)
#    print (targetdiskAttributes)
#print (diskAttributes)