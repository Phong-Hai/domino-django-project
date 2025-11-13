(() => {
  const CART_KEY = 'cart';

  const getCart = () => {
    try {
      return JSON.parse(localStorage.getItem(CART_KEY)) || [];
    } catch {
      return [];
    }
  };

  const saveCart = (cart) => localStorage.setItem(CART_KEY, JSON.stringify(cart));
  const clearCart = () => localStorage.removeItem(CART_KEY);

  const updateBadge = () => {
    const cart = getCart();
    const badge = document.getElementById('numberItemInCart');
    if (badge) badge.textContent = cart.length;
  };

  const renderCart = () => {
    const container = document.getElementById('cartContainer');
    if (!container) return;

    const cart = getCart();

    if (cart.length === 0) {
      container.innerHTML = `
        <div style="text-align:center; margin-top:60px;">
          <h2>Your cart is empty</h2>
          <a href="/menu">
            <button style="margin-top:20px; padding:10px 25px; background:#003366; color:#fff; border:none; border-radius:8px; cursor:pointer;">
              Start Order Here
            </button>
          </a>
        </div>`;
      updateBadge();
      return;
    }

    let html = `
      <table style="width:90%; margin:30px auto; border-collapse:collapse;">
        <tr style="background:#003366; color:white;">
          <th style="padding:15px;">Item</th>
          <th style="padding:15px;">Price</th>
          <th style="padding:15px;">Qty</th>
          <th style="padding:15px;">Total</th>
          <th style="padding:15px;">Action</th>
        </tr>`;

    let grandTotal = 0;
    cart.forEach((item, i) => {
      const total = (item.price || 0) * (item.quantity || 0);
      grandTotal += total;
      html += `
        <tr style="border-bottom:1px solid #ddd; text-align:center;">
          <td style="padding:12px;">${item.name}</td>
          <td>$${item.price.toFixed(2)}</td>
          <td>
            <button onclick="changeQty(${i}, -1)" style="width:30px;">-</button>
            ${item.quantity}
            <button onclick="changeQty(${i}, 1)" style="width:30px;">+</button>
          </td>
          <td>$${total.toFixed(2)}</td>
          <td>
            <span onclick="removeItem(${i})" style="color:red; cursor:pointer;">Remove</span>
          </td>
        </tr>`;
    });

    html += `
      </table>
      <div style="text-align:right; font-size:1.4em; margin:20px 5%;">
        <strong>Total: $${grandTotal.toFixed(2)}</strong>
      </div>
      <div style="text-align:right; margin:20px 5%;">
        <button id="checkoutBtn" 
          style="padding:10px 25px; background:#28a745; color:#fff; border:none; border-radius:8px; cursor:pointer;">
          Process Checkout
        </button>
      </div>`;

    container.innerHTML = html;

    const checkoutBtn = document.getElementById('checkoutBtn');
    if (checkoutBtn) checkoutBtn.addEventListener('click', handleCheckout);

    updateBadge();
  };

  // --- Quantity Change ---
  window.changeQty = (i, delta) => {
    const cart = getCart();
    if (!cart[i]) return;
    cart[i].quantity += delta;
    if (cart[i].quantity <= 0) cart.splice(i, 1);
    saveCart(cart);
    updateBadge();
    renderCart();
  };

  // --- Remove Item ---
  window.removeItem = (i) => {
    const cart = getCart();
    cart.splice(i, 1);
    saveCart(cart);
    updateBadge();
    renderCart();
  };

  // --- Checkout + Print Invoice ---
  const handleCheckout = () => {
    const cart = getCart();
    if (cart.length === 0) return;

    const confirmed = confirm("Proceed to checkout and print your invoice?");
    if (!confirmed) return;

    const orderId = Math.floor(Math.random() * 900000 + 100000);
    const date = new Date();

    const invoiceData = {
      orderId,
      date: date.toLocaleDateString(),
      time: date.toLocaleTimeString(),
      cart,
      total: cart.reduce((sum, i) => sum + i.price * i.quantity, 0).toFixed(2),
    };

    localStorage.setItem("invoiceData", JSON.stringify(invoiceData));
    clearCart();

    window.location.href = "/invoice/";
  };

  document.addEventListener('DOMContentLoaded', () => {
    updateBadge();
    renderCart();
  });
})();
