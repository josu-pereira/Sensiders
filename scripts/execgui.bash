#!/bin/bash

echo -e "\e[48;5;204m [Sensiders]: \e[0m Oi somos a Sensiders, vamos lhe ajudar a instalar umas coisas"
sudo apt update && sudo apt upgrade

echo -e "\e[48;5;204m [Sensiders]: \e[0m caso voce esteja numa instancia"
read -p " Gostaria de instalar uma gui lxde?(s/n)" gui
if [[ $gui == "s" ]]
	then
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Estaremos instalando os pacotes, aguarde..."

		sudo apt install xrdp lxde-core lxde tigervnc-standalone-server -y
		echo -e "\e[48;5;204m [Sensiders]: \e[0m aguarde mais um pouco..."
		sed -i 's/max_bpp=32/max_bpp=16/g' /etc/xrdp/xrdp.ini
		sed -i 's/allowed_users=console/allowed_users=ubuntu/g' /etc/X11/Xwrapper.config
		service xrdp start
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Ja configurado, agora para se conectar na area remota va no win e conecte com o ip da instancia"
	else
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Tudo bem, vamos continuar"
fi

echo -e "\e[48;5;204m [Sensiders]: \e[0m Verificando se voce tem java."

java -version

if [[ $? = 0 ]]
	then
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Vemos que voce ja o Java instalado, vamos executar a nossa aplicacao"
		cd ..
		cd Application/projeto-java-monitoramento/target/
		sudo chmod 777 projeto-java-monitoramento-1.0-SNAPSHOT-jar-with-dependencies.jar
		java -jar projeto-java-monitoramento-1.0-SNAPSHOT-jar-with-dependencies.jar		
	else
		echo -e "\e[48;5;204m [Sensiders]: \e[0m nao encontramos nenhuma versao do java instalado"
		read -p "vamos instalar o java para voce, voce confirmar?(s/n)" res
	if [[ $res == "s" ]]
		then
			echo -e "\e[48;5;204m [Sensiders]: \e[0m Instalando o java"
			sleep 2
			curl -s "https://get.sdkman.io" | bash
			source "$HOME/.sdkman/bin/sdkman-init.sh"
			sdk install java 8.0.265.j9-adpt
		#	sudo apt install java
		#	sudo apt install jre-default-headless
		#	sudo apt install opejdk-11-jre
			echo -e "\e[48;5;204m [Sensiders]: \e[0m Instalacao com sucesso"
		else
			echo -e "\e[48;5;204m [Sensiders]: \e[0m Tudo bem, nao vamos instalar o java"
	fi
fi




