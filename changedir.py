import os
a=os.getcwd()
print 'you are currently under:',a
b=raw_input("Type in which dir you want to go:")
os.chdir(b)
d=os.getcwd()
print 'You are now inside:',d