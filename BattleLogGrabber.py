import codecs

logs = []
start_string = "AI.Damage"

with codecs.open('log.txt', encoding = 'utf-8') as file:

    battle_session = False      

    for line in file:
        if start_string in line:
            battle_session = True
        elif "DEBUG:" in line or "INFO:" in line:
            battle_session = False

        if battle_session:
            logs += line

output_file = codecs.open('battle_logs.txt', encoding = 'utf-8', mode = "w+")

for log in logs:
    output_file.write(log)

output_file.close()
        
