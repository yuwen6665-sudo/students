# 学习环境启动脚本
Set-Location "E:\study"
$venv = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $venv) { . $venv }

Write-Host ""
Write-Host "=== 环境已就绪 ===" -ForegroundColor Green
Write-Host ("Python : " + (python --version 2>&1))
Write-Host ("venv   : " + (Get-Command python).Source)
Write-Host ""
Write-Host "常用命令：" -ForegroundColor Cyan
Write-Host "  python hello.py    运行脚本" -ForegroundColor Cyan
Write-Host "  code .             用 VS Code 打开当前目录" -ForegroundColor Cyan
Write-Host "  exit               退出" -ForegroundColor Cyan
Write-Host ""
Write-Host "注意：这里才是命令行。IDLE 里那个 >>> 只能打 Python 代码。" -ForegroundColor Yellow
Write-Host ""