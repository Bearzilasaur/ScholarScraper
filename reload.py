#quick snippet to reload modules while testing.

import importlib


def reload(function, module=None):
	importlib.reload(function) 
	if module !=None:
		try:
			from function import module
		except:
			print("\n"*10,"Unable to import function from module")
			pass
	elif module ==None:
		pass
	else:
		print("ERROR: How did you break this? Line: 17")