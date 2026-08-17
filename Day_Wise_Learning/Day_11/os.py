#Make folders

import os
print(os.getcwd())
print(os.getcwdb())
os.makedirs("test",exist_ok=True)
print(os.path.join("test","filename.txt"))
os.removedirs("test")
# print(os.environ)