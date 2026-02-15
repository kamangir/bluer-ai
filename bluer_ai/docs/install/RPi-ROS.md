# install: RPi-ROS

1. Open [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and select `Operating System` -> `Ubuntu 20.04 LTS Server` -> Then press `Shift+Ctrl+X` to open `Advanced options`, select `Set hostname`, and enter a unique host name. Then, `Set username and password` -> user: `pi` and password: `abcli2025`. Then, `Configure wireless LAN` and add the network name and password. Then, select `Services` -> `Enable SSH` and press `Save`. Proceed to write the SD Card.

2. After the write is complete, insert it into the Raspberry Pi, connect the HDMI cable to a monitor, turn the motherboard on, and wait for the motherboard to boot.

3. It is likely that the boot does not complete automatically. Consult AI.

4. run `@seed headless_ubuntu_rpi clipboard`. now, run `@ssh rpi <host-name>` and paste the seed 🌱 into the ssh window.

5. ⚠️ needs more work - `sudo nano /boot/firmware/usercfg.txt` and add these lines,

```init
start_x=1
gpu_mem=128
dtoverlay=ov5647
```

this `dtoverlay` is for camera v1.3, use proper value for other cameras.

then `sudo reboot` and after reboot `ls /dev/video*`, you should see something like `/dev/video0`.
