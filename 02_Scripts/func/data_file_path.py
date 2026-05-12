def get_data_path(file_path, data_type="raw"):
    """
    Add prefix to link to data folder
    No need to use / in the initial of file_path
    data_type = "raw" or "processed", depending on the targeted folder, default to raw
    """
    if file_path.startswith("/"):
        file_path = file_path[1:]
    if data_type == "raw":
        return f"../01_Data/01_Raw_Data/{file_path}"
    elif data_type == "processed":
        return f"../01_Data/02_Processed_Data/{file_path}"
