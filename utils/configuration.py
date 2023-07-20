def load_yaml(path):
    """
    Loads a YAML file from the specified `path`
    returns the data as a Python object.
    """
    import yaml

    with open(path, "r") as file:
        data = yaml.load(file, yaml.SafeLoader)
        return data
