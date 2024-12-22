import datetime

import time

end_time = datetime.datetime("date")
site_block = ["website_name"]
host_path = "host_path"
redirect = "host_server_no"

while True:
    if datetime.datetime.now()<end_time:
        print("Start block")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(website + "\n")
                else:
                    pass

    else:
        with open(host_path,"r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)

            host_file.truncate()
            
        time.sleep(5)      

