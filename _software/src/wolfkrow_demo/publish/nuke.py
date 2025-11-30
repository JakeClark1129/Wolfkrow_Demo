
import nuke

from wolfkrow_demo.publish.publish import publish

def publish_selected_write_nodes():
    selected_nodes = nuke.selectedNodes("Write")
    if not selected_nodes:
        nuke.message("No Write nodes selected for publishing.")
        return


    print(str(selected_nodes))
    for write_node in selected_nodes:
        
        print(str(write_node))
        file_path = write_node['file'].getValue()
        publish_type = "comp"  # Example publish type
        publish_name = write_node.name()
        publish_version = 1  # Example version, this could be extracted or incremented as needed

        print(f"Publishing {file_path} as {publish_name} v{publish_version}")

        # Call the publish function from publish.py
        results = publish(file_path, publish_type, publish_name, publish_version)
        if not results:
            nuke.message(f"Publishing failed for {file_path}")
            return

    nuke.message("Publishing of selected Write nodes completed.")