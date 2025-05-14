function mostrar(){
    var prod = document.getElementById('produto').value;
    var preco = Number(document.getElementById('valor').value);
    var promocao = Number(Math.floor(preco / 2));
    var leve = Number((preco * 2) + promocao);

    resultado.textContent = prod + " - Promoção: Leve 3 por R$: " + leve;
    resul.textContent = "O 3° produto custa apenas R$: " + promocao;
}

var botao = document.querySelector("input[type='button']");
botao.addEventListener("click", mostrar);
