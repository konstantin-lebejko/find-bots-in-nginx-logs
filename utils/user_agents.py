import re
import json

from utils.io import read_logs_line_by_line, read_file
from utils.ips import pull_ip


def pull_user_agent(string):
    user_agent_re = re.search('"(.*)"', string)
    return user_agent_re.group(1)


def is_user_agent_crawler(log_user_agent, crawler_information):
    for crawler in crawler_information:
        if log_user_agent in crawler['instances']:
            return (True, crawler)
    return (False, None)


def is_crawler_in_crawler_list(crawler, crawler_user_agent, crawler_list):
    for known_crawler in crawler_list:
        is_crawler_pattern_matching = crawler['pattern'] == known_crawler['pattern']
        is_crawler_ua_matching = crawler_user_agent == known_crawler['user_agent']

        if is_crawler_pattern_matching and is_crawler_ua_matching:
            return True
    return False


def get_crawler_information(logs_file_path, crawler_info_path):
    crawler_info = json.loads(read_file(crawler_info_path))

    # List of known crawlers (with crawler information)
    known_crawlers = []
    # List of IP addresses per user agent
    user_agent_ips = {}
    # Crawler log frequency
    crawler_log_frequency = {}
    # User log frequency
    user_log_frequency = {}

    for log_line in read_logs_line_by_line(logs_file_path):
        user_agent = pull_user_agent(log_line)
        ip = pull_ip(log_line)

        # If user agent is detected as a crawler - add it to know crawler list
        # is_crawler - boolean flag, what_crawler - crawler information (if flag is True)
        is_crawler, what_crawler = is_user_agent_crawler(
            user_agent, crawler_info
        )
        if is_crawler:
            if not is_crawler_in_crawler_list(what_crawler, user_agent, known_crawlers):
                pattern = what_crawler.get("pattern")
                url = what_crawler.get('url')

                known_crawlers.append({
                    'pattern': pattern,
                    'url': url,
                    'user_agent': user_agent
                })

            # If user agent is detected as a crawler increase the frequency by one
            if user_agent in crawler_log_frequency:
                crawler_log_frequency[user_agent] += 1
            else:
                crawler_log_frequency[user_agent] = 1
        else:
            # If user agent is not a crawler increase the frequency by one
            if user_agent in user_log_frequency:
                user_log_frequency[user_agent] += 1
            else:
                user_log_frequency[user_agent] = 1

        # Add log IP to user agent IP list
        if user_agent in user_agent_ips and ip not in user_agent_ips[user_agent]:
            user_agent_ips[user_agent].append(ip)
        # If user agent is not in the list - add it
        else:
            user_agent_ips[user_agent] = [ip]

    return (known_crawlers, user_agent_ips, crawler_log_frequency, user_log_frequency)
