#!/bin/bash

# Check for NVIDIA GPU
if lspci | grep -iq nvidia; then
    echo "NVIDIA GPU found. Installing with CUDA support."
    poetry install --extras=cuda --with cuda
else
    echo "No NVIDIA GPU found. Installing with CPU support."
    poetry install --extras=cpu
fi