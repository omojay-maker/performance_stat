Assignment by https://roadmap.sh/projects/server-stats

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
chmod +x server_stats.py
Usage
Run the script from the terminal:

bash
python server_stats.py
Or if you made it executable:

bash
./server_stats.py
No command‑line arguments are needed – the script will display all stats immediately.

Output Example
text
============================================================
  CPU USAGE
============================================================
Total CPU Usage: 12.3%

============================================================
  MEMORY USAGE
============================================================
Total:     16.00 GB
Available: 10.24 GB
Used:      5.76 GB
Percentage: 36.0%

============================================================
  DISK USAGE (/)
============================================================
Total:     512.00 GB
Used:      320.00 GB
Free:      192.00 GB
Percentage: 62.5%

============================================================
  TOP 5 PROCESSES BY CPU USAGE
============================================================
   PID    CPU% NAME
  1234    45.6 chrome
  5678    22.1 python
  9012    15.3 java
  3456    10.8 code
  7890     8.2 slack

============================================================
  TOP 5 PROCESSES BY MEMORY USAGE
============================================================
   PID   MEMORY (MB) NAME
  1234      2048.50 MB  chrome
  5678      1024.20 MB  java
  9012       512.10 MB  python
  3456       256.80 MB  code
  7890       128.40 MB  slack
Customisation
To monitor a different disk partition, change the path in psutil.disk_usage('/') (e.g., 'C:\\' on Windows or '/home' on Linux).

Adjust the number of top processes (e.g., :5 to :10) if you want more.

Modify the get_size() function to change the displayed units.

Stretch Goals (optional extras)
You can easily extend the script with additional stats:

OS version – platform.platform() or os.name

System uptime – psutil.boot_time() and current time difference

Load average (Linux/macOS) – psutil.getloadavg()

Logged‑in users – psutil.users()

Failed login attempts – parse /var/log/auth.log or use lastb

Network I/O – psutil.net_io_counters()

Disk I/O – psutil.disk_io_counters()

Example snippet for uptime:

python
import time
boot_time = psutil.boot_time()
seconds = time.time() - boot_time
hours = seconds // 3600
minutes = (seconds % 3600) // 60
print(f"Uptime: {int(hours)}h {int(minutes)}m")
Dependencies
psutil – cross‑platform system monitoring library.

License
This project is open source and available under the MIT License.

