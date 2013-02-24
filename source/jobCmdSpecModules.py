'''
Created on 2013/1/30

@author: chiounan
'''
from xml.dom.minidom import parse
import sys

# input XML file root - xmlRoot
# output job attributes as a dictionary array - jobAttribute
def parseJob (xmlRoot):
    jobAttributes = {}
    job = xmlRoot.getElementsByTagName('job')[0]
    jobProtectionGroupId = job.getAttribute('protectionGroupId')
    jobId = job.getAttribute('id')
    jobName = job.getAttribute('name')
    jobType = job.getAttribute('type')
    jobSessionNo = job.getAttribute('sessionNo')
    jobWorkerServerName = job.getAttribute('workerServerName')
    jobManageServerName = job.getAttribute('manageServerName')
    
    jobAttributes['protectionGroupId'] = jobProtectionGroupId
    jobAttributes['id'] = jobId
    jobAttributes['name'] = jobName
    jobAttributes['type'] = jobType
    jobAttributes['sessionNo'] = jobSessionNo
    jobAttributes['workerServerName'] = jobWorkerServerName
    jobAttributes['manageServerName'] = jobManageServerName
    return jobAttributes

def parseCommnad(xmlRoot):
    commnadAttributes = {}
    command = xmlRoot.getElementsByTagName('command')[0]
    commandName = command.getAttribute('name')
    commandMethod = command.getAttribute('method')
    commandMode = command.getAttribute('mode')
    if(command.getAttribute('token')):
        commnadAttributes['token'] = command.getAttribute('token')
    commnadAttributes['commandName'] = commandName
    commnadAttributes['commandMethod'] = commandMethod
    commnadAttributes['commandMode'] = commandMode
    return commnadAttributes

def parseClient(xmlRoot):
    clientAttributes = {}
    client = xmlRoot.getElementsByTagName('client')[0]
    clientId = client.getAttribute('id')
    clientHostName = client.getAttribute('hostName')
    clientAttributes['id'] = clientId
    clientAttributes['hostName'] = clientHostName
    return clientAttributes

# input full path of XML file - filename
# output file handler - xmlFile
# exception handler - IOError
def openXmlFile (filename):
    try:
        xmlFile = open (filename)
    except IOError:
        print (filename + ' not found.')
    else:
#        print (filename + ' found.')
        return xmlFile 

def closeXmlFile (fileHeader):
    fileHeader.close()
    return

# input XML file root - xmlRoot
# output option attributes as a dictionay array - optionAttibutes
def parseOption (xmlRoot):
    optionAttributes = {}
    option = xmlRoot.getElementsByTagName('option')[0]
    optionSync = option.getElementsByTagName('sync')[0]
    sync_watermarkTriggerInMB = optionSync.getAttribute('watermarkTriggerInMB')
    sync_microScanByte = optionSync.getAttribute('microScanByte')
    sync_isEncryption = optionSync.getAttribute('isEncrytion')
    optionEncrypt = optionSync.getElementsByTagName('encrypt')[0]
    encrypt_keyName = optionEncrypt.getAttribute('keyName')
    encrypt_keyCipher = optionEncrypt.getAttribute('keyCipher')
    optionRetention = option.getElementsByTagName('retention')[0]
    rentetion_type = optionRetention.getAttribute('type')
    retentionBasic = optionRetention.getElementsByTagName('basic')[0]
    retention_basic_count = retentionBasic.getAttribute('count')
    retention_basic_unit = retentionBasic.getAttribute('unit')
    retentinoHourly = optionRetention.getElementsByTagName('hourly')[0]
    retention_hourly_count = retentinoHourly.getAttribute('count')
    retention_hourly_minuteOffset = retentinoHourly.getAttribute('minuteOffset')
    retentinoDaily = optionRetention.getElementsByTagName('daily')[0]
    retention_daily_count = retentinoDaily.getAttribute('count')
    retention_daily_hourOffset = retentinoDaily.getAttribute('hourOffset')
    retentinoWeekly = optionRetention.getElementsByTagName('weekly')[0]
    retention_weekly_count = retentinoWeekly.getAttribute('count')
    retention_weekly_dayOfWeek = retentinoWeekly.getAttribute('dayOfWeek')
    retentinoMonthly = optionRetention.getElementsByTagName('monthly')[0]
    retention_monthly_count = retentinoMonthly.getAttribute('count')
    retention_monthly_dayOfMonth = retentinoMonthly.getAttribute('dayOfMonth')
    
    optionAttributes['watermarkTriggerInMB'] = sync_watermarkTriggerInMB
    optionAttributes['microScanByte'] = sync_microScanByte
    optionAttributes['isEncrytion'] = sync_isEncryption
    optionAttributes['keyName'] = encrypt_keyName
    optionAttributes['keyCipher'] = encrypt_keyCipher
    optionAttributes['type'] = rentetion_type
    optionAttributes['basic_count'] = retention_basic_count
    optionAttributes['basic_unit'] = retention_basic_unit
    optionAttributes['hourly_count'] = retention_hourly_count
    optionAttributes['hourly_minuteOffset'] = retention_hourly_minuteOffset
    optionAttributes['daily_count'] = retention_daily_count
    optionAttributes['daily_hourOffset'] = retention_daily_hourOffset
    optionAttributes['weekly_count'] = retention_weekly_count
    optionAttributes['weekly_dayOfWeek'] = retention_weekly_dayOfWeek
    optionAttributes['monthly_count'] = retention_monthly_count
    optionAttributes['monthly_dayOfMonth'] = retention_monthly_dayOfMonth
    return optionAttributes

# Handle more than one pool
def handlePools(pool):
    poolId = pool.getAttribute('id')
#    print (poolId)
    return poolId

# Handle more than one server
def handleServers(server):
    singleServerAttriputes = {}
    serverId = server.getAttribute('id')
    serverName = server.getAttribute('name').split('/')[0]
    serverIP = server.getAttribute('name').split('/')[1]
    user = server.getElementsByTagName('user')[0]
    userName = user.getAttribute('name')
    userPasswork = user.getAttribute('password')
    serverPools = server.getElementsByTagName('pools')[0]
    pools = serverPools.getElementsByTagName('pool')
    poolList = []
    for pool in pools:
        poolId = handlePools(pool)
        poolList.append(poolId)
#    print (poolList)
    
    singleServerAttriputes['id'] = serverId
    singleServerAttriputes['server_name'] = serverName
    singleServerAttriputes['server_IP'] = serverIP
    singleServerAttriputes['user_name'] = userName
    singleServerAttriputes['password'] = userPasswork
    singleServerAttriputes['pools'] =  poolList
#    print ('singleServerAttriputes: %s' % singleServerAttriputes)
    return singleServerAttriputes
        
# input XML file root - xmlRoot
# output server attributes as a list array - serversAttibutes 
def parseServers(xmlRoot):
    serversAttributes = []
    servers = xmlRoot.getElementsByTagName('server')
#    print ('Number of servers: %s' % servers.length)
    for server in servers:
        singleServerAttributes = handleServers(server)
        serversAttributes.append(singleServerAttributes)
    return serversAttributes

# Handle exclusion for sourcedisk
def handleSourcediskExclusion(exclusion):
    exclusionPartId = exclusion.getAttribute('partId')
#    print ('exclusion partId: %s' % exclusionPartId)
    return exclusionPartId
    
# Handle sourcedisks
def handleSourcedisk(sourcedisk):
    singleSourcediskAttributes = {}
    sourcediskId = sourcedisk.getAttribute('id')
#    print ('sourcedisk id: %s' % sourcediskId)
    singleSourcediskAttributes['id'] = sourcediskId
    exclusions = sourcedisk.getElementsByTagName('exclusion')
#    print ('Number of exclusions of sourcedisk (id: %s): %s' % (sourcediskId, exclusions.length))
    sourcediskExclusionAttributes = []
    if exclusions.length == 0:
        sourcediskExclusionAttributes = ''
    else:
        for exclusion in exclusions:
            sourcediskExclusionAttributes.append(handleSourcediskExclusion(exclusion))
#            print (sourcediskExclusionAttributes)
            singleSourcediskAttributes['exclusionPartId'] = sourcediskExclusionAttributes
    return singleSourcediskAttributes        

# Handle multiple exclusions in volumes
# Return a array of exclusion id
def handleVolumes(exclusion):
    serialNum = exclusion.getAttribute('serialNum')
    return serialNum

# Handle multiple clients
# Return a dictionary array of single client attributes
def handleClients(client):
    singleClientAttributes = {}
    clientId = client.getAttribute('id')
    clientName = client.getAttribute('name').split('/')[0]
    clientIP = client.getAttribute('name').split('/')[1]
    clientDisks = client.getElementsByTagName('disks')[0]
    isAllDisk = clientDisks.getAttribute('isAllDisk')
    isGroupAll = clientDisks.getAttribute('isGroupAll')
    sourceDisks = clientDisks.getElementsByTagName('sourcedisk')
#    print ('Number of sourcedisks: %s' % sourceDisks.length)
    disksSourcediskAttributes = []
    if sourceDisks.length == 0:
        disksSourcediskAttributes = ''
    else:
        for sourcedisk in sourceDisks:
            disksSourcediskAttributes.append(handleSourcedisk(sourcedisk))
#            print (disksSourcediskAttributes)
    try:
        diskVolumes = client.getElementsByTagName('volumes')[0]
    except IndexError:
        clientVolumesExclusion = ''
    else:
        clientVolumesExclusion = diskVolumes.getElementsByTagName('exclusion')
        
    volumesExclusionAttributes = []
    if clientVolumesExclusion == '':
        volumesExclusionAttributes = ''
    else:
        for exclusion in clientVolumesExclusion:
            volumesExclusionAttributes.append(handleVolumes(exclusion))
#        print (volumesExclusionAttributes)
    
    singleClientAttributes['id'] = clientId
    singleClientAttributes['client_name'] = clientName
    singleClientAttributes['client_IP'] = clientIP
    singleClientAttributes['isAllDisk'] = isAllDisk
    singleClientAttributes['isGroupAll'] = isGroupAll
    singleClientAttributes['sourcedisk'] = disksSourcediskAttributes
    singleClientAttributes['volumes'] = volumesExclusionAttributes
    return singleClientAttributes

# input XML file root - xmlRoot
# output client attributes as a list array - clientsAttributes
def parseClients(xmlRoot):
    clientsAttributes = []
    clients = xmlRoot.getElementsByTagName('client')
#    print ('Number of clients: %s' % clients.length)
    if clients.length == 0:
        clientsAttributes = ''
        print ('There is no client info.')
        sys.exit()
    else:
        for client in clients:
            singleClientAttributes = handleClients(client)
#            print ('singleClientAttributes: %s' % singleClientAttributes)
            clientsAttributes.append(singleClientAttributes)
    return clientsAttributes

# parse Data_ClientDisk disks attributes 
def parseDisksAttributes(xmlRoot):
    disksAttributes = []
    disks = xmlRoot.getElementsByTagName('disk')
    for disk in disks:
        singleDiskAttributes = {}
        singleDiskAttributes['id'] = disk.getAttribute('id')
        singleDiskAttributes['role'] = disk.getAttribute('role')
        disksAttributes.append(singleDiskAttributes)
#    print ('disksAttributes[]: %s' % disksAttributes)
    return disksAttributes

# parse Data_ClientDisk disks attributes
def parseDataClientDiskAttributes(xmlRoot):
    disksAttributes = []
    disks = xmlRoot.getElementsByTagName('disks')[0]
    disk = disks.getElementsByTagName('disk')
    for disk_n in disk:
        device = disk_n.getElementsByTagName('device')[0]
        attribute = disk_n.getElementsByTagName('attribute')[0]
        disksafe = disk_n.getElementsByTagName('disksafe')[0]
#        backupinfo = disk_n.getElementsByTagName('backupinfo')[0]
        singleDiskAttributes = {}
        singleDiskAttributes['disk_id'] = disk_n.getAttribute('id')
        singleDiskAttributes['disk_role'] = disk_n.getAttribute('role')
        singleDiskAttributes['device_name'] = device.getAttribute('name')
        singleDiskAttributes['signature'] = attribute.getAttribute('signature')
        singleDiskAttributes['disksafe_uniqueName'] = disksafe.getAttribute('uniqueName')
        try:
            backupinfo = disk_n.getElementsByTagName('backupinfo')[0]
        except IndexError:
            singleDiskAttributes['originalId'] = ''
            singleDiskAttributes['serverId'] = ''
            singleDiskAttributes['serverName'] = ''
            singleDiskAttributes['vid'] = ''
        else:
            singleDiskAttributes['originalId'] = backupinfo.getAttribute('originalId')
            singleDiskAttributes['serverId'] = backupinfo.getAttribute('serverId')
            singleDiskAttributes['serverName'] = backupinfo.getAttribute('serverName')
            singleDiskAttributes['vid'] = backupinfo.getAttribute('vid')
#        print ('singleDiskAttributes[]: %s' % singleDiskAttributes)
        disksAttributes.append(singleDiskAttributes)
    return disksAttributes

# parse volume serial number
def parseVolumesAttributes(xmlRoot):
    volumesAttributes = []
    volumes = xmlRoot.getElementsByTagName('volume')
    for volume in volumes:
        singleVolumeAttributes = {}
        singleVolumeAttributes['serialNum'] = volume.getAttribute('serialNum')
        singleVolumeAttributes['occupiedBytes'] = volume.getAttribute('occupiedBytes')
        volumesAttributes.append(singleVolumeAttributes)
#    print ('volumesAttributes[]: %s' % volumesAttributes)
    return volumesAttributes    

# gets attributes by tag name
# return a list
# the length of list is len(list)
def parseXAttributes(xmlRoot, tagName, tagElement):
    attributesList = []
    title = xmlRoot.getElementsByTagName(tagName)
    for element in title:
        elementValue = element.getAttribute(tagElement)
        attributesList.append(elementValue)
    return attributesList
                 