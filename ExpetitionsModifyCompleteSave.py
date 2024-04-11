import sys
import re
import os
import glob
import subprocess
import fnmatch
import uuid
import json
from pathlib import Path

# load CompleteSave into json object
strCompleteSavePath = r'C:\Users\Public\Documents\Steam\RUNE\2477340\remote\completesave1.cfg'
print('CompleteSave Filename : {}'.format(strCompleteSavePath))

jsonString = Path(strCompleteSavePath).read_text().rstrip('\x00')
completeSave = json.loads(jsonString)
keysList = list(completeSave.keys())

# change money
completeSave[keysList[0]]['SslValue']['persistentProfileData']['money'] = 999999999
print('\n Change money to 999999999\n')

# add Truck
templateTrucks = '{"phantomMode":0,"isUnviewed":false,"id":"","tmBodies":[],"suspensionDamage":0,"type":"don_71_ultimate","customizationPreset":{"id":-1,"uiName":"","overrideMaterialName":"","tintsColors":[{"a":0.0,"r":0.0,"g":0.0,"b":0.0},{"a":0.0,"r":0.0,"g":0.0,"b":0.0},{"a":0.0,"r":0.0,"g":0.0,"b":0.0}],"gameDataXmlNode":null,"isSpecialSkin":false},"wheelsScale":0.0,"suspension":"don_71_se_suspension_default","uid":"{17D44731-EC60-46e1-8D03-95B99D356F31}","engine":{"name":""},"damage":0,"gearbox":{"name":""},"controlConstrPosition":[],"constraints":[],"winchUpgrade":{"name":""},"wheelsType":"","rims":"rim_1","addons":[],"tires":"allterrain_1","repairs":2147483647,"engineArmor":0,"fuel":2147483648.0,"water":0.0,"wheelRepairs":2147483647,"wheelsDamage":[],"engineDamage":0,"wheelsSuspHeight":[],"truckCRC":0,"isPoweredEngaged":[],"isUnlocked":true,"damageDecals":[],"gearboxDamage":0,"fuelTankDamage":0,"gearboxArmor":0,"suspensionArmor":0,"fuelTankArmor":0,"itemForObjectiveId":"","globalId":"{D39C2668-5FA5-4d59-BDE7-02F57AC713BA}","trailerGlobalId":"","isPacked":false,"isInvalid":false,"needToInstallDefaultAddons":true,"retainedMapId":""}'

truckPatterns = [
		['afim_1960', 'afim_1960_suspension_default'],
		['ank_mk38_ht', 'ank_mk38_ht_suspension_default'],
		['collie_PUG_293', 'collie_PUG_293_suspension_default'],
		['khan_39_marshall', 'khan_39_marshall_suspension_default'],
		['khan_lo4f', 'khan_lo4f_suspension_default'],
		['krs_58_bandit', 's_krs_58_bandit_suspension_default'],
		['tatra_805', 'tatra_805_suspension_default'],
		['tatra_force_t815_7', 'tatra_force_suspension_default'],
		['tuz_108_warthog', 'tuz_108_warthog_suspension_default'],
		['tuz_16_actaeon', 'tuz_16_actaeon_suspension_default'],
		['yar_87', 'yar_87_suspension_default'],
	]

for truckPattern in truckPatterns:
	truck = json.loads(templateTrucks)
	
	truck['type'] = truckPattern[0]
	truck['suspension'] = truckPattern[1]
	truck['uid'] = '{{{}}}'.format(str(uuid.uuid4()))
	truck['globalId'] = '{{{}}}'.format(str(uuid.uuid4()))
	
	completeSave[keysList[0]]['SslValue']['persistentProfileData']['trucksInWarehouse'].append(truck)
	
	print('add truck :', truck['type'], truck['suspension'], truck['uid'], truck['globalId'])
	
# save
with open(strCompleteSavePath, 'w', encoding='utf-8') as f:
    json.dump(completeSave, f, ensure_ascii=False, indent=4)
	
print('\nDone.\n')
	
	
	
