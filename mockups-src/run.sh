#!/bin/bash
# usage: run.sh job.json   (un seul PSD ouvert à la fois)
cp "$1" /Users/jaydogo/jaydogo-portfolio/mockups-src/job.json
osascript -e "with timeout of 1800 seconds" -e "tell application \"Adobe Photoshop 2026\" to do javascript file (POSIX file \"/Users/jaydogo/jaydogo-portfolio/mockups-src/fill.jsx\")" -e "end timeout"
