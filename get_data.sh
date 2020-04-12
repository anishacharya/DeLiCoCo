#!/usr/bin/env bash
curr_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
data_dir=$curr_dir'/data'

mkdir -p "$data_dir"

if [ -f "$data_dir"'/epsilon_normalized.bz2' ]; then echo "epsilon exists skipping download"
else
	wget -t inf https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/epsilon_normalized.bz2
fi

if [ -f "$data_dir"'/rcv1_test.binary.bz2' ]; then echo "rcv1 exists skipping download"
else
	wget -t inf https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/rcv1_test.binary.bz2
fi

mv 'epsilon_normalized.bz2' "$data_dir"
mv 'rcv1_test.binary.bz2' "$data_dir"

echo "Processing epsilon"
python3 get_data_helper.py --i "$data_dir"'/epsilon_normalized.bz2' --o "$data_dir"'/epsilon_normalized.pickle'
echo "Processing rcv1"
python3 get_data_helper.py --i "$data_dir"'/rcv1_test.binary.bz2' --o "$data_dir"'/rcv1_test.pickle'