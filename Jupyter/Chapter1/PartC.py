import re


def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.readlines()

    log_list = []
    for line in logdata:
        pattern = r'^(\d+\.\d+\.\d+\.\d+) - (.+) \[(.*?)\] "(.*?)"' # is used to match and capture specific parts of each log line
        match = re.search(pattern, line)

        if match:
            host = match.group(1)
            user_name = match.group(2)
            time = match.group(3)
            request = match.group(4)

            log_dict = {
                "host": host,
                "user_name": user_name,
                "time": time,
                "request": request
            }

            log_list.append(log_dict)

    return log_list

assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
#print(len(logs()))