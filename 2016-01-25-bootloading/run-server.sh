#!/bin/bash

OPT="$OPT -enable-kvm -m 1024"

# UEFI
OPT="$OPT -drive if=pflash,format=raw,file=ubuntu.flash"

# disk
OPT="$OPT -drive id=disk0,file=ubuntu.disk,format=raw,index=0,media=disk,if=none \
          -device virtio-blk-pci,drive=disk0,bootindex=0"

# networking
OPT="$OPT -netdev id=net0,type=user \
          -device virtio-net-pci,netdev=net0,romfile="

# VGA
OPT="$OPT -device qxl-vga"

# SSH
#OPT="$OPT -redir tcp:8002-:22"

qemu-system-x86_64 $OPT
