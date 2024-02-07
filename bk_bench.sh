#!/bin/bash


usage() {
  echo "Usage: $0 <mode> <virt-type>"
  echo "Example: $0 cpu container"
  exit 1
}

if [ $# -ne 2 ]; then
  usage
fi

mode=$1
virt=$2

echo "Running $mode benchmarks in $virt..."

mkdir -p ./bench/$mode/$virt

if [ $mode = "disk" ]; then
   echo -e "\tPreparing dataset..."
   sysbench fileio --file-num=128 --file-block-size=4096 --file-total-size=120G --file-test-mode=rndrd --file-io-mode=sync --file-extra-flags=direct prepare
fi

for i in 1 2 4 8 16 32 64
do
   case $mode in
      "cpu")
         sysbench cpu --cpu-max-prime=100000 --threads=$i run > ./bench/$mode/$virt/${mode}_$i.log ;;
      "mem")
	      sysbench memory --memory-block-size=1K --memory-total-size=120G --threads=$i run > ./bench/$mode/$virt/${mode}_$i.log ;;
      "disk")
         sysbench fileio --file-num=128 --file-block-size=4096 --file-total-size=120G --file-test-mode=rndrd --file-io-mode=sync --file-extra-flags=direct --threads=$i run > ./bench/$mode/$virt/${mode}_$i.log ;;
      "net")
	      iperf -c 127.0.0.1 -e -i 1 --nodelay -l 8192K --trip-times --parallel $i >> ./bench/$mode/$virt/${mode}_$i.log ;;
   esac
   echo -e "\tRan with $i threads."
   sleep 1
done


if [ $mode = "disk" ]; then
   echo -e "\tCleaning up dataset..."
   sysbench fileio --file-num=128 --file-block-size=4096 --file-total-size=120G --file-test-mode=rndrd --file-io-mode=sync --file-extra-flags=direct cleanup
fi
