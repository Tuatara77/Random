import os
count = 1
if count < 100:
    with open(f"{count}.py", "r") as reader:
        with open(f"{count+1}.py", "w") as writer:
            lines = reader.readlines()
            for f in lines:
                if f[0:5] == "count": writer.write(f"count = {count+1}\n")
                else: writer.write(f)
    os.system(f"python {count+1}.py")