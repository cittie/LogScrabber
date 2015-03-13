import codecs

logs = []
normal_string = "DEBUG:"
info_string = "INFO:"
warning_string = "WARN:"
error_string = "ERROR:"

with codecs.open('log.txt', encoding = 'utf-8') as file:

    error_switch = False
    for line in file:
        if warning_string in line or error_string in line:
            error_switch = True
        elif normal_string in line or info_string in line:
            error_switch = False

        if error_switch:
            logs += line

output_file = codecs.open('exception_logs.txt', encoding = 'utf-8', mode = "w+")

for log in logs:
    output_file.write(log)

output_file.close()
        
