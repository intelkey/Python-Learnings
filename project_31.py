'''31. Log Message Analyzer (A2 – string find)
    Detect errors in log messages.'''

log_mess = input("Enter your log message: " ).lower()
if_error = log_mess.find("error")

if if_error == -1:
    print("Error is not present in log message.")
else:
    print("Error is present in log message.")
