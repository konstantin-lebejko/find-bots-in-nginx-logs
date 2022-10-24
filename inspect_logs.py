from utils.inspect import inspect_logs

# INPUTS:
logs_file_path = "./input/logs.txt"

string_date = "10/Oct/2022"
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
page = "/careers/job-4529006004.delivery-director/"

inspect_logs(logs_file_path, string_date, user_agent, page)
