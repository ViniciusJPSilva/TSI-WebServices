
const result_div = document.querySelector("#result");

let cep = prompt("Forneça o CEP (somente os números): ");

let req = new XMLHttpRequest();

req.onload = function() {
    resp = req.responseText;
    resp_obj = JSON.parse(resp);
    
    if(resp_obj.length == 0)
        alert("Nenhum resultado encontrado!");
    else
        alert(`O cep ${resp_obj.cep} pertence à rua ${resp_obj.logradouro} do bairro ${resp_obj.bairro}, ${resp_obj.localidade} / ${resp_obj.uf}`);
}

req.onerror = function () {
    alert("Ocorreu um erro! Verifique os dados e tente novamente.");
}

req.open("GET", `https://viacep.com.br/ws/${cep}/json`);
req.send(null);
