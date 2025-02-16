import yaml

data = {
    "name": "Example",
    "numbers": [1, 2, 3.14],
    "enabled": True,
    "nested": {"key1": "value1", "key2": [True, False]},
}

yaml_output = yaml.safe_dump(data, default_flow_style=False)
print(yaml_output)

loaded_data = yaml.safe_load(yaml_output)
print(loaded_data)

print(loaded_data["numbers"])


try:
    with open("config.yaml", "r") as file:
        data = yaml.safe_load(file)
        print(data)
except FileNotFoundError:
    print("Error: config.yaml not found")
except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}")
