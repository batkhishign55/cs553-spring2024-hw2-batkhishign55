[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/4oeFqbG6)
### CS553 Cloud Computing Assignment 2 Repo
**Illinois Institute of Technology**  

**Student**:  
* Batkhishig Dulamsurankhor (bdulamsurankhor@hawk.iit.edu)  A20543498 

## File structure
```bash
├── README.md           # Readme file
├── bench               # benchmarking results
│   ├── cpu             # cpu benchmark results
│   ├── disk            # disk benchmark results
│   ├── mem             # memory benchmark results
│   └── net             # network benchmark results
├── bk_bench.sh         # benchmark script
├── bk_plot.py          # plotting script from raw log files
├── cpu.png
├── disk.png
├── hw2-report.pdf      # report pdf file
├── mem.png
└── net.png
```

## Running benchmark

Add execute privilege to ```bk_bench.sh```:
```bash
chmod +x bk_bench.sh
```

Run the test (for example cpu in baremetal):
```bash
./bk_bench.sh cpu baremetal
```

Output of the test will be in ```./bench/cpu/baremetal/``` directory with each log file created for different threads.

## Running benchmark in container/vm

Copy benchmark script:
```bash
scp bk_bench.sh username@hostaddress:~/
```

Ssh into container/vm
```bash
ssh username@hostaddress:
```

Run the test similar to running it in the host machine
```bash
./bk_bench.sh cpu container
```

Exit from container/vm
```bash
exit
```

Collect the results
```bash
scp -r username@hostaddress:/bench ./
```

## Plotting the graph from the raw log files
```bash
python3 bk_plot.py
```

