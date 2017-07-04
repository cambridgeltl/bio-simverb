#!/bin/bash
# script to batch evaluate on all intrinsic evaluation




# model to evaluate:


FILES=$(find $1 -maxdepth 1 -type f -name '*.bin')
for file in $FILES
do
	echo $file
	filename="${file##*/}"
	echo $filename
	
	python evalrank.py -q $file word-similarities/simVerb-3500/data/SimVerb_2col.txt
	python evalrank.py -q $file word-similarities/SimLex-999/SimLex-999.txt
	python evalrank.py -q $file word-similarities/bio-simverb/Bio-SimVerb.txt
	python evalrank.py -q $file word-similarities/bio-simlex/Bio-SimLex.txt
	python evalrank.py -q $file word-similarities/UMNSRS/UMNSRS-sim.txt
	python evalrank.py -q $file word-similarities/UMNSRS/UMNSRS-rel.txt
	python evalrank.py -q $file word-similarities/MayoSRS/MayoSRS.txt
done
wait

