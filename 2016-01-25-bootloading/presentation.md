Preparation
===

Start gotty server

    # start gotty with tmux
    ./gotty -p 8080 tmux new -A -s gotty

    # on another terminal, attach
    tmux new -A -s gotty

Start python http.server

    python3 http.server 8000

Start qemu server

    ./run-server

Confirm that all of the above work (SSH, load in browser)

Presentation
===

BIOS demo
---

MBR magic

    sudo tail -c +511 /dev/sda | head -c 2 | hexdump -C

Find GRUB

    sudo head -c 512 /dev/sda | strings

Show first partiton offset

    sudo parted -l

UEFI demo
---

Show uefi existence

    ls /sys/firmware/efi

Show uefi loader

    lsblk
    cd /boot/efi
    tree

Show boot entries

    sudo efibootmgr -v

Remove Ubuntu and go to shell

    sudo efibootmgr -B -b 0000
    sudo efibootmgr -v
    sudo reboot

Remake Ubuntu

    sudo efibootmgr -c -p 1 -d /dev/vda -L Ubuntu -l "\efi\ubuntu\grubx64.efi"
    sudo reboot
