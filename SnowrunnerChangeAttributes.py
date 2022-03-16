# python SnowrunnerChangeAttributes.py | tee output.log

import os
import glob
import pandas as pd
import re

def specialCharReplace(strSource, strSearch):
	strRet = ''
	listSource = list(strSource)
	for eachCh in listSource:
		if eachCh in strSearch:
			strRet += '['+eachCh+']'
		else:
			strRet += eachCh
			
	return strRet

def doInsert(iIndex, row):
	print('[{}] {} :'.format(iIndex, row['Filename']))
	
	strFilename = specialCharReplace(row['Filename'], '[]')
	strPrefix = row['PrefixString'].replace('\\t', '\t').replace('\\n', '\n')
	strTarget = row['TargetString'].replace('\\t', '\t').replace('\\n', '\n')
	
	files = glob.glob(strFilename, recursive=True)
	
	for file in files:
		print('    >> ', end='')
		if os.path.exists(file):
			with open(file, 'r+', encoding='utf-8') as f:
				content = f.read()
				if content.find(strTarget) == -1:
					index = content.find(strPrefix)
		
					if index != -1:
						bInsert = True
			
						new_index = index+len(strPrefix)
						new_content = content[:new_index] + strTarget + content[new_index+1:]
			
						f.seek(0)
						f.truncate()
			
						f.write(new_content)
						print('插入成功   ', end='')
					else:
						print('插入失敗   ', end='')
				else:
					print('無須插入   ', end='')
		else:
			print('檔案不存在 ', end='')
			
		print(file)

	
	
def doReplace(iIndex, row):

	print('[{}] {} :'.format(iIndex, row['Filename']))
	
	strFilename = specialCharReplace(row['Filename'], '[]')
	strTarget = row['TargetString'].replace('\\t', '\t').replace('\\n', '\n')
	strReplace = row['ReplaceToString'].replace('\\t', '\t').replace('\\n', '\n')
	
	files = glob.glob(strFilename, recursive=True)
	
	for file in files:
		print('    >> ', end='')
		if os.path.exists(file):
			with open(file, 'r+', encoding='utf-8') as f:
				content = f.read()
				if (content.find(strTarget) != -1 and strTarget != '*' ) or (strTarget == '*'):
					new_content = content.replace(strTarget, strReplace) if strTarget != '*' else strReplace
			
					f.seek(0)
					f.truncate()
					f.write(new_content)
					
					print('更新成功   ', end='')
				else:
					print('無須更新   ', end='')
					
		else:
			print('檔案不存在 ', end='')
			
		print(file)
	

if __name__ == "__main__":

	df = pd.read_excel('E:\Temp\Snowrunner\SnowrunnerChangeAttributes.xlsx', dtype=str).fillna('')
	#print(df)
	
	for iIndex, row in df.iterrows():
		if row['Enable'].upper() == 'V':
			if row['Action'] == 'Replace':
				doReplace(iIndex, row)
				
			if row['Action'] == 'Insert':
				doInsert(iIndex, row)
				
