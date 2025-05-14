function mostrar(){
    var quinze =Number(document.getElementById('valorquinze').value);
    var temp = Number(document.getElementById('tempo').value);
    var total = (temp / 15) * quinze;

    resposta.textContent = "Valor a Pagar R$: " + total.toFixed(2);
}

var botao = document.querySelector("input[type='button']");
botao.addEventListener("click", mostrar);