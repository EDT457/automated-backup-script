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
                except Exception as e:
                    print(f"Failed to copy {source_file}: {e}")
            else:
                backup_files(os.path.join(source, file), os.path.join(dest, file))

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, source, backup):
        self.source = source
        self.backup = backup

    def on_modified(self, event):
        if not event.is_directory:
            source_file = event.src_path
            dest_file = source_file.replace(self.source, self.backup)
            print(f"File changed: {source_file}")
            try:
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(source_file,dest_file)
            except Exception as e:
                print(f"Failed to copy {source_file}: {e}")

    def on_created(self, event):
        if not event.is_directory:
            source_file = event.src_path
            dest_file = source_file.replace(self.source, self.backup)
            print(f"File made: {source_file}")
            try:
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(source_file,dest_file)
            except Exception as e:
                print(f"Failed to copy {source_file}: {e}")

    def on_deleted(self, event):
        if not event.is_directory:
            source_file = event.src_path
            dest_file = source_file.replace(self.source, self.backup)
            print(f"File removed from source: {event.src_path}")
            try:
                if os.path.exists(dest_file):
                    os.remove(dest_file)
                    print(f"Deleted from backup: {dest_file}")
                else:
                    print(f"File not found in backup: {dest_file}")
            except Exception as e:
                print(f"Failed to delete {dest_file}: {e}")

 
def main():
    source = input("Source address: ")
    backup = input("Backup address: ")
    if not os.path.isdir(source):
        print("Source folder does not exist")
    backup_files(source, backup)
    event_handler = ChangeHandler(source, backup)
    observer = Observer()
    observer.schedule(event_handler, source, recursive=True)
    observer.start()
    print("Watching for changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()


if __name__ == "__main__":
    main()