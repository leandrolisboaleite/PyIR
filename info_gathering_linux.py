import subprocess

def run_commands(commands):
    for command in commands:
        print("Running command: ", command)
        try:
            output, error = subprocess.Popen(
                command.split(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            ).communicate()
            output_str = output.decode()
            with open("results.txt", "a") as file:
                file.write("\n\n\n")
                file.write("Command: " + command + "\n")
                file.write("Output:\n")
                file.write(output_str)
        except Exception as e:
            print("Error running command: ", e)

commands = [
    "cat /etc/passwd",
    "cat /etc/group",
    "cat /etc/sudoers",
    "lastlog",
    "cat /var/log/auth.log",
    "uptime",
    "cat /proc/meminfo",
    "ps aux",
    "cat /etc/resolv.conf",
    "cat /etc/hosts",
    "iptables -L -v -n",
    "find / -type f -size +512k -exec ls -lh {}/;",
    "find / -mtime -1 -ls",
    "ip a",
    "last -F -x -i",
    "cat /var/log/messages",
    "cat /var/log/auth.log",
    "netstat -nap",
    "arp -a",
    "echo $PATH"
]

run_commands(commands)
