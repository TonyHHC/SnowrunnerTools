import sys
import re
import os
import glob
import subprocess
import fnmatch

work_dir = r'E:\Temp\Expetitions\initial\[media]'

def change_mod_attribute_by_file(filename, listPatterns):
	#filename = 'example.json'
	print(f'\nupdate {filename} .......')
	
	# 讀取指定檔案中的內容
	with open(f'{filename}', 'r', encoding="utf-8" ) as f:
		content = f.read()
	
		for eachPattern in listPatterns:
			# 定義要替換的單字和替換後的單字
			pattern = re.compile(eachPattern[0])
			replace_with = eachPattern[1]

			# 替換內容中的單字
			content = re.sub(pattern, replace_with, content)
			
			print(f'  {replace_with} ==> Done')

	# 將處理後的內容寫回檔案中
	with open(f'{filename}', 'w', encoding="utf-8" ) as f:
		f.write(content)
		
def getAllXmlInFolder(folderName):
	filename_list = [folderName+'\\'+f for f in os.listdir(folderName) if f.endswith('.xml')]
	
	return filename_list
	
def getAllXmlInFolderRecursively(folderName):
	filename_list = []
	for root, dirs, files in os.walk(folderName):
		for file in files:
			if file.endswith(".xml"):
				filename_list.append(os.path.join(root, file))
				
	return filename_list
		

if __name__ == '__main__':

	# Unlock
	listPatterns = [
		[r'\tUnlockByRank="\d+(\.\d+)?"', '\tUnlockByRank="1"'],
		[r'\tUnlockByExploration="(.+)"', '\tUnlockByExploration="false"'],
		[r'\tAddonUnlockByObjective="(.+)"', '\tAddonUnlockByObjective="false"'],
		[r'\tFuelConsumption="\d+(\.\d+)?"', '\tFuelConsumption="0.1"'],
		[r'\tDiffLockType=".+(\.+)?"', '\tDiffLockType="Always"'],
		[r'\tCountry=".+(\.+)?"', 'Country=""'],
		[r'\tFuelCapacity="\d+(\.\d+)?"', '\tFuelCapacity="1000"']
	]
	
	filename_list = getAllXmlInFolderRecursively(work_dir)
	for filename in filename_list:
		change_mod_attribute_by_file(filename, listPatterns)
	
	# Wheel grip
	listPatterns = [
		[r'BodyFriction="\d+(\.\d+)?"', 'BodyFriction="3.2"'],
		[r'SubstanceFriction="\d+(\.\d+)?"', 'SubstanceFriction="5.0"'],
		[r'BodyFrictionAsphalt="\d+(\.\d+)?"', 'BodyFrictionAsphalt="4.0"'],
	]
	
	filename_list = getAllXmlInFolder(work_dir + r'\classes\wheels')
	for filename in filename_list:
		change_mod_attribute_by_file(filename, listPatterns)
	

