# 1. Read a log file line by line
# 2. Count ERROR, WARNING, and INFO messages
# 3. Display a summary of counts
# 4. Show all ERROR lines for review

import re

# Read log file - why use readlines() instead of loop and read line by line 
def read_logs(log_file):
    try:
        with open(log_file, "r") as f:
            reader = f.readlines()
            reader = [x.rstrip() for x in reader]
            return reader

    except FileNotFoundError:
        print(f"{log_file} not found")
        return []


# Show logs
def show_logs(log_list):
    for log in log_list:
        print(log)


# Count ERROR, WARNING, and INFO messages 
def count_log_levels(log_list):
    try:
        warning_count = 0
        error_count = 0
        info_count = 0
        
        for log in log_list:
            if "WARNING" in log.split():
                warning_count += 1
            elif "ERROR" in log.split():
                error_count += 1
            elif "INFO" in log.split():
                info_count += 1
        
        return warning_count, error_count, info_count

    except Exception as e:
        print(f"an exception has occured {e}")


def print_summary(warning_count, error_count, info_count):    
    
    print(f"Number of Warning Logs: {warning_count}")
    print(f"Number of Error Logs: {error_count}")
    print(f"Number of Info Logs: {info_count}")


def display_errors(log_list):
    try:
        error_list = [log for log in log_list if "ERROR" in log]
        return error_list
    except:
        pass
    

# 1. Extract IP's 
# 2. Count IP's frequency
# 3. Find failed login attempts

# Extract IP's
def extract_ips(log_list):
    try:
        ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        ip_list = []
        for log in log_list:
            ip_list.extend(re.findall(ip_pattern, log))
        return ip_list
    except Exception as e:
        print(f"An error has occured with extracting IPs: {e}")

# Count IPs
def count_ips(ip_list):
    try:
        # Create ip count dictionary
        ip_counts = {}

        # Loop through each ip in list of ips
        for ip in ip_list:
            # If the ip is in the ip_count dictionary then add 1 to its count
            if ip in ip_counts:
                ip_counts[ip] = ip_counts[ip]+1
            else:
                # If not in the ip_count dict then create an entry and make its count 1
                ip_counts[ip] = 1
        
        
        # Return ip_counts dictionary
        return ip_counts
    
    except Exception as e:
        print(f"An error has occured: {e}")


def failed_login_attempts(log_list):
    try:
        user_pattern = r'user: (\w+)'
        failed_login_pattern = r'Failed login'
        ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

        failed_login_list = []

        for log in log_list:
            if failed_login_pattern in log:
                # Get username
                user_match = re.search(user_pattern, log)
                # Get ip
                ip_match = re.search(ip_pattern, log)
                if user_match and ip_match:
                    username = user_match.group(1)
                    ip = ip_match.group(1)

                    # Append as a tuple to the list
                    failed_login_list.append((ip, username))

        return failed_login_list
        

    except Exception as e:
        print(f"An error has occured {e}")

def extract_timestamps(log_list):
    # Sample Timestamp from log: 2025-01-15 10:24:00
    time_pattern = r'^(\d{4})\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01]) ([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])'
    timestamps = []

    
    for log in log_list:
        time_match = re.search(time_pattern, log)
        timestamps.append((time_match.group(0)))
    return timestamps


def main():
    try:
        print("\n")
        print("----- Log analyzer v.01 -----")
        print("-------- made by pp -----")

        while True:         
            
            log_file = "logs_w_ips.log" #input("What log file will we be working with today? \n")
            log_list = read_logs(log_file)
            warning, error, info = count_log_levels(log_list)
            ip_list = extract_ips(log_list)

            ip_counts = count_ips(ip_list)
            
            failed_login_attempts(log_list)

            print("\nMenu\n" \
            "1. Show Logs\n" \
            "2. Display Log Level Counts\n" \
            "3. Display Error Logs \n" \
            "4. Display Most Frequent IPs \n" \
            "5. Display Failed Logon IP Attempts\n" \
            "6. Quit\n")

            x = int(input("What is your choice? "))
            if x == 1:
                print("----- Logs -----")
                show_logs(log_list)
            
            elif x == 2:
                print("----- Log Summary -----")
                print_summary(warning, error, info)
            
            elif x == 3:
                error_list = display_errors(log_list)
                print("----- Error Logs -----")
                for log in error_list:
                    print(log)
            
            elif x == 4:
                print("----- IP Counts -----")
                for ip, count in ip_counts.items():
                    print(f"IP: {ip} | Count: {count}")
            
            elif x == 5:
                failed_login_list = failed_login_attempts(log_list)
                print("----- Failed Logon Attempts -----")
                for x in range(len(failed_login_list)):
                    ip = failed_login_list[x][0]
                    user = failed_login_list[x][1]
                    print(f"{ip} - user : {user}")
        
            elif x == 6:
                print("Good bye!")
                break

    except Exception as e: 
        print(f"Log_analyzer broke. {e}")


# main()

# Create report instead of menu
def report():
    print("----- Log analyzer v.01 -----")
    print("-------- made by pp -----")
    print("")
    log_file = "logs_w_ips.log" #input("What log file will we be working with today? \n")
    log_list = read_logs(log_file)
    
    warning, error, info = count_log_levels(log_list)
    print("----- Log Summary -----")
    print_summary(warning, error, info)
    print("")
    error_list = display_errors(log_list)
    print("----- Error Logs -----")
    for log in error_list:
        print(log)
    print("")

    ip_list = extract_ips(log_list)
    ip_counts = count_ips(ip_list)
    print("----- IP Counts -----")
    for ip, count in ip_counts.items():
        print(f"IP: {ip} | Count: {count}")
    print("")

    failed_login_list = failed_login_attempts(log_list)
    print("----- Failed Logon Attempts -----")
    for x in range(len(failed_login_list)):
        ip = failed_login_list[x][0]
        user = failed_login_list[x][1]
        print(f"{ip} - user : {user}")
    print("")

    timestamps = extract_timestamps(log_list)
    

report()