# HeroAlerter
Script to receive alerts when a worker is down or below it's configured hashrate, works with herominers.com

usage:
python3 -m pip install -r requirements.txt
python3 halert.py


All you have to do is enter any cryptocurrency from herominers and enter your crypto address (needed to access workers list from herominers api), select the scan frequency, set a minimum hashrate(good for multi-gpu when only some of them hangs), and how many times the audio.wav should play.

When a new worker is found, you can decide to add it to the alert list, this will decide if the system plays an audio file or not when the worker has an hashrate of 0 or lower than its configured mminimum hashrate.

Donate to fight the system</br>Haven - XHV: hvs1Vs4GjeU1b88ojdf4WJ411etuGcyzHDb551aGZmFHHMB7dzPWpYn9vmiWayxty4hZf3SeeAzoqGpbsWHmzbK54DAdUf4d1L</br>
Bitcoin - BTC: bc1qjywjjgy2xjvwujnke7vhxcllqlp7q6jh734mx7</br>
Ethereum - ETH: 0x3ee7c0538e7320c3560314da70ec893f55f4662d</br>
Cardano - ADA: addr1qyvnlwgauhuenhaagcdlty7yk6d36al30rd5m32uwdcu5c5me8sfk2ht0n0j9dy4rl6sn7rm7t0hdd4850xvfyfm5qtq0vun86
