# Log Archive Tool

This is a Bash command-line tool that archives logs from a specified directory into a compressed `tar.gz` file with a timestamp and logs the archiving action to a file. It’s designed to help keep systems clean by compressing and storing logs for future reference.

## Features
- Accepts a log directory as a command-line argument (e.g., `./log_archive.sh /var/log`).
- Compresses the directory into a `tar.gz` file with a timestamp (e.g., `logs_archive_20250929_130000.tar.gz`).
- Stores archives in an `archives/` directory.
- Logs the archiving action (directory, timestamp, archive file) to `archive_history.log`.

## Requirements
- A Unix-based system (e.g., Linux, macOS) with Bash and `tar` installed.
- A directory containing logs to archive.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/log-archive-tool.git
   cd log-archive-tool
   ```
2. Make the script executable:
   ```bash
   chmod +x log_archive.sh
   ```

## Usage
Run the script with a log directory as an argument:
```bash
./log_archive.sh <log-directory>
```
Example:
```bash
./log_archive.sh /var/log
```
This creates `archives/logs_archive_YYYYMMDD_HHMMSS.tar.gz` and logs the action to `archive_history.log`.

## Error Handling
- If no directory is provided: Shows `Usage: log-archive <log-directory>` and exits.
- If the directory is invalid or unreadable: Shows `Error: Invalid or unreadable directory` and exits.

## Project Structure
- `log_archive.sh`: The main Bash script.
- `archives/`: Directory for storing `tar.gz` archives.
- `archive_history.log`: Log file for archiving actions.
- `LICENSE`: Project license (e.g., MIT).
- `README.md`: This file.

## Testing
To test the script:
1. Create a test directory with sample files:
   ```bash
   mkdir test_logs
   touch test_logs/log1.txt
   ```
2. Run the script:
   ```bash
   ./log_archive.sh test_logs
   ```
3. Verify the archive in `archives/` and the log entry in `archive_history.log`.

## Future Enhancements
- Add scheduling with `cron` for automatic archiving.
- Integrate Python for advanced features like emailing or cloud storage.

## License
MIT License (see `LICENSE` file).
