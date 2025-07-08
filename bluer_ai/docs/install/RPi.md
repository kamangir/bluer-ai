# Raspberry Pi

1. Open [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and select `Operating System` -> `Raspberry Pi OS (other)` and select an image, either lite (headless) or full (with GUI). 

> ℹ️ A 32-bit legacy image, such as `Bullseye`, has better compatibility with the camera, but will be more challenging when trying to install the latest OpenCV and torch. **64-bit images, are, therefore, recommended**.

2. Then press `Shift+Ctrl+X` to open `Advanced options`, select `Set hostname`, and enter a unique host name, the select `Set username and password` and set the user to `pi` and the password to `abcli2025`. Then select `Configure wireless LAN` and set the SSID and password. In `Services` select `Enable SSH` and `Use password authentication` and press `Save`. Proceed to write the SD Card.

3. After the write is complete, eject the SD card, insert it into the Raspberry Pi, turn the motherboard on, and wait for the motherboard to boot.

## Headless

4. run `@ssh rpi <host-name>`. Then, run `@seed headless_rpi clipboard` (or `headless_rpi_64_bit`) in another terminal and paste it into the ssh window.

5. (only needed on older versions) Run `sudo raspi-config` -> `Interfacing Options` -> enable `Camera` and other interfaces as needed, then go to `System Options` -> `Boot / Auto Login` and select `Console Autologin`. 

## With UI

4. Insert a [seed usb key](seed), open a terminal, and run `bash /media/pi/SEED/abcli/rpi.sh`.

5. Run `sudo nano /boot/config.txt` and uncomment the line that reads `#hdmi_force_hotplug=1`, if it exists. If you wish to rotate the screen, add one of the following to the end of this file and then reboot:

```
display_rotate=0
display_rotate=1
display_rotate=2
display_rotate=3
```

6. go to `Preferences` -> `Raspberry Pi Configuration` -> `Interfaces` and change the following to `Enabled`: `Camera:`, `I2C`, and `SSH`, as needed.

## known issues

1. on `rpi4b` headless install raises `ERROR: Wheel 'tensorflow' located at /home/pi/tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl is invalid.`