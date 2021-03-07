FROM gitpod/workspace-full

RUN alias run_tests="cd /workspace/spenser && python -m pytest -s -v"