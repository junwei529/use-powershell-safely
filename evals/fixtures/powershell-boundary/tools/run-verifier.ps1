$inputPath = Join-Path $PSScriptRoot '..\data\input file.json'
$verifierPath = Join-Path $PSScriptRoot 'verify_json.py'

$command = "python `"$verifierPath`" --input $inputPath"
$output = & pwsh -NoProfile -Command $command 2>&1
$exitCode = $LASTEXITCODE

if ($exitCode -ne 0) {
    Write-Error "JSON invalid: $output"
    exit $exitCode
}

$output
