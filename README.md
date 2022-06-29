Instruções de uso<br/>
- 1104.py: https://www.beecrowd.com.br/judge/pt/problems/view/1104<br/>
A primeira entrada deve ser feita passando dois numeros separados por espaço. exemplo: 3 4.<br/>
A segunda entrada são os numeros que correspondem as cartas de Alice, separados por espaço. Exemplo: 1 2 3.<br/>
A terceira entrada são os numeros que correspondem as cartas de Beatriz, separados por espaço. Exemplo: 4 5 6 7.<br/>
A saida será o número de trocas possíveis. Exemplo: 3.<br/>
Após a saida, o programa retornará para a primeira entrada. A entrada 0 0 (zero, espaço, zero) termina a execução.<br/>

- 1867.py: https://www.beecrowd.com.br/judge/pt/problems/view/1867<br/>
A primeira entrada deve ser feita passando dois numeros separados por espaço. exemplo: 10 11.<br/>
A saida será o digito que corresponde ao numero com maior algarismo unico, após a soma individual de seus algarismos. 1 para o primeiro numero, 2 para o segundo numero, 0 para empate. Exemplo  2.<br/>
Após a saida, o programa retornará à entrada. A entrada 0 0 (zero, espaço, zero) termina a execução.<br/>

- 1121.py: https://www.beecrowd.com.br/judge/pt/problems/view/1121<br/>
A primeira linha da entrada deve ser feita digitando 3 numeros separados por espaço. Exemplo: 3 3 3. Os números são, respectivamente, numero de linhas, numero de colunas e numero de comandos a serem dados.<br/>
As linhas em sequência devem ser os elementos que vão compor a matriz. Cada entrada será uma linha, com as colunas sendo os caracteres digitados. Os caracteres devem ser digitados sem espaço. Exemplo: .#*S .<br/>
O numero de entradas que compõe a matriz é proporcional ao numero de linhas que você atribuiu a ela. Uma matriz 3x3 terá 3 entradas de linha. A menor matriz aceita é 2x2.<br/>
Após a entrada das linhas, será as entradas de comandos de movimentação. E para esquerda, F para frente e D para direita. Os comandos devem ser dados em letras maiusculas e sem espaço. Exemplo: FEFFEFEFDD.<br/>

Sugestão de teste:<br/><br/>
..*#<br/>
S...<br/>
.*..<br/>
..*.<br/>
FEFFDFEFEFFFEF<br/><br/>
Com essa entrada, o robô coletará 2 figurinhas e será impedido de coletar a terceira pela pilastra no meio do caminho (#).



