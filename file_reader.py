def read_contents(file_name):
    fh = open(file_name, "r")

    content = fh.read()

    fh.close()

    return content

def get_json(file_name):
    import json

    contents = read_contents(file_name)
    return json.loads(contents)
