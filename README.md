# boletim_diario_da_operacao

"O Boletim diário da operação é um documento disponibilizado pela ONS e traz diáriamente os resultados da operação, este documento serve de subsídio às equipes de Programação, Pré-Operação e Tempo Real e também como fonte de dados estatísticos." [https://ons.org.br](https://www.ons.org.br/paginas/resultados-da-operacao/boletins-da-operacao)

Este projeto visa realizar a coleta dos dados disponibilizados diariamente pelo ONS e entregá-los em um formato mais amigável para consumo.


Neste primeiro push, estamos concentrando nossos esforços na coleta, padronização e exportação em formato CSV dos dados relacionados ao "Balanço de energia - Diário" e "Balanço de energia - Acumulado até o dia" Esses dados são estruturados da seguinte forma:

producao | programado | verificado | desvio | regiao | data_diario


Nosso próximo passo é ampliar a gama de dados relevantes que coletamos, visando integrá-los em um banco de dados relacional. Isso permitirá uma consulta mais eficiente e uma análise mais abrangente das informações, facilitando o cruzamento de dados e a obtenção de insights valiosos.

---

## Atualizações

30/09/2023

Adicionados os seguintes arquivos, onde cada um é responsável pela coleta dos dados das respectivas abas do boletim diário:

**- balanco_diario.py:** 'Balanço de Energia' e 'Balanço de Energia Acumulado'

**- carga_horaria.py:**  'Carga Horária'

**- demanda_maxima.py:** 'Demanda Máxima'

**- energia_armazenada.py:** 'Variação Energia Armazenada'

**- energia_natural_afluente.py:** 'Energia Natural Afluente'

**- motivo_despacho_termico.py:** 'Motivo do Despacho Térmico'

**- producao.py:** 'Produção Térmica', 'Produção Hidráulica', 'Produção Eólica', 'Produção Solar'

**- reserva_girante.py:** 'Reserva Girante Demanda Máx.'

**- reservatorios_hidraulicos.py:** 'Sit. Princ. Reservatórios S', 'Sit. Princ. Reservatórios SE', 'Sit. Princ. Reservatórios N', 'Sit. Princ. Reservatórios NE'


Cada um destes arquivos possui seu respectivo arquivo com prefixo 'collect_', os arquivos 'collect_' são utilizados para organizar a chamada dos respectivos scripts de coleta, centralizar inialização da função, parse dos argumentos e salvamento do arquivo de output no diretório indicado.


**commons.py:** Arquivo criado para concentrar as diversas funções de tratamento que possam ser compartilhadas entre os vários scripts.


 