[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]] $Path
)

[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)

$scriptPath = Join-Path $PSScriptRoot 'check-markdown.mjs'
if ($Path -and $Path.Count -gt 0) {
    & node $scriptPath @Path
} else {
    & node $scriptPath
}
exit $LASTEXITCODE
