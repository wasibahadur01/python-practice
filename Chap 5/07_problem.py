s=set(1,2,3,4,'wasi',[1,2])
s.update[4][0]=9
# The code has multiple issues. Here is the corrected version:
print(s)