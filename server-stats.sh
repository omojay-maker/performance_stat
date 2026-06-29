#!/bin/bash
echo "========================================"
echo "       SERVER PERFORMANCE STATS"
echo "========================================"
echo

# 1. Total CPU Usage
echo "--- CPU Usage ---"
# Extract idle percentage from `top` and compute usage.
cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}' | cut -d. -f1)
if [ -z "$cpu_idle" ]; then
    # Fallback: try using mpstat if available
    cpu_idle=$(mpstat 1 1 | awk '/Average/ {print $NF}')
fi
if [ -n "$cpu_idle" ]; then
    cpu_usage=$((100 - cpu_idle))
    echo "Total CPU Usage: $cpu_usage%"
else
    echo "Total CPU Usage: Unable to determine"
fi
echo

# 2. Memory Usage
echo "--- Memory Usage ---"
mem_info=$(free -m | grep Mem)
total_mem=$(echo $mem_info | awk '{print $2}')
used_mem=$(echo $mem_info | awk '{print $3}')
free_mem=$(echo $mem_info | awk '{print $4}')
mem_percent=$((used_mem * 100 / total_mem))
echo "Total Memory: ${total_mem}MiB"
echo "Used Memory:  ${used_mem}MiB"
echo "Free Memory:  ${free_mem}MiB"
echo "Usage:        ${mem_percent}%"
echo

# 3. Disk Usage (root filesystem)
echo "--- Disk Usage (/) ---"
disk_info=$(df -h / | awk 'NR==2')
total_disk=$(echo $disk_info | awk '{print $2}')
used_disk=$(echo $disk_info | awk '{print $3}')
free_disk=$(echo $disk_info | awk '{print $4}')
disk_percent=$(echo $disk_info | awk '{print $5}' | tr -d '%')
echo "Total Disk:   ${total_disk}"
echo "Used Disk:    ${used_disk}"
echo "Free Disk:    ${free_disk}"
echo "Usage:        ${disk_percent}%"
echo

# 4. Top 5 Processes by CPU Usage
echo "--- Top 5 Processes by CPU Usage ---"
ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6 | awk 'NR==1 {print "PID\tCOMMAND\t\t%CPU"} NR>1 {printf "%s\t%s\t\t%s\n", $1, $2, $3}'
echo

echo "========================================"