def format_config_data(config):
    formatted_data = []

    # iterate over each of the section in the data
    for section, values in config.items():
        
        # skip the filename key because further filename value is not iterable
        if section == "filename":  
            continue

        # add section name to get the formatted output
        formatted_data.append(f"{section}:")  

        # adding each key-value pair under the section as per the format 
        for key,value in values.items():
            formatted_data.append(f"- {key}: {value}")
    
    # return the formatted data lines
    return formatted_data