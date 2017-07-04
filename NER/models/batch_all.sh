#!/bin/bash

#SBATCH -A KORHONEN-SL3-GPU
#SBATCH -p tesla
#SBATCH -n 1
#SBATCH -t 120

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 WORDVECS [ARGS]" >&2
    exit 1
fi

#WORDVECS="$1"
WVDIR="$1"  #"/scratch/hwc25/eval/win/"
DATA="$2"
REPETITIONS="$3"
shift

BASEDIR="/home/hwc25/scratch/MTL-Bioinformatics-2016/models/"
#SCRIPTDIR="${BASEDIR}/keras/"
# CNN="/home/hwc25/scratch/MTL-Bioinformatics-2016/models/mlpy."
# DATADIR="${BASEDIR}/data/doc-10-class"

PARAMS="$@ --verbosity 0"

. /etc/profile.d/modules.sh
module purge
module load default-wilkes
module unload cuda
module load cuda/7.5 python/2.7.5
module load cudnn/4.0_cuda-7.5

#. $HOME/env/tensorflow-0.9/bin/activate
source ~/python/venv/bin/activate

export THEANO_FLAGS='mode=FAST_RUN,device=gpu,floatX=float32'
#mkdir win2-logs-"$DATA"-"$REPETITIONS"
#for v in "$WVDIR"/*.bin; do
echo "$WVDIR"
echo "$DATA"
echo "$REPETITIONS"
#filename="${v##*/}"
#mkdir logs
python baseline.py ../data/"$DATA" "$WVDIR"
	#echo "test" > logs/"$filename"-"$DATA"-"$REPETITIONS".txt
	
#done
#wait 
#mv logs/* win2-logs-"$DATA"-"$REPETITIONS"



#../data/"$DATA"

#python baseline.py "$DATA" "$WORDVECS"
# for d in "$DATADIR"/label-*; do
    
# done