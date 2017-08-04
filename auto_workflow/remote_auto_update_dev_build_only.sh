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
	echo "Use 'source paths.sh' to set required paths."
	exit
fi

# Check for spark-submit command
ss=`which spark-submit`
if [ -z "$ss" ]; then
	echo "Spark-submit not in the path. Halting!"
	echo "Use 'source paths.sh' to set required paths."
	exit
fi

# Get latest data.
echo -e "\n----------"
echo "1. Synchronize data from Github"
REPO_PATH=$AAC_ROOT/aac-repos/$1
if [ ! -d $REPO_PATH ]; then
    echo "Repo doesn't exist. Doing git clone..."
    cd $AAC_ROOT/aac-repos
	git clone git@github.com:american-art/$1.git
else
	echo "Repo already exists. Doing git clean n pull..."
	cd $AAC_ROOT/aac-repos/$1
	git checkout -- .
	git clean -fd
	git pull
fi
cd $CURR_PATH

if [ $? -eq 0 ]
then
  echo "Successfully synchronized data"
else
  echo "Couldn't synchronize data"
  exit
fi

# applay karma model
echo -e "\n----------"
echo "2. Apply Karma model"
CONFIG_FILE="workflow_config_${1}"
if [ ! -f "${CONFIG_FILE}.py" ]; then
    echo "Repo configuration file doesn't exist"
    exit
fi
spark-submit --archives $AAC_ROOT/aac-dependencies/karma.zip --py-files $AAC_ROOT/aac-dependencies/python-lib.zip \
--executor-memory 1g \
--num-executors 1 \
--executor-cores 1 \
--driver-class-path $AAC_ROOT/aac-softwares/Web-Karma/karma-spark/target/karma-spark-0.0.1-SNAPSHOT-shaded.jar \
auto_workflow.py $CONFIG_FILE
#custom_workflow.py "/opt/aac-repos/cbm/CBMAA_Roles/LOD CBMAA Constituents.csv" /opt/aac-out/

if [ $? -eq 0 ]
then
  echo "Successfully applied all models"
else
  echo "Error occurred while applying models"
  exit
fi

# # import into dev triple store
# echo -e "\n----------"
# echo "3. Import into dev triple store (american-art-dev)"
# python auto_import.py "$1" dev

# echo -e "\n----------"
# echo "Test your data at http://localhost:3030/american-art-dev/query or http://data.americanartcollaborative.org/sparql_dev"
echo "DONE!"
