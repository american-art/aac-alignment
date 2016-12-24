#!/usr/bin/env bash

CURR_PATH="$(pwd)"

# Check empty string.
if [ -z $1 ]; then
    echo "No such repo"
    exit
fi

# Check for AAC_ROOT variable
if [ -z "$AAC_ROOT" ]; then
	echo "AAC_ROOT not set. Halting!"
	echo "Use 'source <paths.sh>' to set required paths."
	exit
fi

# push generated data into github
# make sure there's no other update in master branch, or there will be a merge issue
# the github account is american-art-admin, you need to set up ssh key first.
echo "----------"
echo "1. Push generated data to Github"
REPO_PATH=$AAC_ROOT/aac-repos/$1
if [ ! -d $REPO_PATH ]; then
    echo "Repo doesn't exist. Nothing to push... settling with git clone"
    cd $AAC_ROOT/aac-repos
	git clone git@github.com:american-art/$1.git
else
	echo "Repo already exists. Doing git push..."
	cd $REPO_PATH
	git add .
	git commit -m "Applied updated model(s)"
	git remote set-url origin git@github.com:american-art/$1.git
	git push
fi

cd $CURR_PATH

# import into production triple store
echo -e "\n----------"
echo "2. Import into production triple store (american-art)"
python auto_import.py "$1" pro

echo -e "\n----------"
echo "DONE!"
