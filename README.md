# Cleanroom

Cleanroom allows you to visualize your brainwaves in a webapp in real-time.
Unlike most tools, this avoids
[lsl](https://github.com/sccn/labstreaminglayer). This means fewer
dependencies and things that can break. In particular, it's helpful on
Raspberry Pi where lsl support (as of August 2018) is iffy. It may also be
helpful as a learning exercise, or if you're just generally having trouble
with other tooling for reading Muse headset data, since it's much simpler.
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

## Similar projects

Before you try this project, I encourage you to try other tooling first, which
is likely much more mature / less buggy! Cleanroom is more applicable if you're
on a less-commonly-used platform, or if other tooling is not working well for
you.

This is not a complete index of tooling, but some of the things worth checking
out:

1) [Muse LSL](https://github.com/alexandrebarachant/muse-lsl)
2) [LSL](https://github.com/sccn/labstreaminglayer)
3) [BCI Workshop code](https://github.com/NeuroTechX/bci-workshop/), which
   this repo draws a lot from.
