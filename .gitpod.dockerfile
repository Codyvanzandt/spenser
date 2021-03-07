FROM gitpod/workspace-full

RUN echo 'run_tests="cd /workspace/spenser && python -m pytest -s -v"' >> $HOME/.bashrc