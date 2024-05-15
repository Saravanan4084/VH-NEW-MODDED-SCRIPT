import os, _ba, ba
import yaml

# Define function to retrieve server configuration
def get_server_config():
    return _ba.app.server._config


def update_server_config(config):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, '..', 'config.yaml')

    with open(file_path, "w") as f:
        f.write(yaml.dump(config))

# Define function to update only party_name in server configuration
def change_party_name(server_thing, new_party_name):
    try:
        # Retrieve current server configuration
        config = get_server_config()

        # Update only the party name in the configuration
        config[server_thing] = new_party_name

        # Write updated configuration back to config.yaml
        update_server_config(config)

        return True, f"Party name '{new_party_name}' updated successfully."
    except Exception as e:
        return False, f"An error occurred: {e}"
