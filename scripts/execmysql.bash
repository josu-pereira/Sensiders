#!/bin/bash
echo -e "\e[48;5;204m [Sensiders]: \e[0m Instalando docker."

sudo apt-get install docker.io
sudo systemctl start docker
sudo systemctl enable docker

echo -e "\e[48;5;204m [Sensiders]: \e[0m Verificando se voce tem mysql no docker."

sudo docker inspect mysql8 | grep MYSQL_MAJOR

if [[ $? = 0 ]]
	then
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Vemos que voce ja o mysql no docker baixado"
	else
		echo -e "\e[48;5;204m [Sensiders]: \e[0m nao encontramos nenhuma versao do mysql instalado"
		read -p "vamos instalar a imagem mysql para voce, voce confirmar?(s/n)" res
	if [[ $res == "s" ]]
		then
			echo -e "\e[48;5;204m [Sensiders]: \e[0m Instalando a imagem"
            sudo docker pull mysql
            sudo docker run -d -p 3306:3306 -e"MYSQL_ROOT_PASSWORD=urubu100" mysql
            echo -e "\e[48;5;204m [Sensiders]: \e[0m Abrindo o terminal da instancia:"
            echo -e "\e[48;5;204m [Sensiders]: \e[0m Senha do mysql: \e[1murubu100"
            sleep 2
		    sudo docker exec -it $(sudo docker ps -a -q) bash
	fi
fi
