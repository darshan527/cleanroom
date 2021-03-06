# Cleanroom

Cleanroom allows you to visualize your brainwaves in a webapp in real-time.
Unlike most tools, this avoids
[lsl](https://github.com/sccn/labstreaminglayer). This means fewer
dependencies and things that can break. In particular, it's helpful on
Raspberry Pi where lsl support (as of August 2018) is iffy. The trade-off
is that, unlike lsl, this not battle-tested and should not be used in a
production setting.

The UI looks like this, but uhh...bigger:

<p align="center">
    <img src="https://raw.github.com/ysimonson/cleanroom/master/demo.gif">
</p>

## Hardware requirements

* [A Muse 2016 headset](http://www.choosemuse.com/)
* If you are on mac or windows, a [BLED112 bluetooth LE dongle](https://www.silabs.com/products/wireless/bluetooth/bluetooth-low-energy-modules/bled112-bluetooth-smart-dongle), as pygatt requires it.

## Getting started

1) Plug in the dongle and turn on your Muse headset.
2) Clone this repo: `git clone git@github.com:ysimonson/cleanroom.git`.
3) Setup virtualenv: `virtualenv -p python3 venv`.
4) Install dependencies `pip install -r requirements.txt`.
5) Start the server: `python web.py`.
6) Wait for the server to connect to your Muse headset.
7) Navigate to `http://localhost:8888`.

## Platform-specific issues

Mac:

* You may need to manually apply [this fix](https://github.com/peplin/pygatt/issues/159).

Linux:

* If you get an operation not permitted error when starting the server, you need to run this: ``sudo setcap 'cap_net_raw,cap_net_admin+eip' `which hcitool` ``

## Similar projects

1) [Muse LSL](https://github.com/alexandrebarachant/muse-lsl)
2) [LSL](https://github.com/sccn/labstreaminglayer)
3) [BCI Workshop code](https://github.com/NeuroTechX/bci-workshop/), which
   this repo draws a lot from.
