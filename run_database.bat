@echo off
CHCP 1251

D:

set PROJECT_PATH="D:\projects\ssk_new\back"

:: ������ API �����
echo ------------------------------"
echo "������ ���� ������"
echo ------------------------------"

:: ����������� ��������� ���������
set VENV_FILE=%PROJECT_PATH%\env\Scripts\activate.bat
:: ���� �������
set SCRIPT_FILE=%PROJECT_PATH%\core.py

:: ����������� ���������
call %VENV_FILE%
:: ������ �����
cd %PROJECT_PATH%
python %SCRIPT_FILE%

pause