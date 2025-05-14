function mostrar(){
    var remedio = document.getElementById('medicamento').value;
    var custo = Number(document.getElementById('valor').value);
    var promoc = Math.floor(custo * 2)

    resppromo.textContent = "Promoção de " + remedio
    doispor.textContent = "Leve 2 por apenas R$:" + promoc.toFixed(2)
}

var botao = document.querySelector("input[type='button']")
botao.addEventListener("click", mostrar)