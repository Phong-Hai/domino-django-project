var amount_of_product = 1;
function addproduct(){    
    const change_amount = document.getElementById("numberItemInCart");
    change_amount.innerText = amount_of_product;
    amount_of_product++;
}