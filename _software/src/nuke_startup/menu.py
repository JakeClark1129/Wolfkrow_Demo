
import nuke

menu = nuke.menu("Nuke")
wolfkrow_demo_menu = menu.addMenu("Publish")

from wolfkrow_demo.publish.nuke import publish_selected_write_nodes
wolfkrow_demo_menu.addCommand("Publish Selected Write Nodes", "publish_selected_write_nodes()")
