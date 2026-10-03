import re
def parse(lines):
    line=lines.strip() 
    if line=="":
        return None
    parts = line.split()
    if len(parts) < 3:
        return None
    timestamp = " ".join(parts[:3])
    pid_match = re.search(r"sshd\[(\d+)\]", line)
    pid = int(pid_match.group(1)) if pid_match else None
    
      
