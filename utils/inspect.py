from utils.io import read_logs_line_by_line


def inspect_logs(logs_file_path, string_date, user_agent, page):
    for log_line in read_logs_line_by_line(logs_file_path):
        if string_date in log_line and user_agent in log_line and page in log_line:
            print(log_line)
