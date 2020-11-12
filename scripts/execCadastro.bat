@echo off

setlocal enabledelayedexpansion

echo Seja bem vindo
@REM set /p maquina=Por favos coloque o nome da sua maquina:

echo vamos inicializar o programa para cadastrar a maquina

java -version

IF "%ERRORLEVEL%" EQU "0" (
     echo voce tem o java entao vamos prosseguir

     cd ..\Application\cadastro-componentes\
     mvn clean install
     cd target\
     icacls cadastro-componentes-1.0-SNAPSHOT-jar-with-dependencies.jar /grant Users:F
     java -jar cadastro-componentes-1.0-SNAPSHOT-jar-with-dependencies.jar
)
