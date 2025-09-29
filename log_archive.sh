#!/bin/bash

LOG_DIR=$1
if [ -z "$LOG_DIR" ]; then
	echo "Usage: log-archive <log-directory>"
	exit 1
fi

if [ -d "$LOG_DIR" ] && [ -r "$LOG_DIR" ]
then
	TIMESTAMP=$(date +"%Y%m%d_%H%M%S" )
	mkdir -p archives
	tar -czf ./archives/logs_archive_$TIMESTAMP.tar.gz $LOG_DIR
	echo "$LOG_DIR, $TIMESTAMP, ./archives/logs_archive_$TIMESTAMP.tar.gz" >> archive_history.log


else 
	echo "Error: Invalid or unreadable directory"
	exit 1

fi


