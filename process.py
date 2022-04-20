log_file = open("um-server-01.txt")
# This line opens a file that you want to have your code run over

def sales_reports(log_file):
    # This line defines a function the takes in the external file as a parameter
    for line in log_file:
        # This line starts a for loop
        line = line.rstrip()
        # This line defines "line" to the method rstrip invoked
        day = line[0:3]
        # This line defines "day" as the method rstrip and passes it the characters we want removed
        if day == "Tue":
            # This line is an if statment that checks if "Tue" is in the file
            print(line)
            # This line prints the response of the if statement to the terminal


sales_reports(log_file)
# This line runs the function pasing in the opened file
