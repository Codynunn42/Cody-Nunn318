$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$currentBranch = $null

Push-Location $repoRoot
try {
    $currentBranch = (git branch --show-current).Trim()
    if (-not $currentBranch) {
        throw 'Unable to detect current git branch.'
    }

    if (git status --porcelain) {
        throw 'Working tree is not clean. Commit or stash changes before running morning sync.'
    }

    Write-Host "Fetching latest remote changes..."
    git fetch --all --prune

    $branchesToSync = @('main', 'executive-desk-working')
    foreach ($branch in $branchesToSync) {
        Write-Host "Syncing $branch..."
        git switch $branch | Out-Null

        git pull --ff-only
    }
}
finally {
    if ($currentBranch) {
        Write-Host "Returning to $currentBranch..."
        git switch $currentBranch | Out-Null
    }

    Pop-Location
}

git status --short --branch
Write-Host 'Morning sync complete.'
