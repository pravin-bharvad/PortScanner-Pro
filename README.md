# PortScanner-Pro

A multithreaded Python port scanner built for learning network security fundamentals.

## Features

- Multi-threaded scanning
- Thread limiting using Semaphore
- Custom port range input
- Scan summary with duration
- Open port count

## Technologies Used

- Python
- socket
- threading

## How It Works

The scanner attempts TCP connections to specified ports
and reports open ports. Thread limiting ensures stable
and efficient performance.

## Example Usage

python fast_scanner.py

Enter target IP (127.0.0.1):
Enter start port:
Enter end port:

## Educational Purpose

This project was built to understand:
- Network fundamentals
- Port scanning
- Concurrency control
- System resource management
