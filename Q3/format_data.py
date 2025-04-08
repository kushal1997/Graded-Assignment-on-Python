def format_config_data(config):
    formatted_data = []
    for section, values in config.items():
        # print(section,values)
        if section == "filename":
            continue

        formatted_data.append(f"{section}:")
        for key,value in values.items():
            # print(f"key ========== > {key}, value ============> {value}")
            formatted_data.append(f"- {key}: {value}")
    return formatted_data