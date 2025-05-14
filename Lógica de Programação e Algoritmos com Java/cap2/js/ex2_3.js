function mostrar (){
    var veiculores = document.getElementById("veiculo").value;
    var preçores = Number(document.getElementById("preço").value);
    var entrada = Math.floor(preçores / 2) 
    var parcela = Math.floor(entrada / 12)

    veiculoresp.textContent = "Promoção: " + veiculores
    entra.textContent = "Entrada de R$: " + entrada.toFixed(2)
    parc.textContent = "+ 12x de R$: " + parcela.toFixed(2)

}

var botao = document.querySelector("input[type = 'button']")
botao.addEventListener("click", mostrar)