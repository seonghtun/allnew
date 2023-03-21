#!/bin/bash

opt1=$1
opt2=$2

if [ $# -eq 2 ]; then
	if [ $opt1 == 'aaa' -a $opt2 == 'test' ] || [ $opt1 == 'test' -a $opt2 == 'aaa' ]; then
		echo good
	else
		echo bad
	fi
else
	echo "input two parameter...!!"
fi

