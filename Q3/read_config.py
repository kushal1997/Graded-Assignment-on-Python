
config_data = {}
section = ''

try:
    with open(".config",'r') as file:
        for line in file:
            # print(line)
            if not line:
                continue
            if line.startswith("["):
                # print(line[1:-2])
                section = line[1:-2]
                config_data[section] = {}
            elif '=' in line:
                if section:
                    # print(line.split("="))
                    key, value = line.split("=")
                    print("key,value",key,value)
                    config_data[section][key]=value[:-1]
            else:
                print("Wrong line format",line)
except Exception as e:
    print("error : ",e)

print("config data",config_data)