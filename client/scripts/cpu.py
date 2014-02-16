#!/usr/bin/env python
import commands


def monitor():
	shell_command = 'sar 1 3| grep "^Average:"'

	status,result = commands.getstatusoutput(shell_command)

	user,nice,system,iowait,steal,idle = result.split()[2:]

	value_dic = {
		'user': user,
		'nice': nice,
		'system': system,
		'iowait': iowait,
		'steal': steal,
		'idle': idle
	}
	return value_dic

if __name__ == '__main__':
	print monitor()