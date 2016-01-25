Preparation
===

* start gotty server

    # start a tmux session under gotty
    gotty tmux new -A -s gotty

    # on another terminal
    tmux new -A -s gotty

    # to control tmux

* start python http.server

    python3 http.server 8000

* start qemu server

    ./run-server

Confirm that all of the above work (SSH, load in browser)

Presentation
===

BIOS demo

    # MBR magic
    sudo tail -c +511 /dev/sda | head -c 2 | hexdump -C

    # find GRUB
    sudo head -c 512 /dev/sda | strings

    # show first partiton offset
    sudo parted -l

UEFI demo

    # show uefi existence
    ls /sys/firmware/efi

    # show uefi loader
    lsblk
    cd /boot/efi
    tree

    # show boot entries
    sudo efibootmgr -v

    # remove Ubuntu and go to shell
    sudo efibootmgr -B -b 0000
    sudo efibootmgr -v
    sudo reboot

    # remake Ubuntu
    sudo efibootmgr -c -p 1 -d /dev/vda -L Ubuntu -l "\efi\ubuntu\grubx64.efi"
    sudo reboot
