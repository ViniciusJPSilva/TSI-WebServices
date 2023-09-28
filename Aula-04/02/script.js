
const result_div = document.querySelector("#result");

function createRequest() {
    let uf = document.querySelector("#uf").value;
    let city = document.querySelector("#city").value;
    let street = document.querySelector("#street").value.replaceAll(" ", "+");

    let req = new XMLHttpRequest();
    result_div.innerHTML = "";

    req.onload = function() {
        resp = req.responseText;
        resp_obj = JSON.parse(resp);
        
        if(resp_obj.length == 0)
            result_div.appendChild(document.createElement('h4')).innerHTML = "Nenhum resultado encontrado!";
        else
            createTable(resp_obj, result_div)
    }

    req.onerror = function () {
        msg = document.createElement('h4');
        msg.classList.add('msg_error');
        result_div.appendChild(msg).innerHTML = "Ocorreu um erro! Verifique os dados e tente novamente.";
    }

    req.open("GET", `https://viacep.com.br/ws/${uf}/${city}/${street}/json`);
    req.send(null);
}

function createTable(data, container) {
    let table = document.createElement('table');
    table.setAttribute("border", "1");

    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');

    table.appendChild(thead);
    table.appendChild(tbody);

    let headers = ['CEP', 'Rua', 'Bairro', 'Cidade/Estado'];
    let headerRow = document.createElement('tr');
    for (let i = 0; i < headers.length; i++) 
        headerRow.appendChild(document.createElement('th')).innerHTML = headers[i];
    
    thead.appendChild(headerRow);

    resp_obj.forEach(d => {
        let row = document.createElement('tr');
        
        row.appendChild(document.createElement('td')).innerHTML = d.cep;
        row.appendChild(document.createElement('td')).innerHTML = d.logradouro;
        row.appendChild(document.createElement('td')).innerHTML = d.bairro;
        row.appendChild(document.createElement('td')).innerHTML = `${d.localidade}/${d.uf}`;
        
        tbody.appendChild(row);
    });
      

    result_div.append(table);
}

// alert(`O cep ${resp_obj.cep} pertence à rua ${resp_obj.logradouro} do bairro ${resp_obj.bairro}, ${resp_obj.localidade} / ${resp_obj.uf}`);