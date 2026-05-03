import shutil
import os
from datetime import datetime

source="/mnt/d/important_data" #for windows use: "D:/test_folder"
backup_dir="/mnt/d/backups" # for windows use: "D:/backups"
timestamp=datetime.now().strftime("%Y%m%d%H%M%S")
backup_file=os.path.join(backup_dir,f"backup_{timestamp}.zip")

shutil.make_archive(backup_file.replace('.zip',''),'zip',source)
print(f"Backup created at: {backup_file}")