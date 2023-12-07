def fetch_widget_by_name_from_root(root, widget_name):
    for child in root.winfo_children():
        if child._name == widget_name:
            return child
    return