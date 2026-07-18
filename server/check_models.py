import os, sys, importlib, traceback

for root, dirs, files in os.walk('app/models'):
    for f in files:
        if f.endswith('.py') and f != '__init__.py':
            path = os.path.join(root, f)
            mod_name = path.replace('/', '.').replace('.py', '')
            try:
                importlib.import_module(mod_name)
            except Exception as e:
                print(f"Error in {mod_name}:")
                traceback.print_exc(limit=0)
                print('-'*40)
