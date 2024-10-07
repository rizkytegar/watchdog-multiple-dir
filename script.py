import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# This function sets up logging for the application
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level to INFO
        format='%(asctime)s - %(message)s',  # Format the log messages
        datefmt='%Y-%m-%d %H:%M:%S'  # Date format for log entries
    )

# Main function to monitor directories
def main(directories):
    # Create an event handler that logs file system events
    event_handler = LoggingEventHandler()
    
    # Create an Observer object that will monitor the file system
    observer = Observer()
    
    # Loop through each directory in the provided list
    for directory in directories:
        # Schedule the event handler for each directory, enabling recursive monitoring
        observer.schedule(event_handler, directory, recursive=True)
    
    # Start the observer
    observer.start()
    print("Monitoring started for directories:", directories)
    print("Press Ctrl+C to stop.")

    try:
        # Keep the program running indefinitely until interrupted
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer if a keyboard interrupt (Ctrl+C) is received
        observer.stop()
    observer.join()  # Wait for the observer to finish

if __name__ == "__main__":
    # Set up logging for the application
    setup_logging()
    
    # List of directories to monitor (up to 10)
    directories_to_watch = [
        '/path/to/directory1',  # Replace with actual directory paths
        '/path/to/directory2',
        '/path/to/directory3',
        '/path/to/directory4',
        '/path/to/directory5',
        '/path/to/directory6',
        '/path/to/directory7',
        '/path/to/directory8',
        '/path/to/directory9',
        '/path/to/directory10',
    ]

    # Call the main function with the list of directories
    main(directories_to_watch)
