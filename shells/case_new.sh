#!/bin/bash

if [ $# -ep 0 ]; then
	echo "Enter the contry name~!!"
else
	case "$1" in
		ko) echo "Seoul";;
		us) echo "Washington" ;;
		cn) echo "Beijing" ;;
		jp) echo "Tokyo" ;;
		*) echo "Your entery => $1 is not the list"
	esac
fi
