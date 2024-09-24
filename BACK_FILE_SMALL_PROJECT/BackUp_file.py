import shutil
import datetime
import os

today = datetime.date.today()
def backup_files(source,destination):
    backup_file_name = os.path.join(destination, f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)
source = "/Users/ATGWORKS/Python"
destination = "/Users/ATGWORKS/Python/BACK_FILE_SMALL_PROJECT"
backup_files(source,destination)