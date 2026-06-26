# x_Recon 🔍

`x_Recon` is a high-performance, asynchronous, multi-threaded network scanner and asset discovery tool written completely from scratch in Python. By utilizing Python's native `concurrent.futures.ThreadPoolExecutor`, it allows users to scan entire network blocks dynamically while keeping resource consumption safe and lightweight.

---

## 🚀 Features

* **Dynamic Concurrency Control:** Dictate the speed of your scans by specifying thread execution limits at runtime.
* **Asynchronous TCP Scanning:** Utilizes non-blocking socket loops to quickly check port availability.
* **Live Banner Grabbing:** Interrogates active ports to capture service introduction responses and server configuration identification strings.
* **Asset & Threat Advisory Engine:** Dynamically aggregates discovered ports across networks and references them against standard exploit-vector matrices to provide a summary threat advisory at the end of execution.
* **Optimized Thread Lifetimes:** Scans networks on a host-by-host concurrent basis to ensure stable socket descriptor handling and prevent memory leaks.

---

## 🛠️ Installation & Setup

No third-party packages or complex environments are required. This script runs entirely on Python 3 standard modules (`socket`, `ipaddress`, `time`, `concurrent.futures`).

1. **Clone the repository:**
   ```bash
      git clone [https://github.com/inecho7/x_Recon.git](https://github.com/inecho7/x_Recon.git)
         cd x_Recon
         