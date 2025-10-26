# 1. Read a log file line by line
# 2. Count ERROR, WARNING, and INFO messages
# 3. Display a summary of counts
# 4. Show all ERROR lines for review

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
    
    
    print("-----Log Summary-----")
    print(f"Number of Warning Logs: {warning_count}")
    print(f"Number of Error Logs: {error_count}")
    print(f"Number of Info Logs: {info_count}")


def display_errors(log_list):
    try:
        pass
    except:
        pass


log_file = read_logs("system.log")

def main():
    try:
        print("\n")
        print("-----Log analyzer v.01-----")
        print("--------made by pp-----")

        while True:
            
            
            log_file = "system.log" #input("What log file will we be working with today? \n")
            log_list = read_logs(log_file)
            warning, error, info = count_log_levels(log_list)

            print("\nMenu\n" \
            "1. Show Logs\n" \
            "2. Display Log Level Counts\n" \
            "3. Quit\n")

            x = int(input("What is your choice? "))
            if x == 1:
                show_logs(log_list)
            elif x == 2:
                print_summary(warning, error, info)
            elif x ==3:
                print("Good bye!")
                break

    except Exception as e: 
        print("Log_analyzer broke.")


main()