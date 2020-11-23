FROM mjalas/javafx
FROM maven:3.6.3-jdk-11

WORKDIR /apps
COPY . /apps
RUN mvn clean install

CMD mvn exec:java -Dexec.mainClass="br.com.bandtec.agoravai.App"

# apt install openjfx
#docker build -t <nomeDaImagem> .
#on another terminal run : socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
#docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$(ipconfig getifaddr en0):0 <nomeDaImagem>
