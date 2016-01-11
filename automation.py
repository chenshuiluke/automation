from backup import Backup
import json
import shutil
def createBackup(backups):
	print(backups)
	backup = Backup()
	backup.getUserInput()
	backups['backups'].append(json.loads(backup.returnJson()))
	with open("presets.json", "w") as jsonWriter:
		jsonWriter.write(json.dumps(backups, sort_keys = True, indent = 4))
def getBackups():
	backups = None
	try:
		with open("presets.json", "r") as jsonFile:
			backups = json.load(jsonFile)
	except:
		backups = { "backups" : []}
	return backups

def runBackups(backups):
	for backup in backups['backups']:
		print("copying from {} to {}".format(backup['origin'], backup['destination']))
		try:
			shutil.copytree(backup['origin'], backup['destination'] + "/" + backup['origin'])
		except (shutil.Error, FileExistsError) as err:
			if type(err) == "shutil.Error":
				errors = err[0]
				for error in errors:
					src, dst, why = error
					print("Error copying {} : {}", src, why)
		print("done copying")

def main():
	choice = None
	backups = getBackups()
	while choice == None or choice != "3":
		choice = input("1. Define new backup\n2. Run backups\n3. Exit\n")
		if choice == "1":
			createBackup(backups)
		if choice == "2":
			runBackups(backups)
if(__name__ == "__main__"): main()
