import subprocess

completed_process = subprocess.run(["notepad"])
print(completed_process.returncode)