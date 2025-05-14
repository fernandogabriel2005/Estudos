function conta(){
    var valorbuffet = Number(document.getElementById('buffet').value);
    var consu = Number(document.getElementById('consumo').value);
    var math = consu * 0.001
    var resp = valorbuffet * math

    resposta.textContent = "Valor a pagar R$: " + resp.toFixed(2);
}

var botao = document.querySelector("input[type='button']");
botao.addEventListener("click", conta);