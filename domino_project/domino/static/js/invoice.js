document.addEventListener("DOMContentLoaded", () => {
    const invoiceData = JSON.parse(localStorage.getItem("invoiceData"));
    if (!invoiceData) return;

    // Fill text info
    document.getElementById("customerName").textContent = invoiceData.customer_name || "Customer";
    document.getElementById("orderNumber").textContent = invoiceData.orderId || "N/A";
    document.getElementById("orderDate").textContent = invoiceData.date || "";
    document.getElementById("billingInfo").innerHTML = invoiceData.address || "";
    document.getElementById("paymentMethod").textContent = invoiceData.payment_method || "";

    // Fill table
    const tbody = document.getElementById("invoiceItems");
    let subtotal = 0;
    invoiceData.cart.forEach(item => {
        const tr = document.createElement("tr");
        const total = (item.price * item.quantity).toFixed(2);
        subtotal += parseFloat(total);
        tr.innerHTML = `
          <td>${item.name}</td>
          <td>${item.id || '-'}</td>
          <td style="text-align:center;">${item.quantity}</td>
          <td style="text-align:right;">$${total}</td>
        `;
        tbody.appendChild(tr);
    });

    const tax = subtotal * 0.1;
    const grandTotal = subtotal + tax;
    document.getElementById("subtotal").textContent = "$" + subtotal.toFixed(2);
    document.getElementById("tax").textContent = "$" + tax.toFixed(2);
    document.getElementById("grandTotal").textContent = "$" + grandTotal.toFixed(2);

    // Print button
    document.getElementById("printInvoice").addEventListener("click", () => window.print());
});
