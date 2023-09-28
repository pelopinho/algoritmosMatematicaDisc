function getHorarioAtual() { 
    /* Define a função 'getHorarioAtual', que cria uma 
    instância do objeto 'Date' chamada 'agora' que 
    representa os dados e a hora atual. Em seguida, extrai as horas,
    minutos e segundos dos dados atuais. Logo após isso, a função retorna uma
    string que retorna esses valores no formato h:mm:ss*/

    const agora = new Date();
    const horas = agora.getHours();
    const minutos = agora.getMinutes();
    const segundos = agora.getSeconds();
    return `${horas}:${minutos}:${segundos}`;
}

function calcularMinutosPassados() {
    /* Função que realiza a mesma tarefa da primeira função, porém com a
    finalidade de calcular os minutos passados desde a
    meia-noite (horas*60+minutos). Feito isso, ela retorna esse valor
    como um número de minutos */
    const agora = new Date();
    const horas = agora.getHours();
    const minutos = agora.getMinutes();
    const minutosPassados = horas * 60 + minutos;
    return minutosPassados;
}


/* Constante inicializada com o valor retornado pela
função 'getHorarioAtual', que conterá a hora atual*/
const horarioAtual = getHorarioAtual();

/* Constante inicializada com o valor retornado pela
função 'calcularMinutosPassados', que conterá o número total
de minutos passados desde a meia-noite  */
const minutosPassados = calcularMinutosPassados();


// Objetos criados para impressão das mensagens solicitadas no código
console.log(`Horário atual: ${horarioAtual}`);
console.log(`Minutos passados hoje: ${minutosPassados} minutos`);