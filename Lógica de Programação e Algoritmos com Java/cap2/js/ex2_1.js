// Declara a função mostrarOla
function mostrarOla() {
    // Obtém o conteúdo do campo com id="nome"
    var nome = document.getElementById("nome").value;

    // Exibe no parágrafo (resposta): "Olá" e o nome informado
    document.getElementById("resposta").textContent = "Olá, " + nome;
}

// Cria uma referência ao botão (selecionado corretamente pelo tipo de input)
var botaoMostrar = document.querySelector("input[type='button']");

// Registra o evento de clique no botão para chamar a função mostrarOla
botaoMostrar.addEventListener("click", mostrarOla);
