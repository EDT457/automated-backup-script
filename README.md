# Automated Backup Script

A Python automation tool with a professional GUI that continuously monitors a source folder and backs up files to a destination, with real-time change detection and comprehensive logging.

## Project Overview

This project creates a practical backup automation solution that IT professionals use in real-world scenarios. The application features a user-friendly GUI that allows users to select folders via file browser, start/stop backups with a single click, and view real-time activity logs. The script performs an initial full backup, then continuously monitors the source folder for changes and automatically syncs them to the backup location.

## Features

- **GUI Interface** - Clean, intuitive interface with file browser buttons for easy folder selection
- **Initial Full Backup** - Recursively copies all files and folder structures from source to backup on startup
- **Continuous Monitoring** - Watches source folder for changes in real-time using the watchdog library
- **Change Detection** - Automatically detects and backs up:
  - New files created
  - Existing files modified
  - Deleted files (removes from backup)
- **Real-Time Activity Log** - Display all backup operations with timestamps directly in the GUI
- **Start/Stop Control** - Easy-to-use button that toggles between "Start Backup" (green) and "Stop Backup" (red)
- **Folder Structure Preservation** - Maintains the exact directory hierarchy in the backup
- **Comprehensive Logging** - All actions timestamped and logged to `backup_log.txt` for auditing
- **Error Handling** - Gracefully handles permission errors, missing files, and failed operations
- **Threading** - Background processing keeps the GUI responsive while backups run
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

The GUI will open with options to:
1. **Select Source Folder** - Click "Browse" to choose the folder to monitor and backup
2. **Select Backup Folder** - Click "Browse" to choose the destination for backups
3. **Start Backup** - Click the green "Start Backup" button to begin monitoring
4. **Monitor Activity** - Watch real-time logs in the Activity Log panel
5. **Stop Backup** - Click the red "Stop Backup" button to end monitoring

## How It Works

1. **Initial Backup** - On startup, all files from the source folder are copied to the backup location
2. **Monitoring** - The script watches the source folder for filesystem events
3. **Change Detection** - When files are created, modified, or deleted, the script automatically syncs the changes to backup
4. **Real-Time Updates** - All actions appear instantly in the GUI activity log
5. **File Logging** - Every action is also recorded with a timestamp in `backup_log.txt`

## GUI Features

- **File Browser Buttons** - Easily navigate and select folders instead of typing paths
- **Activity Log Display** - Real-time scrollable log showing all backup operations
- **Status Feedback** - Button changes color and text to reflect backup status
- **Non-Blocking Interface** - Backup runs in background thread, GUI stays responsive
- **Comprehensive Feedback** - See exactly what's being backed up and any errors that occur

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
- **Threading in Python** to keep GUIs responsive during long-running operations
- **Tkinter GUI development** including widgets, layout management, and event handling
- **Debouncing techniques** to prevent duplicate processing of rapid events
- Creating **professional logging systems** with timestamps for auditing
- **Real-time GUI updates** from background threads
- Handling real-world edge cases (permissions, missing files, concurrent modifications)
- **Error handling and recovery** in long-running processes
- Practical automation skills used by IT professionals and system administrators

## Use Cases

- Automated daily file backups for important documents
- Real-time synchronization of development files
- Compliance and audit logging for IT operations
- Protecting against accidental file deletion
- System administration automation tasks
- Personal file safety and disaster recovery

## Future Improvements

- Implement incremental backups with change tracking
- Add email notifications for backup failures
- Support for cloud storage backends (AWS S3, Azure Blob)
- Compression of backup files to save storage space
- Exclude certain file types or folders from backup
- Scheduled backups at specific times
- Backup versioning to keep multiple file versions
- Configuration file support for saving preferences


## Author

Ethan Tan
