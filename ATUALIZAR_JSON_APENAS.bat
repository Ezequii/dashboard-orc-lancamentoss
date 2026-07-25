@echo off
setlocal EnableExtensions
chcp 65001 >nul
cd /d "%~dp0"
title Dashboard AMAGGI - Atualizar JSON

echo =====================================================
echo  DASHBOARD AMAGGI - ATUALIZAR JSON APENAS
 echo =====================================================

echo Este processo NAO faz commit, push ou build.
echo.

where python >nul 2>nul || (
  echo ERRO: Python nao foi encontrado.
  echo Instale o Python e marque a opcao Add Python to PATH.
  pause
  exit /b 1
)

if not exist "atualizar_dados\CONTROLE_DE_REQUISICOES_2026.xlsx" (
  echo ERRO: planilha nao encontrada.
  echo Coloque o arquivo em atualizar_dados\CONTROLE_DE_REQUISICOES_2026.xlsx
  pause
  exit /b 1
)

python -c "import openpyxl" >nul 2>nul
if errorlevel 1 (
  echo Instalando a biblioteca openpyxl somente na primeira vez...
  python -m pip install openpyxl==3.1.5
  if errorlevel 1 goto erro
)

echo Convertendo a planilha para JSON...
python scripts\atualizar_dados.py
if errorlevel 1 goto erro

echo.
echo =====================================================
echo  JSON ATUALIZADO COM SUCESSO
 echo =====================================================
echo.
echo Agora abra o GitHub Desktop e envie manualmente:
echo.
echo  atualizar_dados\CONTROLE_DE_REQUISICOES_2026.xlsx
echo  public\data\orcamentos.json
echo  public\data\meta.json
echo.
echo Mensagem sugerida: Atualiza dados do dashboard
pause
exit /b 0

:erro
echo.
echo A conversao falhou. Leia a mensagem acima.
echo Os arquivos anteriores foram preservados na pasta backups.
pause
exit /b 1
