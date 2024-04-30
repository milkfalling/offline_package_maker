import os
import shutil

def copy_python_files(source_dir, dest_dir):
    # 確保目的地資料夾存在，若不存在則創建
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 遍歷源資料夾中的所有檔案和子資料夾
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.py'):
                # 構建源檔案的完整路徑
                source_file = os.path.join(root, file)
                # 構建目的地檔案的完整路徑，並在檔案名前加上'duplicate'前綴
                dest_file = os.path.join(dest_dir, 'duplicate_' + file)
                # 複製檔案
                shutil.copyfile(source_file, dest_file)
                print(f"已複製檔案: {source_file} 到 {dest_file}")

# 要複製的源資料夾路徑
source_directory = 'C:\BiDaETech'
# 目的地資料夾路徑（當前腳本的資料夾）
destination_directory = os.path.dirname(os.path.realpath(__file__))

# 呼叫函式開始複製
copy_python_files(source_directory, destination_directory)
