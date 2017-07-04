#!/bin/bash

SLEEPTIME=1    # Seconds to sleep between invoking sbatch
REPETITIONS=3    # Number of repetitions to run
#WVDIR="/scratch/hwc25/eval/win/"
WVDIR="../vec/" # folder contains all vector
#WVDIR="/scratch/hwc25/eval/chosen_vec/"


data=("BC4CHEMD" "JNLPBA" "AnatEM-IOB" "BC2GM-IOB")
for d in "${data[@]}"; do
	for i in $(seq $REPETITIONS); do
		for v in "$WVDIR"/*.bin; do
			echo "$d" "$v"
			python baseline.py ../data/"$d" "$v"
		done
	#wait
	done
done
