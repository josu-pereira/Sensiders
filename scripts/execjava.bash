#!/bin/bash

echo -e "\e[48;5;204m [Sensiders]: \e[0m Verificando se voce tem java."

java -version

if [[ $? = 0 ]]
	then
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Vemos que voce ja o Java instalado, vamos executar a nossa aplicacao"
		cd ..
		cd Application/projeto-java-monitoramento/
		mvn clean install
		cd target/

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
			sdk install java 11.0.9.j9-adpt
			
			echo -e "\e[48;5;204m [Sensiders]: \e[0m Instalacao com sucesso o java"
			echo -e "\e[48;5;204m [Sensiders]: \e[0m Agora vamos executar o programa"
			cd ..
			cd Application/projeto-java-monitoramento/
			mvn clean install
			cd target/
			sudo chmod 777 projeto-java-monitoramento-1.0-SNAPSHOT-jar-with-dependencies.jar
			java -jar projeto-java-monitoramento-1.0-SNAPSHOT-jar-with-dependencies.jar
		else
			echo -e "\e[48;5;204m [Sensiders]: \e[0m Tudo bem, nao vamos instalar o java"
            
	fi
fi
