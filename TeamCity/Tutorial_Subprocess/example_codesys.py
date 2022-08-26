import subprocess

completed_process = subprocess.run(["powershell", "start codesys"], check=True)
print(completed_process.returncode)