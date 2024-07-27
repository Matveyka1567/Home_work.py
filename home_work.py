    # ДЗ № 1
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = ['145_934_462', '331_002_651', '80_345_321', '67_886_011',
'65_273_511', '1_380_004_385']
print(f"{capitals[0]} is the capital of {countries[0]}, population equal {population[0].replace('_', '')}")
print(f"{capitals[1]} is the capital of {countries[1]}, population equal {population[1].replace('_', '')}")
print(f"{capitals[2]} is the capital of {countries[2]}, population equal {population[2].replace('_', '')}")


                    # ДЗ № 2
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate'] 
    return any(map(lambda x: x in command, ignore))
