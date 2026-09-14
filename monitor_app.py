"""CLI system monitor and localhost port scanner.

This is a small educational utility. It displays basic disk/memory metrics and
scans TCP ports 1-1024 on localhost in the background.
"""

from __future__ import annotations

import os
import shutil
import socket
import sys
import threading
import time
from datetime import datetime


class SystemMonitor:
    """Collect local metrics and run a localhost TCP port scan."""

    def __init__(self) -> None:
        self.is_running = True
        self.scan_results: list[tuple[int, str]] = []
        self.scan_progress = 0.0
        self.current_metrics: dict[str, float | str] = {}

    def get_system_metrics(self) -> dict[str, float | str]:
        """Return basic CPU, memory, and disk metrics."""
        metrics: dict[str, float | str] = {}

        if hasattr(os, "getloadavg"):
            metrics["cpu_load"] = round(os.getloadavg()[0] * 10, 1)
        else:
            metrics["cpu_load"] = "N/A"

        if sys.platform.startswith("linux"):
            with open("/proc/meminfo", encoding="utf-8") as meminfo:
                lines = meminfo.readlines()
            mem_total = int(lines[0].split()[1])
            mem_available = int(lines[2].split()[1])
            metrics["mem_percent"] = round(
                ((mem_total - mem_available) / mem_total) * 100, 1
            )
        else:
            metrics["mem_percent"] = "N/A"

        total, used, free = shutil.disk_usage(os.path.abspath(os.sep))
        metrics["disk_percent"] = round((used / total) * 100, 1)
        metrics["disk_free_gb"] = round(free / (2**30), 2)
        self.current_metrics = metrics
        return metrics

    def scan_single_port(self, target_host: str, port: int) -> None:
        """Check whether a TCP port is accepting connections."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.3)
                if sock.connect_ex((target_host, port)) == 0:
                    try:
                        service = socket.getservbyport(port)
                    except OSError:
                        service = "Unknown Service"
                    self.scan_results.append((port, service))
        except OSError:
            pass

    def network_scanner_worker(self, target_host: str, start_port: int, end_port: int) -> None:
        """Scan a TCP port range using small batches of threads."""
        self.scan_results.clear()
        total_ports = end_port - start_port + 1

        for batch_start in range(start_port, end_port + 1, 50):
            if not self.is_running:
                break
            batch_end = min(batch_start + 49, end_port)
            threads = [
                threading.Thread(target=self.scan_single_port, args=(target_host, port))
                for port in range(batch_start, batch_end + 1)
            ]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()
            self.scan_progress = round(
                ((batch_end - start_port + 1) / total_ports) * 100, 1
            )

        self.scan_progress = 100.0

    def start_scan(self, host: str, start_port: int, end_port: int) -> None:
        """Start the network scan in a daemon thread."""
        scan_thread = threading.Thread(
            target=self.network_scanner_worker,
            args=(host, start_port, end_port),
            daemon=True,
        )
        scan_thread.start()

    def render_terminal_ui(self) -> None:
        """Render the current dashboard state in the terminal."""
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 60)
        print(
            " SYSTEM MONITOR & LOCALHOST PORT SCANNER | "
            f"{datetime.now():%H:%M:%S}"
        )
        print("=" * 60)

        metrics = self.get_system_metrics()
        print("\n[+] SYSTEM METRICS")
        print(f"  ├─ CPU Load Approx : {metrics['cpu_load']}%")
        print(f"  ├─ Memory Usage    : {metrics['mem_percent']}%")
        print(
            f"  └─ Disk Usage      : {metrics['disk_percent']}% "
            f"({metrics['disk_free_gb']} GB free)"
        )

        print("\n[+] LOCALHOST SCANNER (127.0.0.1:1-1024)")
        print(f"  ├─ Scan Progress   : {self.scan_progress}%")
        print("  └─ Open Ports Found:")
        if not self.scan_results:
            print("       None detected yet or scanning...")
        else:
            for port, service in sorted(self.scan_results)[:10]:
                print(f"       • Port {port:<5} -> {service}")

        print("\n" + "=" * 60)
        print(" Press Ctrl+C to terminate safely.")

    def run_loop(self) -> None:
        """Run the monitor dashboard until interrupted."""
        self.start_scan("127.0.0.1", 1, 1024)
        try:
            while self.is_running:
                self.render_terminal_ui()
                time.sleep(1.5)
        except KeyboardInterrupt:
            self.is_running = False
            print("\n[-] Shutting down gracefully...")


if __name__ == "__main__":
    SystemMonitor().run_loop()
