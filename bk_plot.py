
# pip3 install matplotlib

import matplotlib.pyplot as plt
import os

virt = ['baremetal', 'container', 'vm']
paths = []
cpu_data = {'lat': [], 'eps': []}
mem_data = {'to': [], 'tp': []}
disk_data = {'to': [], 'tp': []}
net_data = {'lat': [], 'tp': []}

net_flag = ['0.0000-1.0000', '1.0000-2.0000', '2.0000-3.0000',
            '3.0000-4.0000', '4.0000-5.0000', '5.0000-6.0000',
            '6.0000-7.0000', '7.0000-8.0000', '8.0000-9.0000', '9.0000-10.0000']


def build_file_loc(type):
    global paths
    paths = []
    for v in virt:
        types = []
        for i in range(7):
            types.append(os.path.join(
                'bench', type, v, type+'_'+str(2**i)+'.log'))
        paths.append(types)


def extract_cpu_info():
    for types in paths:
        lat = []
        eps = []
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
        to = []
        tp = []
        for path in types:
            print(path)
            file = open(path, 'r')
            lines = file.readlines()
            to.append(float(lines[17][17:lines[17].index('(')]))
            tp.append(
                float(lines[19][lines[19].index('(')+1:lines[19].index(')')-7]))
        mem_data['to'].append(to)
        mem_data['tp'].append(tp)


def extract_disk_info():
    for types in paths:
        to = []
        tp = []
        for path in types:
            print(path)
            file = open(path, 'r')
            lines = file.readlines()
            to.append(float(lines[23][22:]))
            tp.append(float(lines[28][22:]))
        disk_data['to'].append(to)
        disk_data['tp'].append(tp)


def extract_net_info():
    for types in paths:
        lat = []
        tp = []
        for path in types:
            print(path)
            file = open(path, 'r')
            lines = file.readlines()

            lats = []
            tps = []
            for line in lines:
                for f in net_flag:
                    try:
                        line.index(f)
                        lats.append(
                            float(line[line.index('K/')+2:line.index('(')]))

                        lidx = 0
                        try:
                            lidx = line.index('GBytes')
                        except:
                            lidx = line.index('MBytes')

                        tps.append(float(line[lidx+6:line.index('Gbits/sec')]))
                    except Exception as e:
                        pass
            # print(lats)
            # print(tps)
            lat.append(round(sum(lats)/len(lats), 2))
            tp.append(round(sum(tps)/10, 2))
        net_data['lat'].append(lat)
        net_data['tp'].append(tp)


x = [1, 2, 4, 8, 16, 32, 64]


def plot_cpu_data():
    fig, axs = plt.subplots(2)
    axs[0].plot(x, cpu_data['eps'][0], label="baremetal")
    axs[0].plot(x, cpu_data['eps'][1], label="container")
    axs[0].plot(x, cpu_data['eps'][2], label="vm")
    axs[0].set_title('CPU - Events per Second')
    axs[0].legend()

    axs[1].plot(x, cpu_data['lat'][0], label="baremetal")
    axs[1].plot(x, cpu_data['lat'][1], label="container")
    axs[1].plot(x, cpu_data['lat'][2], label="vm")
    axs[1].set_title('CPU - Average Latency (ms)')
    axs[1].legend()

    fig.tight_layout()
    plt.savefig('cpu.png')


def plot_mem_data():

    fig, axs = plt.subplots(2)
    axs[0].plot(mem_data['to'][0], label="baremetal")
    axs[0].plot(mem_data['to'][1], label="container")
    axs[0].plot(mem_data['to'][2], label="vm")
    axs[0].set_title('Memory - Total Operations')
    axs[0].legend()

    axs[1].plot(mem_data['tp'][0], label="baremetal")
    axs[1].plot(mem_data['tp'][1], label="container")
    axs[1].plot(mem_data['tp'][2], label="vm")
    axs[1].set_title('Memory - Throughput (MiB/sec)')
    axs[1].legend()

    fig.tight_layout()
    plt.savefig('mem.png')


def plot_disk_data():

    fig, axs = plt.subplots(2)
    axs[0].plot(disk_data['to'][0], label="baremetal")
    axs[0].plot(disk_data['to'][1], label="container")
    axs[0].plot(disk_data['to'][2], label="vm")
    axs[0].set_title('Disk - Total Operations')
    axs[0].legend()

    axs[1].plot(disk_data['tp'][0], label="baremetal")
    axs[1].plot(disk_data['tp'][1], label="container")
    axs[1].plot(disk_data['tp'][2], label="vm")
    axs[1].set_title('Disk - Throughput (MiB/sec)')
    axs[1].legend()

    fig.tight_layout()
    plt.savefig('disk.png')


def plot_net_data():

    fig, axs = plt.subplots(2)
    axs[0].plot(net_data['lat'][0], label="baremetal")
    axs[0].plot(net_data['lat'][1], label="container")
    axs[0].plot(net_data['lat'][2], label="vm")
    axs[0].set_title('Network - Latency')
    axs[0].legend()

    axs[1].plot(net_data['tp'][0], label="baremetal")
    axs[1].plot(net_data['tp'][1], label="container")
    axs[1].plot(net_data['tp'][2], label="vm")
    axs[1].set_title('Network - Throughput (Gbits/sec)')
    axs[1].legend()

    fig.tight_layout()
    plt.savefig('net.png')


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

    build_file_loc('net')
    extract_net_info()
    plot_net_data()
    print(net_data)
