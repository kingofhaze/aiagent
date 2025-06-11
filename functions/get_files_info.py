import os

def get_files_info(working_directory, directory=None):
    if not os.path.abspath(os.path.join(working_directory, directory or '')).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(os.path.abspath(os.path.join(working_directory, directory or ''))):
        return f'Error: "{directory}" is not a directory'
    
    files_info = []
    try:
        contents = os.listdir(os.path.join(working_directory, directory or ''))
        
        for item in contents:
            file = os.path.join(working_directory, directory, item)
            fileSize = os.path.getsize(file)
            isDir = os.path.isdir(file)

            files_info.append(f"- {item}: file_size={fileSize} bytes, is_dir={isDir}")
        return "\n".join(files_info)
    except Exception as e:
        return f'Error: {str(e)}'
    