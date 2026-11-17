#!/bin/bash
#----------------------------------------------------------
#  Script: clean.sh   清除 log 與 nsplug 產生的 targ 檔
#----------------------------------------------------------
cd "$(dirname "$0")"
rm -rf  LOG_* MOOSLog_*
rm -f   targ_*  *~  .LastOpenedMOOSLogDirectory
echo "exp1_tugofwar cleaned."
