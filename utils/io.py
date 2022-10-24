delimiter = '>>>>'


def read_logs_line_by_line(path):
    for line in open(path, 'r'):
        yield line


def read_file(path):
    return open(path, 'r').read()


def export_user_agent_frequency(user_agent_frequency, path):
    with open(path, 'w') as f:
        for user_agent, frequency in user_agent_frequency.items():
            f.write(f'{user_agent} {delimiter} {frequency}\n')


def export_crawlers_list(crawlers, path):
    with open(path, 'w') as f:
        for crawler in crawlers:
            pattern = crawler['pattern']
            url = crawler['url']
            user_agent = crawler['user_agent']

            f.write(f'{pattern} {delimiter} {url} {delimiter} {user_agent}\n')


def export_user_agent_ips(user_agent_ips, path):
    with open(path, 'w') as f:
        for user_agent, ips in user_agent_ips.items():
            ips_as_sting = ', '.join(ips)
            f.write(f'{user_agent} {delimiter} {ips_as_sting}\n')
