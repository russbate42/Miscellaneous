import subprocess, os, argparse

parser = argparse.ArgumentParser(
    prog='remove_all_condor',
    description='automated script to remove all files from condor queue.',
    epilog='Depending on the jobs, this may take a very long time to run.')
parser.add_argument('user',
    default=None,
    action='store',
    type=str)
parser.add_argument('--forcex', '-fx',
    dest='forcex',
    default='False',
    action='store_true')

args = parser.parse_intermixed_args()

if not args.user is None:
    USER = args.user
else:
    USER = subprocess.check_output(['echo', '$USER']).decode('utf-8')

if args.forcex == False:
    ForceX = ''
else:
    ForceX = '-forcex '

# Le crux
condor_q = subprocess.run('condor_q', stdout=subprocess.PIPE)
condor_q_grep = subprocess.run(['grep', '{} ID:'.format(USER)],
       input=condor_q.stdout, stdout=subprocess.PIPE)

print(' -- CONDOR QUEUE --\n')
print(condor_q.stdout.decode('utf-8'))
print()

job_list_raw = condor_q_grep.stdout.decode('utf-8').splitlines()

for job in job_list_raw:
    jobid = job.split()[2]
    print('\nWorking on job: {}'.format(jobid))
    
    Completed = True
    condor_transfer_data = subprocess.run(['condor_transfer_data',
        str(jobid)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if condor_transfer_data.returncode != 0:
        print('Failed to transfer data:')
        print(condor_transfer_data.stderr.decode('utf-8'))
        Completed = False
    else:
        print('  condor_transfer_data success.')

    rmv_str = 'condor_rm {}{}'.format(ForceX, jobid)
    condor_rm = subprocess.run(rmv_str.split(),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if condor_rm.returncode != 0:
        print('Failed to remove:')
        print(condor_rm.stderr.decode('utf-8'))
        Completed = False
    else:
        print('  condor_rm success.')
    
    if Completed == True:
        print('  ..Completed!\n')


