import tkinter as tk
import psutil
import threading
import time

class CPUMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time CPU Monitor")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.labels = []

        tk.Label(root, text="CPU Usage Monitor", font=("Arial", 16)).pack(pady=10)

        # Create label for each core
        for i in range(psutil.cpu_count()):
            lbl = tk.Label(root, text=f"Core {i}: 0%", font=("Arial", 12))
            lbl.pack()
            self.labels.append(lbl)

        self.total_label = tk.Label(root, text="Total CPU Usage: 0%", font=("Arial", 14, "bold"))
        self.total_label.pack(pady=20)

        self.update_cpu()

    def update_cpu(self):
        per_core = psutil.cpu_percent(percpu=True)
        total = psutil.cpu_percent()

        for i, lbl in enumerate(self.labels):
            lbl.config(text=f"Core {i}: {per_core[i]}%")

        self.total_label.config(text=f"Total CPU Usage: {total}%")

        self.root.after(1000, self.update_cpu)  # repeat every 1s

if __name__ == "__main__":
    root = tk.Tk()
    app = CPUMonitorApp(root)
    root.mainloop()
