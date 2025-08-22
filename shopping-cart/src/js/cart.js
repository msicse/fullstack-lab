let cart = JSON.parse(localStorage.getItem("cart")) || [];
let discount = 0;

const coupons = [
  { code: "SAVE10", percentage: 10 },
  { code: "SALE20", percentage: 20 },
];

function saveCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
}

function addToCart(productId) {
  const product = products.find((p) => p.id === productId);
  const existingItem = cart.find((item) => item.id === productId);

  if (existingItem) {
    existingItem.quantity += 1;
  } else {
    cart.push({ ...product, quantity: 1 });
  }

  saveCart();
  updateCartUI();
  document.getElementById("cart-panel").classList.remove("translate-x-full");
}

function removeFromCart(productId) {
  cart = cart.filter((item) => item.id !== productId);
  saveCart();
  updateCartUI();
}

function updateQuantity(productId, change) {
  const item = cart.find((item) => item.id === productId);
  if (item) {
    item.quantity += change;
    if (item.quantity < 1) {
      removeFromCart(productId);
    } else {
      saveCart();
      updateCartUI();
    }
  }
}

function updateCartUI() {
  const cartItems = document.getElementById("cart-items");
  const cartCount = document.querySelector("#cart-open span");

  cartCount.textContent = cart.reduce(
    (total, item) => total + item.quantity,
    0
  );

  cartItems.innerHTML = cart
    .map(
      (item) => `
        <div class="flex gap-2 items-start mb-2 border-b pb-2">
            <img src="${item.image}" alt="${
        item.name
      }" class="w-16 h-16 object-cover rounded-md">
            <div class="flex-grow">
                <div class="flex justify-between items-start">
                    <div>
                        <h4 class="font-bold text-xs">${item.name}</h4>
                        <p class="text-gray-600 text-xs">$${item.price}</p>
                    </div>
                    <button onclick="removeFromCart(${
                      item.id
                    })" class="text-red-500 hover:text-red-700">
                        <i class="fa-solid fa-times text-xs"></i>
                    </button>
                </div>
                <div class="flex items-center space-x-2 mt-1">
                    <button onclick="updateQuantity(${
                      item.id
                    }, -1)" class="bg-gray-200 px-2 py-0.5 rounded text-xs">${item.quantity > 1 ? "-" : '<i class="fa-solid fa-trash-can"></i>'}</button>
                    <span class="text-xs">${item.quantity}</span>
                    <button onclick="updateQuantity(${
                      item.id
                    }, 1)" class="bg-gray-200 px-2 py-0.5 rounded text-xs">+</button>
                </div>
            </div>
        </div>
    `
    )
    .join("");

  // Update totals
  const subtotal = cart.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );
  const discountAmount = (subtotal * discount) / 100;
  const total = subtotal - discountAmount;

  document.getElementById("cart-subtotal").textContent = `$${subtotal.toFixed(
    2
  )}`;
  document.getElementById("cart-discount").textContent = `-$${discountAmount.toFixed(2)}`;
  document.getElementById("cart-total").textContent = `$${total.toFixed(2)}`;
}

// Cart panel toggle
document.getElementById("cart-open").addEventListener("click", () => {
  document.getElementById("cart-panel").classList.remove("translate-x-full");
});

document.getElementById("cart-close").addEventListener("click", () => {
  document.getElementById("cart-panel").classList.add("translate-x-full");
});

// Clear cart
document.getElementById("clear-cart").addEventListener("click", () => {
  cart = [];
  discount = 0;
  saveCart();
  updateCartUI();
});

// Apply Coupon
document.getElementById("apply-coupon").addEventListener("click", () => {
  const couponInput = document.getElementById("coupon-input");
  const couponMessage = document.getElementById("coupon-message");
  const coupon = coupons.find((c) => c.code === couponInput.value);

  if (coupon) {
    discount = coupon.percentage;
    couponMessage.textContent = `Coupon "${coupon.code}" applied!`;
    couponMessage.classList.add("text-green-500");
    couponMessage.classList.remove("text-red-500");
  } else {
    discount = 0;
    couponMessage.textContent = "Invalid coupon code";
    couponMessage.classList.add("text-red-500");
    couponMessage.classList.remove("text-green-500");
  }

  updateCartUI();
});


// Clear cart
document.getElementById("checkout").addEventListener("click", () => {
  if (cart.length > 0) {
    alert("Checkout Successfull!! Thanks");
    cart = [];
    discount = 0;
    saveCart();
    updateCartUI();
  } else {
     alert("Please add Item To Cart !!");
  }
});

// Initial cart render
document.addEventListener("DOMContentLoaded", updateCartUI);