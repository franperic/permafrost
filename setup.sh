#!/bin/bash
echo "Install relevant packages for the Permafrost project\nPrerequisits: python, pip"

# Install relevant packages
if [ -f ./requirements.txt ]
then
    pip install -r requirements.txt
else
	echo "The requirements file does not exist"
fi