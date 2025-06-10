# Raspberry Pi + ROS

1. Open [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and select `Operating System` -> `Ubuntu 20.04 LTS Server` -> Then press `Shift+Ctrl+X` to open `Advanced options`, select `Set hostname`, and enter a unique host name. Then, `Set username and password` -> user: `pi` and password: `abcli2025`. Then, `Configure wireless LAN` and add the network name and password. Then, select `Services` -> `Enable SSH` and press `Save`. Proceed to write the SD Card.

2. After the write is complete, insert it into the Raspberry Pi, connect the HDMI cable to a monitor, turn the motherboard on, and wait for the motherboard to boot.

3. It is likely that the boot does not complete automatically. Consult AI.

4. `@ssh rpi <host-name>`. 🔥 Then, run `@seed headless_ubuntu_rpi clipboard` in another terminal and paste it into the ssh window.

🔥