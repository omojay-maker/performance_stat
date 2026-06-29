#!/usr/bin/env python3
import psutil
import time

def get_size(bytes):
    """Convert bytes to human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

def print_header(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def main():
    #CPU
    print_header("CPU USAGE")
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Total CPU Usage: {cpu_percent}%")

    # MEMORY
    print_header("MEMORY USAGE")
    mem = psutil.virtual_memory()
    print(f"Total:     {get_size(mem.total)}")
    print(f"Available: {get_size(mem.available)}")
    print(f"Used:      {get_size(mem.used)}")
    print(f"Percentage: {mem.percent}%")

    #  DISK (root partition) 
    print_header("DISK USAGE (/)")
    disk = psutil.disk_usage('/')
    print(f"Total:     {get_size(disk.total)}")
    print(f"Used:      {get_size(disk.used)}")
    print(f"Free:      {get_size(disk.free)}")
    print(f"Percentage: {disk.percent}%")

    #  Top 5 processes by CPU
    print_header("TOP 5 PROCESSES BY CPU USAGE")
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    processes.sort(key=lambda p: p['cpu_percent'] or 0, reverse=True)
    top_cpu = processes[:5]
    print(f"{'PID':>6} {'CPU%':>8} {'NAME'}")
    for p in top_cpu:
        print(f"{p['pid']:>6} {p['cpu_percent']:>8.1f} {p['name']}")

    print_header("TOP 5 PROCESSES BY MEMORY USAGE")
    processes_mem = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            mem_info = proc.info['memory_info']
            if mem_info is not None:
                rss = mem_info.rss  
                processes_mem.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'memory': rss
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    processes_mem.sort(key=lambda p: p['memory'], reverse=True)
    top_mem = processes_mem[:5]
    print(f"{'PID':>6} {'MEMORY (MB)':>12} {'NAME'}")
    for p in top_mem:
        mem_mb = p['memory'] / (1024 * 1024)
        print(f"{p['pid']:>6} {mem_mb:>12.2f} MB  {p['name']}")

if __name__ == "__main__":
    main()