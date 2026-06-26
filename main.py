import json
import sys
import os
import pandas as pd


def main():
    """
    Read a file as JSON, into a DICT, sort by key, emit STDOUT
    """
    # Ensure the user provided the file argument
    if len(sys.argv) < 2:
        print("Error: Please provide a file path.")
        sys.exit(1)

    # Retrieve the file path from the first position
    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("Not a valid file: ", file_path)
        sys.exit(2)

    # Open the file and parse it directly into a dictionary
    with open(file_path, "r") as file:
        file_content = file.read()

    data_dict = json.loads(file_content)
    df = pd.json_normalize(data_dict)
    flat_dict = df.to_dict(orient="records")[0]

    print(flat_dict)


if __name__ == "__main__":
    main()
