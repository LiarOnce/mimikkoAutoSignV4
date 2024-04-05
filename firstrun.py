import os

base_path = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(base_path + "/log"):
    os.makedirs(f"{base_path}/log", mode=777)
    os.system(f"chmod 777 {base_path}/log")