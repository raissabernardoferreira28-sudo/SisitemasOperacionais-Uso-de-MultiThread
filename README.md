# SisitemasOperacionais-Uso-de-MultiThread

Um sistema multithread permite que um único processo execute múltiplas tarefas (chamadas de threads) de forma simultânea ou alternada. Em vez de realizar uma tarefa por vez, o programa divide o trabalho, permitindo que diferentes partes do código rodem ao mesmo tempo. O programa utiliza multithreading para somar 10 milhões de números dividindo a tarefa ao meio. Enquanto a versão sequencial processa tudo em um único fluxo, a multithread cria dois "operários" (Threads) que calculam metades distintas simultaneamente. Elas utilizam uma lista global como recurso compartilhado para salvar os valores e o comando join() para sincronizar o sistema, garantindo que o resultado final só seja exibido após ambas terminarem. A grande vantagem é a eficiência e o melhor uso do processador, enquanto a desvantagem é a complexidade extra para evitar erros de sincronização.

Criação:
threading.Thread: Aqui você está "contratando" um operário novo. Você diz qual função ele deve executar (target) e quais dados ele deve usar (args).
start(): Este comando é o gatilho. Ele diz para o sistema operacional: "Pode começar a executar essa thread em paralelo com o resto do programa"

Sincronização:
O join é fundamental. Ele força a Thread Principal (a "dona" do programa) a parar e esperar até que as threads t1 e t2 terminem o serviço.

Compartilhamento:
As threads precisam de um lugar para colocar o resultado do que calcularam. Elas compartilham a lista global resultados_parciais.