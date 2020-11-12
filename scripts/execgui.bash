#!/bin/bash

echo -e "\e[48;5;204m [Sensiders]: \e[0m Oi somos a Sensiders, vamos lhe ajudar a instalar umas coisas"
read -p " Gostaria de atualizar uns pacotes?? (s/n)" pckt
if [[ $pckt == "s" ]]
	then
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Estaremos instalando os pacotes, aguarde..."
	        sudo apt update && sudo apt upgrade
        	sudo apt install maven
	else
	   	echo -e "\e[48;5;204m [Sensiders]: \e[0m Tudo bem, vamos continuar"
fi

echo -e "\e[48;5;204m [Sensiders]: \e[0m caso voce esteja numa instancia"
read -p " Gostaria de instalar uma window manager i3?(s/n)" gui
if [[ $gui == "s" ]]
	then
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Estaremos instalando os pacotes, aguarde..."

		#sudo apt install xrdp lxde-core lxde tigervnc-standalone-server -y
		sudo apt install xrdp tigervnc-standalone-server xorg i3 i3blocks i3lock terminator acpi xbacklight rofi feh clipit pcmanfm
		echo -e "\e[48;5;204m [Sensiders]: \e[0m aguarde mais um pouco..."
		sed -i 's/max_bpp=32/max_bpp=16/g' /etc/xrdp/xrdp.ini
		sed -i 's/allowed_users=console/allowed_users=ubuntu/g' /etc/X11/Xwrapper.config
		service xrdp start
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Ja configurado, agora para se conectar na area remota, conecte com o ip da instancia"
	else
		echo -e "\e[48;5;204m [Sensiders]: \e[0m Tudo bem, vamos continuar"
		read -p " Gostaria de iniciar o java? (s/n)" java
	if [[ $java == "s" ]]
		then
        		echo -e "\e[48;5;204m [Sensiders]: \e[0m Iniciando java..."
			sleep 2
			source ./execjava.bash
	fi
fi

