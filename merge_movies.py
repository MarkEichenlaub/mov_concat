import os
import subprocess

base_command = ['mencoder', '-oac', 'pcm' ,'-ovc', 'copy' ,'-idx' ,'-o']

path = input("What directory are the movies in?")

for folder, subfolders, files in os.walk(path):
	foldername = os.path.split(folder)[-1]
	command = base_command + [os.path.join(folder, '{}.avi'.format(foldername))]
	#get .MOV files
	movFiles = []
	for f in files:
		if f.endswith('.MOV'):
			movFiles.append(os.path.join(folder,f))
	
	movFiles.sort()

	if len(movFiles)>0:
		command += movFiles
		subprocess.Popen(command)
		print(command)
