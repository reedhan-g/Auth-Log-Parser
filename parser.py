import re
def parse_text_line(line):
     line = line.strip()
     if not line:
        return None
     parts = line.split()
     if len(parts) < 3:
        return None
     timestamp = " ".join(parts[:3])

     #PID
     pid_match = re.search(r"sshd\[(\d+)\]", line)
     pid = int(pid_match.group(1))
     if pid_match else None

     #For failed authentication
     match = re.search(
        r"Failed password for (?:invalid user )?(\S+) "
        r"from ([\d.]+) port (\d+)",
        line)
     if match:
        return {
            "timestamp": timestamp,
            "source_ip": match.group(2),
            "username": match.group(1),
            "event_type": "ssh_authentication",
            "status": "failure",
            "pid": pid,
            "port": int(match.group(3))
        }

     #Successful SSH
     match = re.search(
        r"Accepted \S+ for (\S+) "
        r"from ([\d.]+) port (\d+)",
        line
    )
     if match:
        return {
            "timestamp": timestamp,
            "source_ip": match.group(2),
            "username": match.group(1),
            "event_type": "ssh_authentication",
            "status": "success",
            "pid": pid,
            "port": int(match.group(3))
        }