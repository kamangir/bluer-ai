# Raspberry Pi

1. Download the image:

    - `Headless:` [the latest Rapian Buster Lite](https://downloads.raspberrypi.org/raspbian_lite_latest).
    - `With UI:` [2020-02-13-raspbian-buster.zip](http://downloads.raspberrypi.org/raspbian/images/raspbian-2020-02-14/).

2. Open [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and select `Operating System` -> `Use custom` and select the image. Then press `Shift+Ctrl+X` to open `Advanced options`, select `Set hostname`, and enter a unique host name. Now select `Enable SSH` and `Set password` for the `pi` user to `abcli2025` and press `Save`. Proceed to write the SD Card.

3. After the write is complete, reinsert the SD card, if necessary, and run `@wifi copy_to_sd_card`. Then, eject the SD card, insert it into the Raspberry Pi, turn the motherboard on, and wait for the motherboard to boot.

4. `Headless:` run `abcli ssh rpi <host-name>`. Then, run `abcli seed headless_rpi clipboard` in another terminal and paste it into the ssh window.

5. `With UI:` Insert a [seed usb key](seed), open a terminal, and run `bash /media/pi/SEED/abcli/rpi.sh`.

7. `With UI:` Run `sudo nano /boot/config.txt` and uncomment the line that reads `#hdmi_force_hotplug=1`, if it exists. If you wish to rotate the screen, add one of the following to the end of this file and then reboot:

```
display_rotate=0
display_rotate=1
display_rotate=2
display_rotate=3
```

8. `Headless:` Run `sudo raspi-config` -> `Interfacing Options` -> enable `Camera` and other interfaces as needed, then go to `System Options` -> `Boot / Auto Login` and select `Console Autologin`. 

9. `With UI:` go to `Preferences` -> `Raspberry Pi Configuration` -> `Interfaces` and change the following to `Enabled`: `Camera:`, `I2C`, and `SSH`, as needed.

---

Known issue: on `rpi4b` headless install raises `ERROR: Wheel 'tensorflow' located at /home/pi/tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl is invalid.`