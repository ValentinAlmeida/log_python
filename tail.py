from sh import tail
# runs forever
for line in tail("-f", "/var/log/some_log_file.log", _iter=True):
    print(line)