from functions.get_files_info import get_file_content

print(f'{get_file_content("calculator", "main.py")}')
print(f'{get_file_content("calculator", "pkg/calculator.py")}')
print(f'{get_file_content("calculator", "/bin/cat")}')
