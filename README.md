# Automated Backup Script

A Python automation tool that continuously monitors a source folder and backs up files to a destination, with real-time change detection and comprehensive logging.

## Project Overview

This project creates a practical backup automation solution that IT professionals use in real-world scenarios. The script performs an initial full backup, then continuously monitors the source folder for changes (new files, modifications, deletions) and automatically syncs them to the backup location.

## Features

- **Initial Full Backup** - Recursively copies all files and folder structures from source to backup on startup
- **Continuous Monitoring** - Watches source folder for changes in real-time using the watchdog library
- **Change Detection** - Automatically detects and backs up:
  - New files created
  - Existing files modified
  - Deleted files (removes from backup)
- **Folder Structure Preservation** - Maintains the exact directory hierarchy in the backup
- **Comprehensive Logging** - All actions timestamped and logged to `backup_log.txt` for auditing
- **Error Handling** - Gracefully handles permission errors, missing files, and failed operations
- **Debouncing** - Prevents duplicate backups from rapid filesystem events

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
pip install watchdog
```

### Running the Script

```bash
python abs.py
```

The script will prompt you for:
1. **Source address** - The folder path to monitor and backup (e.g., `C:\Users\Documents\MyFiles`)
2. **Backup address** - The destination folder for backups (e.g., `C:\Backups\MyFiles`)

Once started, the script runs continuously. Press `Ctrl+C` to stop.

## How It Works

1. **Initial Backup** - On startup, all files from the source folder are copied to the backup location
2. **Monitoring** - The script watches the source folder for filesystem events
3. **Change Detection** - When files are created, modified, or deleted, the script automatically syncs the changes to backup
4. **Logging** - Every action is recorded with a timestamp in `backup_log.txt`

## Log File Format

The `backup_log.txt` file records all operations:

```
[2025-11-14 14:32:15] STARTUP: source - BACKUP STARTED
[2025-11-14 14:32:15] INITIAL BACKUP: C:\source\file1.txt - SUCCESS
[2025-11-14 14:32:20] FILE CREATED: C:\source\newfile.txt - SUCCESS
[2025-11-14 14:32:25] FILE MODIFIED: C:\source\newfile.txt - SUCCESS
[2025-11-14 14:32:30] FILE DELETED: C:\source\oldfile.txt - SUCCESS
[2025-11-14 14:32:35] SHUTDOWN: source - BACKUP STOPPED
```

## What I Learned

Building this project taught me:

- Working with the **watchdog library** for filesystem event monitoring
- Understanding **file system operations** and how to handle them programmatically
- Implementing **recursive file operations** to handle nested folder structures
- **Debouncing techniques** to prevent duplicate processing of rapid events
- Creating **professional logging systems** with timestamps for auditing
- Handling real-world edge cases (permissions, missing files, concurrent modifications)
- **Error handling and recovery** in long-running processes
- Practical automation skills used by IT professionals and system administrators

## Use Cases

- Automated daily file backups for important documents
- Real-time synchronization of development files
- Compliance and audit logging for IT operations
- Protecting against accidental file deletion
- System administration automation tasks

## Future Improvements

- Add configuration file support for saving source/backup paths
- Implement incremental backups with change tracking
- Add email notifications for backup failures
- Create a GUI interface with monitoring dashboard
- Support for cloud storage backends (AWS S3, Azure Blob)
- Compression of backup files to save storage space
- Exclude certain file types or folders from backup
- Scheduled backups at specific times
- Backup versioning to keep multiple file versions

## Project Structure

```
├── abs.py
├── backup_log.txt
└── README.md
```

## Author

Ethan Tan

## Note

This project aligns with CompTIA A+ certification topics including file systems, automation, and system administration practices.
