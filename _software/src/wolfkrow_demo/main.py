

from wolfkrow.workflow_builder import Loader


def main():
    replacements = {
        "show": "foo",
        "sequence": "bar",
        "shot": "bar_9999",
    }

    loader = Loader(
        replacements=replacements,
    )
    task_graph = loader.parse_workflow("workflow_name")