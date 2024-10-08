if lspci | grep -i nvidia; then
    poetry install --sync --extras=cuda --with cuda
else
    poetry install --sync --extras=cpu
fi
