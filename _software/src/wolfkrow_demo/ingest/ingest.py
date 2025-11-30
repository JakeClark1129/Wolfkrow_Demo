


import argparse
import os
import pyseq
import re
import sys

from wolfkrow import Loader

wolfkrow_environment = {
    "PYSEQ_STRICT_PAD": "1",
}
def parse_args():
    parser = argparse.ArgumentParser(description="Ingest media into Wolfkrow Demo project.")
    
    parser.add_argument(
        "path",
        help="The root path of the media to ingest.",
    )

    return parser.parse_args()

def main():
    args = parse_args()
    root_path = args.path

    show_regex = re.compile(r"shows[/\\](?P<show_name>[^/\\]+)")
    show_match = re.search(show_regex, root_path)
    if not show_match:
        print("Error: Could not determine show name from the provided path.")
        sys.exit(1)

    show_name = show_match.group("show_name")

    client_plate_regex = re.compile(
        r"(?P<shot>(?P<sequence>\d{3}_\w{3})_\d{3})_(?P<publish_name>\w{2}\d{2})_v(?P<version>\d{2})[/\\\\](?P<resolution>(?P<width>\d{3,5})x(?P<height>\d{3,5}))[\\\\/].*[.](?P<extension>\w+)"
    )

    results = {}
    # Walk over the files in the root_path and ingest them one by one
    for root, dirs, files in os.walk(root_path):
        sequences = pyseq.get_sequences(root)
        for sequence in sequences:
            
            if len(sequence) == 1:
                continue

            print(f"Ingesting sequence: {sequence}")
            path = sequence.format("%D%h%p%t")
            match = re.search(client_plate_regex, path)

            if not match:
                continue

            # The base replacements extracted from the file path
            replacements = match.groupdict()
            replacements["project_name"] = show_name
            replacements["start_frame"] = sequence.start()
            replacements["start_frame_minusOne"] = sequence.start() - 1
            replacements["end_frame"] = sequence.end()
            replacements["user"] = "Jacob Clark"
            replacements["input_path"] = path.replace("\\", "/")

            basename = os.path.basename(path).split(".")[0]
            replacements["basename"] = basename

            grade_path = root + f"/../../{basename}.ccc"
            grade_path = os.path.normpath(grade_path)
            replacements["input_grade_path"] = grade_path.replace("\\", "/")


            loader = Loader(
                replacements=replacements,
                temp_dir="$WOLFKROW_DEMO_ROOT/temp/DATE<%Y_%m_%d>/DATE<%H_%M_%S>",
            )
            task_graph = loader.parse_workflow("Demo Ingest")
            output = task_graph.execute_local()
            results[basename] = output

    # Summarize the results
    print("\n")
    print("=" * 80)
    print("=" * 80)
    print("=" * 80)
    for basename, result in results.items():
        print("Ingest Results for {}:".format(basename))
        for task_name, result in result.items():
            result_str = "Success" if result else "Failed"
            print("    {:<50} - {}".format(task_name, result_str))
        print("=" * 80)
    print("=" * 80)
    print("=" * 80)

if __name__ == "__main__":
    main()