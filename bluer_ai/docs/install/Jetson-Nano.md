# install: Jetson-Nano

1. Download the image:

    - `2GB, no tf:` [Jetson Nano Developer Kit w/ JetPack 4.6](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#write)
    - `2GB, tf 1.x:` [Jetson Nano Developer Kit w/ JetPack 4.4](https://developer.nvidia.com/jetson-nano-2gb-jp441-sd-card-image)
    - `4GB, tf 1.x:` [Jetson Nano Developer Kit w/ JetPack 4.3](https://developer.nvidia.com/jetpack-43-archive)
    - `4GB, tf 2.x`: [Jetson Nano Developer Kit w/ JetPack 4.6](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#write)

1. `4 GB/speedup for 2 GB:` Connect a network cable to the ethernet connection on the motherboard or connect one of the USB-A ports on the motherboard to a smartphone and enable USB-tethering on the phone.

1. Follow [these instructions](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-2gb-devkit#write) w/ the image that you downloaded above. Boot the motherboard.

1. Set username to `abcli` and password to `abcli2025` and Select `Log in automatically`.

1. `GNOME:` Go to `System Settings` > `Brightness & Lock`, set `Turn Screen off when inactive for` to `Never`, turn `Lock` off, disable `Require password when waking from suspend`.

1. `LXDE:` Select `Preferances` > `Screensaver` - change `Display Modes` -> `Mode` to `Disable Screen Saver`.

1. Insert a [seed usb key](seed), open a terminal, and run `bash /media/abcli/SEED/abcli/jetson.sh`.

1. Type in `sudo visudo` and add `abcli ALL=(ALL) NOPASSWD: ALL` to the end of the file.

1. `4 GB:` Attach a TP-Link AC600 Mini USB WiFi Adapter to the motherboard, detach the USB/ethernet cable from the motherboard, and reboot.

---

2 GB motherboards start with the `GNOME` desktop environment, and change to `LXDE` after the Ubuntu configuration is complete. 4 GB motherboards start with `GNOME` and stay with `GNOME`.

| [[GNOME.jpeg]] | [[LXDE.jpeg]] |
|---|---|
| [`GNOME`](https://en.wikipedia.org/wiki/GNOME) | [`LXDE`](https://en.wikipedia.org/wiki/LXDE) |
