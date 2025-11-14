from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import shutil
import time

def backup_files(source, dest):
    if not os.path.isdir(dest):
        os.makedirs(dest, exist_ok=True)
    if os.path.isdir(source):
        for file in os.listdir(source):
            if os.path.isfile(os.path.join(source, file)):
                source_file = os.path.join(source, file)
                dest_file = os.path.join(dest, file)
                try:
                    shutil.copy2(source_file,dest_file)
                    log_action("INITIAL BACKUP", source_file, "SUCCESS")
                except Exception as e:
                    log_action("INITIAL BACKUP", source_file, f"FAILED - {e}")
            else:
                backup_files(os.path.join(source, file), os.path.join(dest, file))

def log_action(action, file_path, status, log_file="Backup_log.txt"):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {action}: {file_path} - {status}\n"
    with open(log_file, "a") as f:
        f.write(log_entry)
    print(f"[{timestamp}] {action}: {file_path} - {status}")

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, source, backup, log_file):
        self.source = source
        self.backup = backup
        self.processed_files = {}
        self.log_file = log_file

    def should_process(self, file_path):
        current_time = time.time()
        last_time = self.processed_files.get(file_path, 0)

        if current_time - last_time < 1:
            return False
        
        self.processed_files[file_path] = current_time
        return True

    def on_modified(self, event):
        if not event.is_directory and self.should_process(event.src_path):
            source_file = event.src_path
            dest_file = source_file.replace(self.source, self.backup)
            print(f"File changed: {source_file}")
            try:
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(source_file,dest_file)
                log_action("FILE MODIFIED", source_file, "SUCCESS", self.log_file)
            except Exception as e:
                log_action("FILE MODIFIED", source_file, f"FAILED - {e}", self.log_file)

    def on_created(self, event):
        if not event.is_directory and self.should_process(event.src_path):
            source_file = event.src_path
            dest_file = source_file.replace(self.source, self.backup)
            print(f"File made: {source_file}")
            try:
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(source_file,dest_file)
                log_action("FILE CREATED", source_file, "SUCCESS", self.log_file)
            except Exception as e:
                log_action("FILE CREATED", source_file, f"FAILED - {e}", self.log_file)

    def on_deleted(self, event):
        if not event.is_directory and self.should_process(event.src_path):
            source_file = event.src_path
            dest_file = source_file.replace(self.source, self.backup)
            print(f"File removed from source: {event.src_path}")
            try:
                if os.path.exists(dest_file):
                    os.remove(dest_file)
                    log_action("FILE DELETED", source_file, "SUCCESS", self.log_file)
                else:
                    log_action("FILE DELETED", source_file, "NOT FOUND IN BACKUP", self.log_file)
            except Exception as e:
                log_action("FILE DELETED", source_file, f"FAILED - {e}", self.log_file)

 
def main():
    source = input("Source address: ")
    backup = input("Backup address: ")
    log_file = "backup_log.txt"

    if not os.path.isdir(source):
        print("Source folder does not exist")
        log_action("STARTUP", source, "SOURCE FOLDER NOT FOUND", log_file)
        return
    
    log_action("STARTUP", source, "BACKUP STARTED", log_file)
    backup_files(source, backup)

    event_handler = ChangeHandler(source, backup, log_file)
    observer = Observer()
    observer.schedule(event_handler, source, recursive=True)
    observer.start()
    print("Watching for changes...")
    log_action("MONITORING", source, "WATCHING FOR CHANGES", log_file)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        log_action("SHUTDOWN", source, "BACKUP STOPPED", log_file)
    
    observer.join()


if __name__ == "__main__":
    main()