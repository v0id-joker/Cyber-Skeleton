param([string]$Action)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$shell = New-Object -ComObject Shell.Application

switch ($Action) {
    'check' {
        $explorerWindows = $shell.Windows() | Where-Object { $_.Name -match "File Explorer|Windows Explorer" }
        if ($explorerWindows) {
            Write-Output "$([char]0xe5fe)"
        } else {
            Write-Output "$([char]0xe6ad)"
        }
    }
    'launch' {
        Start-Process "explorer.exe"
    }
    'close' {
        $shell.Windows() | Where-Object { $_.Name -match "File Explorer|Windows Explorer" } | ForEach-Object { $_.Quit() }
    }
}