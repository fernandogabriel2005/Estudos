function mostrar(){

    var nomee = document.getElementById("nome").value;

    var umnota = parseFloat(document.getElementById('notaum').value);

    var doisnota = parseFloat(document.getElementById('notadois').value);

    var medianmo = (umnota + doisnota) / 2;



    medianotas.textContent = "Média DE NOTAS: " + medianmo;

    if(medianmo >= 5){
        resultado.textContent = "Parabéns " + nomee + ", você foi aprovado!";
        resultado.style.color = "blue";
    } else{
        resultado.textContent = "Infelizmente " + nomee + ", suas notas foram abaixo da média, e por consequência está reprovado.";
        resultado.style.color = "red" ;
    }
}

var botao = document.querySelector("input[type = 'button']")
botao.addEventListener("click", mostrar)

