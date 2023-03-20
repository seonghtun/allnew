#!/bin/bash

a=1

while [ $a != "0" ]; do
	echo -n "input : "
	read a
	
	if [ $a != "0" ] ; then
		if [ $a -gt 9 ]; then
			echo "The numer of inputs must be between 2 and 9."
 		elif [ $a -lt 2 ]; then
                	echo "The numer of inputs must be between 2 and 9." 
		else
			for ((k=1; k<=9; k++)) do
				echo " $a * $k = `expr $a \* $k `"
			done
		fi
	fi
done
echo Exit

