#/usr/bin/env python3


# import sys
# import time
#
# for i in range(5):
#     sys.stdout.write('Processing {}\n'.format(i))
#     time.sleep(1)
#
# for i in range(5):
#     sys.stderr.write('Error {}\n'.format(i))
#     time.sleep(1)

import shlex
import subprocess

if __name__ == '__main__':
    shell_cmd = 'adb devices'
    # shell_cmd = 'adb devices'
    cmd = shlex.split(shell_cmd)
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    devlist = []
    while p.poll() is None:
        line = p.stdout.readline().decode()
        line = line.strip()
        if line.find('\tdevice') != -1:
            temp = line.split('\t')
            devlist.append(temp[0])
            print('Subprogram output: [{}]'.format(line))
        # print(line)
        # if line:
        #     if line.find('\tdevice') != -1:
        #         temp = line.split('\t')
        #         devlist.append(temp[0])
        #     print('Subprogram output: [{}]'.format(line))

    if p.returncode == 0:
        print('Subprogram success')
    else:
        print('Subprogram failed')
    # for i in range(len(line)):
    #     if line[i].find('\tdevice') != -1:
    #         temp = line[i].split('\t')
    #         devlist.append(temp[0])
    print('设备：', devlist)



# import sys
# import time
#
# for i in range(5):
#     sys.stdout.write('Processing {}\n'.format(i))
#     sys.stdout.flush()
#     time.sleep(1)
#
# for i in range(5):
#     sys.stderr.write('Error {}\n'.format(i))
#     sys.stderr.flush()
#     time.sleep(1)

