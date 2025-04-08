# function to read a configuration file
def config_reader(filename):
    config_data = {}
    section = ''

    try:
        with open(filename,'r') as file:
            for line in file:
                if not line: # skip empty lines
                    continue
                if line.startswith("["):
                    # extract section name separately from [Database] to 'Database'
                    section = line[1:-2].strip()
                    config_data[section] = {}
                elif '=' in line:
                    if section:

                        # split key & value with striping extra spaces
                        key, value = line.split("=")
                        config_data[section][key.strip()]=value.strip()
                else:
                    print("Wrong line format",line)

    # handle if no file is passed
    except FileNotFoundError:
        print("File not found")

    # handle any I/O error
    except IOError:
        print("Can't read file")

    # catch all unexpected errors
    except Exception as e:
        print("error : ",e)

    return config_data