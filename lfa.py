import re
from collections import defaultdict, Counter

# Define the log file path
log_file_path = 'access.log'

# Regular expression to parse the log lines
log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d{3}) \S+'
)

# Counters and dictionaries to store data
status_counter = Counter()
requested_pages = Counter()
ip_requests = Counter()

# Function to analyze the log file
def analyze_log_file(log_file):
    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                status = data['status']
                ip = data['ip']
                request = data['request'].split()[1]

                # Count status codes
                status_counter[status] += 1
                
                # Count requested pages
                requested_pages[request] += 1
                
                # Count IP addresses
                ip_requests[ip] += 1

# Function to generate the report
def generate_report():
    print("Web Server Log Analysis Report")
    print("==============================\n")
    
    # Number of 404 errors
    print(f"Number of 404 errors: {status_counter['404']}\n")
    
    # Most requested pages
    print("Most Requested Pages:")
    for page, count in requested_pages.most_common(5):
        print(f"{page}: {count} requests")
    print()
    
    # IP addresses with the most requests
    print("IP Addresses with the Most Requests:")
    for ip, count in ip_reques
