import importlib.util

def import_class_from_file(file_path, class_name):
    spec = importlib.util.spec_from_file_location("module_name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    imported_class = getattr(module, class_name)
    return imported_class
