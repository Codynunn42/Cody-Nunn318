$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $repoRoot

$currentBranch = (git branch --show-current).Trim()
if (-not $currentBranch) {
    throw 'Unable to detect current git branch.'
}

Write-Host "Fetching latest remote changes..."
git fetch --all --prune

$branchesToSync = @('main', 'executive-desk-working')
foreach ($branch in $branchesToSync) {
    Write-Host "Syncing $branch..."
    git switch $branch | Out-Null
    git pull --ff-only
}

Write-Host "Returning to $currentBranch..."
git switch $currentBranch | Out-Null

git status --short --branch
Write-Host 'Morning sync complete.'
