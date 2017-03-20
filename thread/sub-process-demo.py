import subprocess

print('$ nslookup www.dianping.com')
r = subprocess.call(['nslookup', 'www.dianping.com'])
print('Exit code:', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\nbaidu.com\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)