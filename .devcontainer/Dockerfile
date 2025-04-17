FROM python:3.12-bookworm

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=vscode

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \ 
    && apt-get install -y build-essential --no-install-recommends make \
        ca-certificates \
        git \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev \
        pciutils

RUN useradd -ms /bin/bash $USER \
    && mkdir -p /home/$USER/.local/bin \
    && chown -R $USER:$USER /home/$USER \
    && chmod -R u+rw /usr/local && chown -R $USER /usr/local
    
# Python and poetry installation
USER $USER
ARG HOME="/home/$USER"

ENV PATH="${HOME}/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry self add poetry-plugin-shell