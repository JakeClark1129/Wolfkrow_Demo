
import os
import pyseq
import re
import sys

from wolfkrow import Loader

# Environment variables needed for Wolfkrow to function correctly.
wolfkrow_environment = {
    "PYSEQ_STRICT_PAD": "1",
}

os.environ.update(wolfkrow_environment)

def publish(image_sequence_path, publish_type, publish_name, publish_version):
    import nuke
    context_regex = re.compile(
        r"shows[/\\](?P<show_name>[^/\\]+)[/\\]shots[\//](?P<sequence>\d{3}_\w{3})[/\\](?P<shot>\d{3}_\w{3}_\d{3})[/\\]"
    )
    context_match = re.search(context_regex, image_sequence_path)
    if not context_match:
        print("Error: Could not determine context from the provided path.")
        sys.exit(1)

    show_name = context_match.group("show_name")
    sequence = context_match.group("sequence")
    shot = context_match.group("shot")

    results = {}
    seqs = pyseq.get_sequences(os.path.dirname(image_sequence_path))
    if len(seqs) == 0:
        print("Error: No image sequences found in the provided path.")
        return results

    seq = seqs[0]

    path = seq.format("%D%h%p%t")
    basename = os.path.basename(path).split(".")[0]
    print(f"Publishing file: {basename}")

    extension = os.path.splitext(path)[1][1:]  # Get extension without the dot

    # The base replacements extracted from the file path
    replacements = {}
    replacements["basename"] = basename
    replacements["project_name"] = show_name
    replacements["sequence"] = sequence
    replacements["shot"] = shot
    replacements["publish_type"] = publish_type
    replacements["publish_name"] = publish_name
    replacements["version"] = publish_version
    replacements["render_extension"] = extension

    replacements["start_frame"] = seq.start()
    replacements["start_frame_minusOne"] = seq.start() - 1
    replacements["end_frame"] = seq.end()
    replacements["user"] = "Jacob Clark"
    replacements["input_path"] = path.replace("\\", "/")

    input_render_scene = nuke.root().name().replace("\\", "/")
    replacements["input_render_scene"] = input_render_scene
    replacements["scene_extension"] = "nk"
    
    loader = Loader(
        replacements=replacements,
        temp_dir="$WOLFKROW_DEMO_ROOT/temp/DATE<%Y_%m_%d>/DATE<%H_%M_%S>",
    )
    task_graph = loader.parse_workflow("Demo Publish")

    result = task_graph.execute_local()

    # Summarize the results
    print("\n")
    print("=" * 80)
    print("=" * 80)
    print("=" * 80)
    print("Publish Results for {}:".format(basename))
    for task_name, result in result.items():
        result_str = "Success" if result else "Failed"
        print("    {:<50} - {}".format(task_name, result_str))
    print("=" * 80)
    print("=" * 80)
    print("=" * 80)
    
    return result