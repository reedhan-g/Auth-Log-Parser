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

    # Session opened
     if "session opened" in line:

        match = re.search(
            r"session opened for user (\S+)",
            line
        )

        return {
            "timestamp": timestamp,
            "source_ip": None,
            "username": match.group(1) if match else None,
            "event_type": "session_open",
            "status": None,
            "pid": pid,
            "port": None
        }
    
     # Session closed
     if "session closed" in line:

        match = re.search(
            r"session closed for user (\S+)",
            line
        )

        return {
            "timestamp": timestamp,
            "source_ip": None,
            "username": match.group(1) if match else None,
            "event_type": "session_close",
            "status": None,
            "pid": pid,
            "port": None
        }
     return None
def parse_structured_event(data):
   return {
        "timestamp": data.get("timestamp"),
        "source_ip": data.get("source_ip"),
        "username": data.get("username"),
        "event_type": data.get("event_type"),
        "status": data.get("status"),
        "pid": data.get("pid"),
        "port": data.get("port")
    }