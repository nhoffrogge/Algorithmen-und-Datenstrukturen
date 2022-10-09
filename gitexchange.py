import git

#git.Repo('https://github.com/nhoffrogge/Algorithmen-und-Datenstrukturen.git')

remoteurl= "https://github.com/nhoffrogge/pythonclonedemo.git"

localfolder= "C:\Users\00087043\Documents\5 - Training\software and coding\Python\exchange"

myrepo = git.Repo.clone_from(remoteurl, localfolder)
myrepo.git.checkout("")