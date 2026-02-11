import psutil

processes = []

for proc in psutil.process_iter(['pid', 'name']):
    pid = proc.info['pid']
    name = proc.info['name']
    rss = proc.memory_info().rss
    row = (pid, name, rss)
    processes.append(row)

top_10 = sorted(processes, key=lambda x: x[2], reverse=True)[:10]
print("\nTop 10 Processes By Memory Usage:")
print("-----------------------------")
print("PID      NAME       MEMORY (MB)")
for pid, name, rss in top_10:
    print(f"{pid} {name} {rss / (1024*1024):.1f} MB")
print("-----------------------------")