function mostrar (){

    var titulo = document.getElementById("titulo").value;
    var hora = Number(document.getElementById("minutos").value);
    var horas = Math.floor(hora / 60) //Math.floor = abaixa para BAIXO. 108 / 60 = 1,8, arredondando para baixo fica 1.
    var minutos = hora % 60 // o que resta da divisão. 10 / 3 vai dar 9 e sobrar 1, esse % vai nos mostrar o 1. 108/60 sobra 48....
    
    
    document.getElementById("resposta").textContent = horas + " hora(s) e " + minutos + " minuto(s)";
    document.getElementById("titulodois").textContent = titulo;

}

var botao = document.querySelector("input[type= 'button']");

botao.addEventListener("click", mostrar)
