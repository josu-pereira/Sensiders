
sudo apt update && sudo apt install python3-dev virtualenv python3-pip python3-venv unixodbc-dev
python3 -m pip install virtualenv

#definindo o nome do ambiente
read -p "Digite o nome do ambiente virtual: " nomeambiente

if [[ -d ./$nomeambiente  ]]
then
	echo "Essa maquina ja existe entao vamos prosseguir com a execucao"
	echo "vamos ativar o ambiente virtual"
	source $nomeambiente/bin/activate

	echo "voltando para a raiz do projeto"
	echo "instalando as bibliotecas para o projeto"
	python3 -m pip install psutil mysql-connector-python mysql-connector requests pyodbc

else
	echo "esse nome de ambiente virtual nao existe entao vamos criar um novo"
	echo "vamos criar um novo ambiente"
	python3 -m venv $nomeambiente

	echo "ativando o ambiente"
	source $nomeambiente/bin/activate

	echo "instalando as bibliotecas para o projeto"
	python3 -m pip install psutil mysql-connector-python mysql-connector requests pyodbc

fi

echo "executando o script"
python3 main.py
