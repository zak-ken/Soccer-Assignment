#!/bin/bash
# get current working directory
path=$(pwd)
echo ${path}

##create virtual python env here
virtualenv "${path}/vp" --python=python2.7

# Run python script (test all commands)
echo Executing the following command: python ${path}/script.py --file ${path}/data/data.txt
${path}/vp/bin/python2.7 ${path}/script.py --file ${path}/data/data.txt
echo Complete...
echo Executing the following command: python ${path}/script.py --multiple_files ${path}/data/multiple_files
${path}/vp/bin/python2.7 ${path}/script.py --multiple_files ${path}/data/multiple_files
echo Complete...
echo Executing the following command: python ${path}/script.py --multiple_files  "['${path}/data/multiple_files/data.txt', '${path}/data/multiple_files/data1.txt', '${path}/data/multiple_files/data1.txt']"
${path}/vp/bin/python2.7 ${path}/script.py --multiple_files  "['${path}/data/multiple_files/data.txt', '${path}/data/multiple_files/data1.txt', '${path}/data/multiple_files/data1.txt']"
echo Complete...
echo Executing the following command: python ${path}/script.py --multiple_files "['${path}/data/multiple_files/data.txt', '${path}/data/multiple_files/data1.txt', '${path}/data/multiple_files/data1.txt']" --file ${path}/data/data.txt
${path}/vp/bin/python2.7 ${path}/script.py --multiple_files "['${path}/data/multiple_files/data.txt', '${path}/data/multiple_files/data1.txt', '${path}/data/multiple_files/data1.txt']" --file ${path}/data/data.txt
echo Complete...
echo Executing the following command: python ${path}/script.py --multiple_files ${path}/data/multiple_files --file ${path}/data/data.txt
${path}/vp/bin/python2.7 ${path}/script.py --multiple_files ${path}/data/multiple_files --file ${path}/data/data.txt
echo Complete...
#Remove virtual python env
rm -r ${path}/vp





