import os
import shutil
import datetime
import time


src_folder = r'C:\Users\zaheeb.shah\Desktop\prop'
dst_folder = r'C:\Users\zaheeb.shah\Desktop\prop2'


start_time = time.time()

while True:
    
    files = os.listdir(src_folder)
    
    
    if len(files) > 0:
        
        for file in files:
            
            file_path = os.path.join(src_folder, file)
            
            
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            
            
            new_file_name = f'{current_date}_{file}'
            
            
            dst_file_path = os.path.join(dst_folder, new_file_name)
            
            
            shutil.move(file_path, dst_file_path)
            
            print(f'Moved {file} to {dst_folder} and renamed it to {new_file_name}')
    
    
    time.sleep(5)
    
    
    elapsed_time = time.time() - start_time
    if elapsed_time >= 60:
        break
