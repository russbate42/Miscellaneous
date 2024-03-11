
# Author R. Bate

import os, subprocess, sys

gpu_list = ['0', '1', '2', '3', '4', '5', '6', '7']
gpu_availability = ['Free']*8
gpu_dict = dict(zip(gpu_list, gpu_availability))
user_pid_dict = dict()
gpu_pid_dict = dict(zip(gpu_list, [[] for _ in range(8)]))

nvidia_process_string = 'nvidia-smi --query-compute-apps=pid '\
                        +'--format=csv,noheader'

# Get the list of processes using nvidia gpus
nv_proc = subprocess.run(nvidia_process_string.split(),
            stdout=subprocess.PIPE)
nvp_list = list(nv_proc.stdout.decode('utf-8').split())
nvidia_smi = subprocess.run('nvidia-smi',
                stdout=subprocess.PIPE
                )
nvp_list_unique = list(set(nvp_list))

# find the user associated with each process
grep_list = []
for nvp in nvp_list_unique:
    subp_out = subprocess.run('ps -aux'.split(),
                stdout=subprocess.PIPE)
    grep_out = subprocess.run('grep {}'.format(nvp).split(),
                input=subp_out.stdout,
                stdout=subprocess.PIPE
                ).stdout.decode('utf-8')
    grep_out_list = grep_out.split()

    user = grep_out_list[0]
    pid = grep_out_list[1]

    user_pid_dict[pid] = user
    
    # now grep nvidia-smi for user process
    grep_pid = subprocess.run('grep {}'.format(nvp).split(),
                input=nvidia_smi.stdout,
                stdout=subprocess.PIPE
                ).stdout.decode('utf-8')
    grep_list.append(grep_pid)

    for line in grep_pid.splitlines():
        splitline = line.split()
        pid_2 = splitline[4]
        gpu = splitline[1]
        gpu_pid_dict[gpu].append(pid_2)

## Print the output
print('+'+'-'*30+'+')
print('| GPU | user and processes ')
print('+'+'-'*30+'+')
for gpu in gpu_list:

    print('| {}  :'.format(gpu))
    gpu_pids = gpu_pid_dict[gpu]
    gpu_users = []
    for gpu_pid in gpu_pids:
        gpu_users.append(user_pid_dict[gpu_pid])

    if len(gpu_users) == 0:
        print('\t\tFree')
        continue

    for user, pid in zip(gpu_users, gpu_pids):
        print('|\t\t{}: {}'.format(user,pid))
print('+'+'-'*30+'+')

