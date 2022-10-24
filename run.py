from utils.user_agents import get_crawler_information
from utils.io import export_crawlers_list, export_user_agent_ips, export_user_agent_frequency

# INPUTS:
# Originally comes from: https://github.com/monperrus/crawler-user-agents
crawler_info_path = "./input/crawler-user-agents.json"
logs_file_path = "./input/logs.txt"

# OUTPUTS:
known_crawlers_path = "./output/known_crawlers.csv"
user_ua_frequency_path = "./output/user_ua_frequency.csv"
crawler_ua_frequency_path = "./output/crawler_ua_frequency.csv"
user_agent_ips_path = "./output/user_agent_ips.csv"

print("Parsing logs...")
known_crawlers, user_agent_ips, crawler_log_frequency, user_log_frequency = get_crawler_information(
    logs_file_path, crawler_info_path
)

print("Exporting...")
export_crawlers_list(known_crawlers, known_crawlers_path)
export_user_agent_frequency(user_log_frequency, user_ua_frequency_path)
export_user_agent_frequency(crawler_log_frequency, crawler_ua_frequency_path)
export_user_agent_ips(user_agent_ips, user_agent_ips_path)

print("Done!")
