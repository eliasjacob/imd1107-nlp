FROM mcr.microsoft.com/devcontainers/miniconda:1-3

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
# COPY environment.yml* .devcontainer/noop.txt poetry.lock pyproject.toml create_env.sh /tmp/conda-tmp/
# RUN conda install -n base --override-channels -c conda-forge mamba 'python_abi=*=*cp*' -y # mamba
RUN apt-get update && apt-get install pciutils -y
RUN conda install -y python=3.12
RUN pip install poetry
# RUN /usr/bin/sh /tmp/conda-tmp/create_env.sh && rm -rf /tmp/conda-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
