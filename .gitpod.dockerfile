FROM gitpod/workspace-full

RUN echo 'alias run_tests="cd /workspace/spenser && python -m pytest -s -v"' >> $HOME/.bashrc