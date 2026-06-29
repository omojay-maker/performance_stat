# Server Performance Stats

This repository contains a Bash script to analyse basic server performance stats.

Project URL: https://github.com/omojay-maker/performance_stat.git

How to Use
Save the script in your repository as server-stats.sh.

Make it executable:

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