#!/bin/bash -e
#----------------------------------------------------------
#  Script: launch.sh   (AOOP Ch2 實驗一：拔河)
#  用法:   ./launch.sh --case=2 --warp=5
#----------------------------------------------------------
#  Part 1: 預設值
#----------------------------------------------------------
ME=`basename "$0"`
TIME_WARP=1
CASE=1
GUI="yes"
AUTO=""
JUST_MAKE=""
DEPLOY=""

#----------------------------------------------------------
#  Part 2: 處理命令列參數
#----------------------------------------------------------
for ARGI; do
    if [ "${ARGI}" = "--help" -o "${ARGI}" = "-h" ] ; then
        echo "$ME [OPTIONS] [time_warp]"
        echo "  --case=N       情境 (東:北) 1:100/100  2:100/30  3:30/100  4:100/0"
        echo "  --warp=N       Time warp (也可直接寫數字，例如 ./launch.sh 5)"
        echo "  --nogui        不開 pMarineViewer (無頭測試用)"
        echo "  --auto, -a     不開 uMAC，背景執行後直接結束 (腳本用)"
        echo "  --deploy, -d   啟動後自動送 DEPLOY=true (不用按按鈕)"
        echo "  --just_make,-j 只產生 targ 檔，不啟動"
        exit 0
    elif [ "${ARGI//[^0-9]/}" = "$ARGI" -a "$TIME_WARP" = 1 ]; then
        TIME_WARP=$ARGI
    elif [ "${ARGI:0:7}" = "--warp=" ]; then
        TIME_WARP="${ARGI#--warp=*}"
    elif [ "${ARGI:0:7}" = "--case=" ]; then
        CASE="${ARGI#--case=*}"
    elif [ "${ARGI}" = "--nogui" ]; then
        GUI="no"
    elif [ "${ARGI}" = "--auto" -o "${ARGI}" = "-a" ]; then
        AUTO="yes"
    elif [ "${ARGI}" = "--deploy" -o "${ARGI}" = "-d" ]; then
        DEPLOY="yes"
    elif [ "${ARGI}" = "--just_make" -o "${ARGI}" = "-j" ]; then
        JUST_MAKE="yes"
    else
        echo "$ME: Bad arg: $ARGI  (用 --help 看說明)"
        exit 1
    fi
done

if [ "$CASE" != 1 -a "$CASE" != 2 -a "$CASE" != 3 -a "$CASE" != 4 ]; then
    echo "$ME: --case 只能是 1, 2, 3, 4"
    exit 1
fi

#----------------------------------------------------------
#  Part 3: 用 nsplug 展開設定檔
#----------------------------------------------------------
cd "$(dirname "$0")"
nsplug meta_tug.moos targ_tug.moos -f --strict \
       WARP=$TIME_WARP CASE=$CASE GUI=$GUI
nsplug meta_tug.bhv  targ_tug.bhv  -f --strict CASE=$CASE

if [ "$JUST_MAKE" = "yes" ]; then
    echo "$ME: targ_tug.moos / targ_tug.bhv 已產生 (case=$CASE)"
    exit 0
fi

#----------------------------------------------------------
#  Part 4: 啟動
#----------------------------------------------------------
echo "Launching tug (case=$CASE) WARP=$TIME_WARP"
pAntler targ_tug.moos >& /dev/null &

if [ "$DEPLOY" = "yes" ]; then
    sleep 3
    uPokeDB targ_tug.moos DEPLOY=true MOOS_MANUAL_OVERRIDE=false >& /dev/null
    echo "DEPLOY sent."
fi

if [ "$AUTO" = "yes" ]; then
    exit 0
fi

uMAC -t targ_tug.moos
kill -- -$$
