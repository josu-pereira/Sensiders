

# Sensiders

<p align="center">
  <img width="303" height="267" src="/LogoPreta.png">
</p>

## Contexto
  O projeto foi inicializado a partir do problema do longo tempo de espera em filas de supermercado e o alto fluxo dentro dos supermercados, o que afeta os clientes destes supermercados e também os próprios varejistas, porque esta demora em filas acarreta em clientes que querem fazer uma compra rápida, mas ao ver estas filas grandes ele acaba desistindo e indo embora. 
  Um dos motivos destas grandes filas ocorrerem é a falta de conhecimento dos horários de grande pico dentro do supermercado e isso afeta o gerenciamento dos caixas, como por exemplo, menos atendentes nos caixas neste horário.
  Isso gera muitas consequencias negativas como por exemplo em uma liquidação onde poderia haver um lucro de 30% do mercado, acaba gerando apenas 7% porque a lentidão na fila bloqueia o fluxo de clientes no supermercado.
  Visando este problema, a Sensiders desenvolveu uma solução. Esta solução conta com sensores instalados pelo supermercado obtendo dados da movimentação e fluxo dos clientes por todo o ambiente. Esses dados são mandados há uma base de dados e um sistema web é disponibilizado para os gerentes do mercado onde esses dados foram tratados e informam o movimento pelo supermercado através de gráficos e heatmaps, fazendo assim que os gerentes possam tomar decisões rápidas e precisas.

  Os computadores da frente do caixa requerem manutenções regularmente, necessitando de uma limpeza do HD, limpeza do componentes internos do PC, averiguação do funcionamento das memórias, manutenções preventivas, e o gerente não pode deixar que ele dê problema de forma inesperada, sem saber que isto trará impactos a ele, porque o cliente vendo que o supermercado apresenta instabilidades constantes no funcionamento durante a compra acaba acarretando na desistencia de clientes, que segundo uma pesquisa da Accenture Strategy identificou que 87% dos consumidores deixam de comprar em uma loja por conta de um atendimento ruim, diminuindo o lucro.
  E que se os caixas estivesse funcionando de forma adequada, teria trago um crescimento de 20% no lucro segundo uma pesquisa holandesa DIJK (1997), uma pesquisa de opinião acrescentou que o aumento nas vedas dava-se pelo tempo de espera.
  E que de acordo com uma pesquisa francesa "Umesh et al" (1989), que analisou o tempo de espera X custo de aprimoramento do sistema, foi detectado uma diminuição das reclamações dos clientes em 40%, impulsionando o lucro em 19%.
  Foi então que o grupo Sensiders decidiu realizar uma análise dos dados do hardware destas máquinas, para assim, o dono do estabelecimento evitar perdas de lucro e maximizar a satisfação dos clientes através de uma aplicação Desktop em conexão com um banco de dados em nuvem para prover maior seguridade e performance à aplicação.

## Solução Sensiders - Monitoramento
  Aplicação de monitoramento de pessoas
   ![](/lld.jpg)
   
  Aplicação de monitoramento do hardware
   ![](/lld2.jpg)

## Novos Recursos
    * Documentação atualizada
    * Redesign, novas funcionalidades e melhorias de desempenho no Front-End web
    * Monitoramento dos recursos de hardware dos caixas de atendimento e dos servidores Node
    * Client Desktop em Java com Dashboard dos dados lidos das máquinas de fácil visualização
    * API em Python capaz de ler os dados do Hardware e conversar com o usuário sobre estas informações, relacionando suas emoções
    
## Instalação
   Git Clone do repositorio
   
  ```shell
   $ git clone https://github.com/BandTec/Sensiders.git
  ```
    
   ![](/projeto1.png)
    
   Abra o diretorio com o terminal na pasta que foi feita o download.
   Vá em application e instale os pacotes do node 
   
  ```shell
   $ cd Application/
   $ cd projeto-aquisicao-local/projeto-node-local 
   $ npm i
   $ npm start
  ```
   ![](/projeto2.png)
    
  Projeto-site
  
  ```shell
   $ cd projeto-site/
   $ npm i
  ```
   ![](/projeto3.png)
    
  Dentro do diretorio: projeto-site, rode o seguinte comando para iniciar o sistema
  
  ```shell
   $ npm run dev
  ```
  Logo depois entre no seu navegador e acesse a url:
    > localhost:3333/
    
   ![](/projeto4.png)
    
## Tecnologias

Sensiders usou as seguintes documentações das tecnologias:

*[HTML] - Corpo do site </br>
*[CSS] - Estilo do site </br>
*[JavaScript] - Uso para verificações </br>
*[Node.js] - Backend completo </br>
*[MSSQL] - Conexão com o banco </br>
*[Java] - Sistema desktop </br>
*[Python] - Captura de dados de hardware </br>

## Licença

GNU

    
[HTML]: <https://developer.mozilla.org/pt-BR/docs/Web/HTML/HTML5>
[CSS]: <https://developer.mozilla.org/pt-BR/docs/Web/CSS>
[JavaScript]: <https://www.javascript.com/>
[Node.js]: <https://nodejs.org/en/>
[MSSQL]: <https://docs.microsoft.com/pt-br/sql/?view=sql-server-ver15>
[Java]: <https://www.java.com/pt_BR/>
[Python]: <https://www.python.org/>

### Equipe

| [**Alexandre Yucra**](https://github.com/Aleyucra74) | [**Felipe Azevedo**](https://github.com/felipe-dias-azevedo) | [**Gabriel Ronny**](https://github.com/gabrielronny) | [**Josue Pereira**](https://github.com/josu-pereira) | [**Patrick Lessa**](https://github.com/PatrickLessa) |
    

