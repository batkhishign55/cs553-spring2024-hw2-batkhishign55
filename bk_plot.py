
# pip3 install matplotlib

import matplotlib.pyplot as plt
import os

virt=['baremetal','container','vm']
paths=[]
cpu_data={'lat':[], 'eps':[]}
mem_data={'to':[], 'tp':[]}
disk_data={'to':[], 'tp':[]}

def build_file_loc(type):
    global paths
    paths=[]
    for v in virt:
        types=[]
        for i in range(7):
            types.append(os.path.join('bench',type,v,type+'_'+str(2**i)+'.log'))
        paths.append(types)

def extract_cpu_info():
    for types in paths:
        lat=[]
        eps=[]
        for path in types:
            print(path)
            file = open(path, 'r')
            lines = file.readlines()
            lat.append(float(lines[23][22:]))
            eps.append(float(lines[14][22:]))
        cpu_data['lat'].append(lat)
        cpu_data['eps'].append(eps)

def extract_mem_info():
    for types in paths:
        to=[]
        tp=[]
        for path in types:
            print(path)
            file = open(path, 'r')
            lines = file.readlines()
            to.append(float(lines[17][17:lines[17].index('(')]))
            tp.append(float(lines[19][lines[19].index('(')+1:lines[19].index(')')-7]))
        mem_data['to'].append(to)
        mem_data['tp'].append(tp)

def extract_disk_info():
    for types in paths:
        to=[]
        tp=[]
        for path in types:
            print(path)
            file = open(path, 'r')
            lines = file.readlines()
            to.append(float(lines[23][22:]))
            tp.append(float(lines[28][22:]))
        disk_data['to'].append(to)
        disk_data['tp'].append(tp)

def plot_cpu_data():

    plt.plot(cpu_data['eps'][0], label = "baremetal") 
    plt.plot(cpu_data['eps'][1], label = "container") 
    plt.plot(cpu_data['eps'][2], label = "vm")
    plt.title('Events per Second')
    plt.legend() 
    plt.show()

    plt.plot(cpu_data['lat'][0], label = "baremetal") 
    plt.plot(cpu_data['lat'][1], label = "container") 
    plt.plot(cpu_data['lat'][2], label = "vm")  
    plt.title('Average Latency (ms)')
    plt.legend() 
    plt.show()

def plot_mem_data():

    plt.plot(mem_data['to'][0], label = "baremetal") 
    plt.plot(mem_data['to'][1], label = "container") 
    plt.plot(mem_data['to'][2], label = "vm")
    plt.title('Total Operations')
    plt.legend() 
    plt.show()

    plt.plot(mem_data['tp'][0], label = "baremetal") 
    plt.plot(mem_data['tp'][1], label = "container") 
    plt.plot(mem_data['tp'][2], label = "vm")  
    plt.title('Throughput (MiB/sec)')
    plt.legend() 
    plt.show()

def plot_disk_data():

    plt.plot(disk_data['to'][0], label = "baremetal") 
    plt.plot(disk_data['to'][1], label = "container") 
    plt.plot(disk_data['to'][2], label = "vm")
    plt.title('Total Operations')
    plt.legend() 
    plt.show()

    plt.plot(disk_data['tp'][0], label = "baremetal") 
    plt.plot(disk_data['tp'][1], label = "container") 
    plt.plot(disk_data['tp'][2], label = "vm")  
    plt.title('Throughput (MiB/sec)')
    plt.legend() 
    plt.show()


if __name__ == "__main__":
    build_file_loc('cpu')
    extract_cpu_info()
    plot_cpu_data()
    print(cpu_data)

    build_file_loc('mem')
    extract_mem_info()
    plot_mem_data()
    print(mem_data)
    
    build_file_loc('disk')
    extract_disk_info()
    plot_disk_data()
    print(disk_data)