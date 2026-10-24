# Downloads the reference images listed in asset_manifest.tsv into the academy's Assets/ folders.
# Usage: powershell -ExecutionPolicy Bypass -File fetch_assets.ps1 -Academy "C:\path\to\vault\Roblox Design Academy"
# Existing files are skipped, never overwritten.
param([Parameter(Mandatory = $true)][string]$Academy)
$manifest = Join-Path $PSScriptRoot "asset_manifest.tsv"
Get-Content $manifest | Where-Object { $_ -and -not $_.StartsWith("#") } | ForEach-Object {
  $ref, $path, $url = $_ -split "`t"
  $dest = Join-Path $Academy $path
  if (Test-Path $dest) { Write-Host "skip (exists) $path"; return }
  New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
  try { Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing; Write-Host "ok   $path" }
  catch { Write-Host "FAIL $path  <- $url" }
}
