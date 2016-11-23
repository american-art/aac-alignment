#!/usr/bin/env bash

CURR_PATH="$(pwd)"

if [ -z $1 ]; then
    echo "No such repo"
    exit
fi

# git pull
echo "----------"
echo "1. Synchronize data from Github"
REPO_PATH="../../aac-repos/$1"
if [ ! -d $REPO_PATH ]; then
    echo "Repo directory doesn't exist"
    exit
fi
cd $REPO_PATH
git status
#git checkout -- .
#git pull
#git clean -fd
cd $CURR_PATH

# applay karma model
echo -e "\n----------"
echo "2. Apply Karma model"
CONFIG_FILE="workflow_config_${1}"
if [ ! -f "${CONFIG_FILE}.py" ]; then
    echo "Repo configuration file doesn't exist"
    exit
fi
# local version
spark-submit --archives ~/ISI/aac-dependencies/karma.zip --py-files ~/ISI/aac-dependencies/python-lib.zip --driver-class-path ~/ISI/softwares/Web-Karma/karma-spark/target/karma-spark-0.0.1-SNAPSHOT-shaded.jar auto_workflow.py $CONFIG_FILE
# server version
# /opt/aac-softwares/spark-1.5.0-cdh5.5.0/bin/spark-submit --archives /opt/aac-dependencies/karma.zip --py-files /opt/aac-dependencies/python-lib.zip --driver-class-path /opt/aac-softwares/Web-Karma/karma-spark/target/karma-spark-0.0.1-SNAPSHOT-shaded.jar auto_workflow.py $CONFIG_FILE

# import into triple store
echo -e "\n----------"
echo "3. Import into triple store"
python auto_import.py "$1" dev

echo -e "\n----------"
echo "DONE!"