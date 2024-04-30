import os
import subprocess
import sys
import re

def get_imported_modules(file_path):
    imported_modules = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('import '):
                module_name = line.split('import ')[1].split()[0]
                imported_modules.add(module_name)
    return imported_modules

def compare_with_installed_modules(imported_modules):
    installed_modules = {module.split('==')[0].split('.')[0] for module in subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8').split('\n')}
    missing_modules = imported_modules - installed_modules
    return missing_modules

def find_missing_modules(folder_path):
    missing_modules = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                imported_modules = get_imported_modules(file_path)
                missing_modules.update(imported_modules)
    return missing_modules

def write_requirements_file(missing_modules, output_file='requirements.txt'):
    with open(output_file, 'w') as req_file:
        for module in missing_modules:
            # 使用正則表達式過濾掉模組名稱中的特殊符號
            module_name = re.sub(r'[^a-zA-Z0-9_-]', '', module)
            if module_name:  # 確保過濾後的模組名稱不為空
                req_file.write(module_name + '\n')

# 获取脚本所在的路径
script_path = os.path.dirname(__file__)

# 将脚本所在的路径作为要检查的文件夹路径
folder_path = script_path

# 查找缺少的模組
missing_modules = find_missing_modules(folder_path)

# 将缺少的模組存储到 requirements.txt 文件中
if missing_modules:
    write_requirements_file(missing_modules)
else:
    print("No missing modules found.")
