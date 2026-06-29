assignment by https://roadmap.sh/projects/server-stats
Server Performance Stats
A lightweight Python script to analyse basic server performance stats.
This tool provides a quick snapshot of your system’s resource usage, helping you debug performance issues or get a better understanding of server load.

Features
Total CPU usage (percentage)

Total memory usage (free, used, and percentage)

Total disk usage (free, used, and percentage) – for the root partition

Top 5 processes by CPU usage

Top 5 processes by memory usage

Optional stretch goals (see below)

Requirements
Python 3.6 or higher

psutil library

Installation
Clone this repository or download the script file.

Install the required dependency:

bash
pip install psutil
Make the script executable (optional on Linux/macOS):

bash
chmod +x server-stats.sh
Run it:

bash
./server-stats.sh
Sample Output
text
========================================
       SERVER PERFORMANCE STATS
========================================

--- CPU Usage ---
Total CPU Usage: 12%

--- Memory Usage ---
Total Memory: 7856MiB
Used Memory:  4200MiB
Free Memory:  3656MiB
Usage:        53%

--- Disk Usage (/) ---
Total Disk:   100G
Used Disk:    45G
Free Disk:    55G
Usage:        45%

--- Top 5 Processes by CPU Usage ---
PID	COMMAND		%CPU
1234	node		45.2
5678	nginx		12.1
9101	mysql		8.5
1122	java		5.3
3344	sshd		2.0

========================================
