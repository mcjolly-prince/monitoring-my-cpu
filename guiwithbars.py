import tkinter as tk
from tkinter import ttk
import psutil

class CPUMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time CPU Monitor")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.num_cores = psutil.cpu_count(logical=True)


        tk.Label(root, text="CPU Usage Monitor", font=("Arial", 16)).pack(pady=10)

        self.core_bars = []

        core_frame = tk.Frame(root)
        core_frame.pack(pady=10)

        for i in range(self.num_cores):
            row_frame = tk.Frame(core_frame)
            row_frame.pack(fill="x", pady=3)

            label = tk.Label(row_frame, text=f"Core {i}", width=10, anchor='w', font=("Arial", 10))
            label.pack(side="left", padx=5)

            percent_label = tk.Label(row_frame, text="0%", width=5, anchor="e", font=("Arial", 10))
            percent_label.pack(side="left")

            bar = ttk.Progressbar(row_frame, orient='horizontal', length=300, mode='determinate', maximum=100)
            bar.pack(side="left", padx=5)

            self.core_bars.append((bar, percent_label))

        # Total CPU usage bar
        tk.Label(root, text="Total CPU Usage", font=("Arial", 12)).pack(pady=(20, 0))
        self.total_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate', maximum=100)
        self.total_bar.pack(pady=5)

        self.total_label = tk.Label(root, text="0%", font=("Arial", 12, "bold"))
        self.total_label.pack()

        self.update_cpu()

    def update_cpu(self):
        per_core = psutil.cpu_percent(percpu=True)
        total = psutil.cpu_percent()

        for i, (bar, percent_label) in enumerate(self.core_bars):
            usage = per_core[i]
            bar['value'] = usage
            percent_label.config(text=f"{usage:.1f}%")

        self.total_bar['value'] = total
        self.total_label.config(text=f"{total:.1f}%")

        self.root.after(1000, self.update_cpu)

if __name__ == "__main__":
    root = tk.Tk()
    app = CPUMonitorApp(root)
    root.mainloop()
