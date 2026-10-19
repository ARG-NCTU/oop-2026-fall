param(
    [ValidateRange(1, 4)][int]$Case = 1,
    [ValidateRange(1, 20)][int]$Warp = 5,
    [switch]$Solution
)
$ErrorActionPreference = 'Stop'
$mission = if ($Solution) { 'exp1_tugofwar_solution' } else { 'exp1_tugofwar' }
wsl -d Ubuntu -- env PATH=/home/nick0/moos-ivp/bin:/usr/bin:/bin bash -c "cd /home/nick0/moos-ivp/ivp/missions/$mission; exec ./launch.sh --case=$Case --warp=$Warp"
exit $LASTEXITCODE
