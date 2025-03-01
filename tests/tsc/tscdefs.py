from __future__ import print_function
import os
import sys

python = os.environ.get("PYTHON", "python")
sys.path.append(os.path.join(os.environ["SUMO_HOME"], 'tools'))
tscRoot = os.environ.get("TSC_HOME", os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
testServer = os.path.join(tscRoot, os.environ.get("TSC_SERVER", "test_server.tsccfg"))

def get_python_tool(rel_path, config=testServer, templates="test_templates"):
    call = [python, os.path.join(tscRoot, "src", "tapas_sumo_coupling", rel_path)]
    if rel_path == "tsc_main.py":
        call += ["--template-folder", templates, "-b", "13.374361,52.506304,13.474692,52.530199"]
    if config:
        return call + ['-c', config]
    return call
