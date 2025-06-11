import os

def get_files_info(working_directory, directory=None):
    try:
        if not os.path.abspath(os.path.join(working_directory, directory or '')).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(os.path.abspath(os.path.join(working_directory, directory or ''))):
            return f'Error: "{directory}" is not a directory'
        
        files_info = []
        contents = os.listdir(os.path.join(working_directory, directory or ''))
        
        for item in contents:
            file = os.path.join(working_directory, directory, item)
            fileSize = os.path.getsize(file)
            isDir = os.path.isdir(file)

            files_info.append(f"- {item}: file_size={fileSize} bytes, is_dir={isDir}")
        return "\n".join(files_info)
    except Exception as e:
        return f'Error: {str(e)}'
    
def get_file_content(working_directory, file_path):
    try:
        if not os.path.abspath(os.path.join(working_directory, file_path)).startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(os.path.join(working_directory, file_path)) or not os.path.isfile(os.path.join(working_directory, file_path)):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(os.path.join(working_directory, file_path), 'r') as file:
            content = file.read()

            if len(content) > 10000:
                return f'{content[:10000]}[...File "{file_path}" truncated at 10000 characters]'            
            
            return content

    except Exception as e:
        return f'Error: {str(e)}'
    