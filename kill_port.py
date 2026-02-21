import subprocess
import re

def find_pids(port=5000):
    out = subprocess.check_output(['netstat', '-ano'], text=True, errors='ignore')
    # match lines containing :port and capture PID
    pids = set(re.findall(rf":{port}\s+\S+\s+\S+\s+(\d+)", out))
    return pids

def kill_pids(pids):
    for pid in pids:
        try:
            subprocess.check_call(['taskkill', '/PID', pid, '/F'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print('killed', pid)
        except subprocess.CalledProcessError:
            print('failed', pid)

if __name__ == '__main__':
    pids = find_pids(5000)
    if not pids:
        print('no-pid')
    else:
        kill_pids(pids)
