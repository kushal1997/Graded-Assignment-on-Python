
config_data = {}
section = ''

with open(".config",'r') as file:
    for line in file:
        # print(line)
        if line.startswith("["):
            # print(line[1:-2])
            section = line[1:-2]
            config_data[section] = {}
        elif '=' in line:
            # print(line.split("="))
            key, value = line.split("=")
            print("key,value",key,value)
            config_data[section][key]=value[:-1]

print("config data",config_data)