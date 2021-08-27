FROM maven:3.6.3-jdk-11

ENV DEBIAN_FRONTEND noninteractive
ENV DISPLAY :0

RUN apt-get update && apt-get install --no-install-recommends -y xorg libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

WORKDIR /apps
COPY . /apps
RUN mvn clean install

CMD mvn exec:java -Dexec.mainClass="br.com.bandtec.agoravai.App"
#image: docker build -t <nomedaImagem> -f <dockerfile> .
#container: docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <nome da sua imagem aqui>
