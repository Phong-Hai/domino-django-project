let cartInitialized = false;

document.addEventListener('DOMContentLoaded', () => {
    if (cartInitialized) return;
    cartInitialized = true;

    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    updateCartCount();

    if (window.location.pathname.includes('cart.html')) {
        displayCartItems();
    }

    setupCartButtons();
});

function setupCartButtons() {
    document.querySelectorAll('.add-to-cart, .addToCart').forEach(button => {
        const newButton = button.cloneNode(true);
        button.parentNode.replaceChild(newButton, button);
    });

    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const id = button.dataset.id;
            const name = button.dataset.name;
            const price = parseFloat(button.dataset.price);

            addToCart(id, name, price);
        });
    });

    document.querySelectorAll('.addToCart').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();

            const menuItem = button.closest('.menu');
            const infoText = menuItem.querySelector('.info_bar p').innerHTML;

            const lines = infoText.split('<br>');
            const name = lines[0].replace('<b>', '').replace('</b>', '');
            const priceText = lines[1];
            const price = parseFloat(priceText.match(/[\d.]+/)[0]);

            const id = name.toLowerCase().replace(/\s+/g, '-');

            addToCart(id, name, price);
        });
    });
}

function addToCart(id, name, price) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    const menuItem = document.querySelector(`[data-id="${id}"]`)?.closest('.menu');
    const imgElement = menuItem?.querySelector('img');
    const imgSrc = imgElement ? imgElement.getAttribute('src') : '';

    const existingItem = cart.find(item => item.id === id);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            id: id,
            name: name,
            price: price,
            quantity: 1,
            image: imgSrc
        });
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    showAddToCartMessage(name);
}

function updateCartCount() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const count = cart.reduce((sum, item) => sum + item.quantity, 0);
    const counter = document.getElementById('numberItemInCart');
    if (counter) {
        counter.textContent = count;
    }
}

function displayCartItems() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const bodyContainer = document.querySelector('.body_container');

    if (cart.length === 0) {
        bodyContainer.innerHTML = `
            <div class="empty-cart">
                <h2>Your cart is empty</h2>
                <p>Add some delicious items to get started!</p>
                <a href="menu.html"><button class="start-order-btn">Start Order Here</button></a>
            </div>
        `;
        return;
    }

    const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
    let cartHTML = `
        <div class="cart-container">
            <h1>Your Cart</h1>
            <div class="cart-items">
    `;

    cart.forEach(item => {
        cartHTML += `
            <div class="cart-item" data-id="${item.id}" style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
                <div class="item-image">
                    <img src="${item.image}" alt="${item.name}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 8px;">
                </div>
                <div class="item-info" style="flex-grow: 1;">
                    <h3>${item.name}</h3>
                    <p class="item-price">$${item.price.toFixed(2)} each</p>
                    <div class="item-controls" style="margin-top: 10px;">
                        <button class="quantity-btn minus" onclick="updateQuantity('${item.id}', -1)">-</button>
                        <span class="quantity">${item.quantity}</span>
                        <button class="quantity-btn plus" onclick="updateQuantity('${item.id}', 1)">+</button>
                        <button class="remove-btn" onclick="removeFromCart('${item.id}')">Remove</button>
                    </div>
                </div>
                <div class="item-total" style="font-weight: bold;">
                    $${(item.price * item.quantity).toFixed(2)}
                </div>
            </div>
        `;
    });

    cartHTML += `
            </div>
            <div class="cart-summary">
                <div class="total-section">
                    <h2>Total: $${total.toFixed(2)}</h2>
                    <div class="cart-actions">
                        <button class="continue-shopping" onclick="window.location.href='menu.html'">Continue Shopping</button>
                        <button class="checkout-btn" onclick="checkout()">Proceed to Checkout</button>
                        <button class="clear-cart-btn" onclick="clearCart()">Clear Cart</button>
                    </div>
                </div>
            </div>
        </div>
    `;

    bodyContainer.innerHTML = cartHTML;
}

function updateQuantity(id, change) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    const item = cart.find(item => item.id === id);

    if (item) {
        item.quantity += change;

        if (item.quantity <= 0) {
            cart = cart.filter(item => item.id !== id);
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartCount();
        displayCartItems();
    }
}

function removeFromCart(id) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart = cart.filter(item => item.id !== id);

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    displayCartItems();
}

function clearCart() {
    if (confirm('Are you sure you want to clear your cart?')) {
        localStorage.removeItem('cart');
        updateCartCount();
        displayCartItems();
    }
}

function showAddToCartMessage(itemName) {
    let notification = document.getElementById('cart-notification');
    if (!notification) {
        notification = document.createElement('div');
        notification.id = 'cart-notification';
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #28a745;
            color: white;
            padding: 15px 20px;
            border-radius: 5px;
            z-index: 1000;
            font-weight: bold;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            transform: translateX(100%);
            transition: transform 0.3s ease;
        `;
        document.body.appendChild(notification);
    }

    notification.textContent = `${itemName} added to cart!`;
    notification.style.transform = 'translateX(0)';

    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
    }, 3000);
}

function checkout() {
    // alert('Checkout functionality would be implemented here!\nTotal items: ' +
    //     JSON.parse(localStorage.getItem('cart')).reduce((sum, item) => sum + item.quantity, 0));
    generatePrintableOrder(); // Call the new function
}

function getCart() {
    return JSON.parse(localStorage.getItem('cart')) || [];
}

function getCartTotal() {
    const cart = getCart();
    return cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
}

function getCartItemCount() {
    const cart = getCart();
    return cart.reduce((sum, item) => sum + item.quantity, 0);
}


// New function to generate printable order
function generatePrintableOrder() {
    const cart = getCart();
    const total = getCartTotal();

    if (cart.length === 0) {
        alert("Your cart is empty. Please add items before checking out.");
        return;
    }

    let printContent = `
        <!DOCTYPE html>
        <html>
        <head>
            <title>Domino's Pizza - Order Receipt</title>
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; color: #333; }
                .receipt-header { text-align: center; margin-bottom: 30px; }
                .receipt-header img { width: 100px; margin-bottom: 10px; }
                .receipt-header h1 { color: #0b648f; margin: 0; font-size: 28px; }
                .receipt-header p { font-size: 14px; color: #555; }
                table { width: 100%; border-collapse: collapse; margin-bottom: 30px; }
                th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
                th { background-color: #f2f2f2; color: #0b648f; }
                .total-row td { font-weight: bold; font-size: 18px; background-color: #e6f7ff; }
                .thank-you { text-align: center; margin-top: 40px; font-size: 16px; color: #0b648f; }
                .note { font-size: 12px; color: #777; text-align: center; margin-top: 10px; }

                @media print {
                    body { -webkit-print-color-adjust: exact; }
                    .receipt-header h1 { color: #0b648f !important; }
                    th { background-color: #f2f2f2 !important; color: #0b648f !important; }
                    .total-row td { background-color: #e6f7ff !important; }
                }
            </style>
        </head>
        <body>
            <div class="receipt-header">
                <img src="image/domino_logo.png" alt="Domino's Logo">
                <h1>Order Receipt</h1>
                <p>Thank you for your order!</p>
                <p>Order Date: ${new Date().toLocaleDateString()}</p>
                <p>Order Time: ${new Date().toLocaleTimeString()}</p>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Item</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Subtotal</th>
                    </tr>
                </thead>
                <tbody>
    `;

    cart.forEach(item => {
        printContent += `
            <tr>
                <td>${item.name}</td>
                <td>$${item.price.toFixed(2)}</td>
                <td>${item.quantity}</td>
                <td>$${(item.price * item.quantity).toFixed(2)}</td>
            </tr>
        `;
    });

    printContent += `
                    <tr class="total-row">
                        <td colspan="3">Total</td>
                        <td>$${total.toFixed(2)}</td>
                    </tr>
                </tbody>
            </table>
            <div class="thank-you">
                We appreciate your business. Enjoy your meal!
            </div>
            <div class="note">
                This is an automated receipt. For any inquiries, please contact us.
            </div>
        </body>
        </html>
    `;

    const printWindow = window.open('', '_blank');
    printWindow.document.write(printContent);
    printWindow.document.close();
    printWindow.focus();
    printWindow.print();
}