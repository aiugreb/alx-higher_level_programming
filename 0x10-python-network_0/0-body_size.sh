#!/bin/bash
# displays the size of the body
curl -sw '%{size_download}\n' -o /dev/null "$1"
