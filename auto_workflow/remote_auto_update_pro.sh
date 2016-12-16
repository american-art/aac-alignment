#!/usr/bin/env bash

CURR_PATH="$(pwd)"

if [ -z $1 ]; then
    echo "No such repo"
    exit
fi

# push generated data into github
# make sure there's no other update in master branch, or there will be a merge issue
echo "----------"
echo "1. Push generated data to Github"
REPO_PATH="../../aac-repos/$1"
if [ ! -d $REPO_PATH ]; then
    echo "Repo directory doesn't exist"
    exit
fi
cd $REPO_PATH
git american-art-admin push
cd $CURR_PATH

# import into triple store
echo -e "\n----------"
echo "2. Import into triple store"
python auto_import.py "$1" pro

echo -e "\n----------"
echo "DONE!"