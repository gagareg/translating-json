import json


path = "input.json"
with open(path, "r") as json_data:
    parsed_data = json.load((json_data))

result_list = []
for i in parsed_data:
    result_list.append({
        "fullname": "{}/{}".format(i['jobname'], i['env']),
        "params": {
            "Action": "$ACTION$",
            "Service": i['service'],
            "Services version": i['version']
        },
    })

end_path = "output.json"
with open(end_path, "w", encoding="utf-8") as file:
    json.dump(result_list, file)

