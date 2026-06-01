def get_data_path(file_path, data_type="raw"):
    import os
    """
    Add prefix to link to data folder
    No need to use / in the initial of file_path
    data_type = "raw" or "processed", depending on the targeted folder, default to raw

    It should work whether the script is run from project folder or 02_Script folder
    """

    # Remove / if it's there
    if file_path.startswith("/"):
        file_path = file_path[1:]

    # Check if script is run in folder data
    if {"01_Data", "02_Scripts"}.issubset(set(os.listdir())):
        add_string = ""
    else:
        add_string = "../"

    # Create file
    if data_type in ["raw", "r"]:
        return f"{add_string}01_Data/01_Raw_Data/{file_path}"
    elif data_type in ["processed", "p"]:
        return f"{add_string}01_Data/02_Processed_Data/{file_path}"
