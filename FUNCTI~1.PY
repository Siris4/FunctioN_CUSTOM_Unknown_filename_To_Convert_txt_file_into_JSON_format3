import json
import os


def convert_txt_to_json():
    # prompt the user for the filename:
    input_file_name = input("Enter the filename (+.txt) of the text file: ")

    # construct the output file name by changing the extension to .json:
    base_name = os.path.splitext(input_file_name)[0]
    output_file_name = f"{base_name}.json"

    try:
        # read the entire string from the text file:
        with open(input_file_name, 'r') as file:
            content = file.read().strip()

        # convert the string to a json format (as a value associated with a key):
        data = {"content": content}

        # save the json object to a file with the same base filename:
        with open(output_file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Conversion complete. The JSON file has been saved as: {output_file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")  # report any errors encountered during the process:


# run the function:
convert_txt_to_json()
