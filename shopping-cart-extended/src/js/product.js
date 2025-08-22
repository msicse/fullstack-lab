const products = [
  {
    id: 1,
    name: "Wireless Headphones",
    price: 99.99,
    description: "High-quality wireless headphones with noise cancellation",
    image:
      "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&w=400",
  },
  {
    id: 2,
    name: "Smartphone",
    price: 699.99,
    description: "Latest model smartphone with advanced features",
    image:
      "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?auto=format&w=400",
  },
  {
    id: 3,
    name: "Laptop",
    price: 999.99,
    description: "Powerful laptop for work and gaming",
    image:
      "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&w=400",
  },
  {
    id: 4,
    name: "Smart Watch",
    price: 199.99,
    description: "Fitness tracking and notifications on your wrist",
    image:
      "https://images.unsplash.com/photo-1546868871-7041f2a55e12?auto=format&w=400",
  },
  {
    id: 5,
    name: "Wireless Earbuds",
    price: 149.99,
    description: "True wireless earbuds with premium sound quality",
    image:
      "src/images/earbuds.jpg",
  },
  {
    id: 6,
    name: "Gaming Console",
    price: 499.99,
    description: "Next-gen gaming console for immersive gameplay",
    image:
      "https://images.unsplash.com/photo-1486401899868-0e435ed85128?auto=format&w=400",
  },
  {
    id: 7,
    name: "Tablet",
    price: 399.99,
    description: "Versatile tablet for work and entertainment",
    image:
      "https://images.unsplash.com/photo-1561154464-82e9adf32764?auto=format&w=400",
  },
  {
    id: 8,
    name: "Bluetooth Speaker",
    price: 79.99,
    description: "Portable speaker with rich, room-filling sound",
    image:
      "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&w=400",
  },
  {
    id: 9,
    name: "Digital Camera",
    price: 799.99,
    description: "Professional-grade camera for stunning photos",
    image:
      "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&w=400",
  },
];



function displayProducts(view = 'grid') {
  productsContainer = document.querySelector("#products");
  productsContainer.innerHTML = "";

  // Update container classes based on view
  productsContainer.className = view === 'grid' 
    ? 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 md:gap-6'
    : 'flex flex-col gap-4';

  for (const product of products) {
    let productItem = "";

    if (view === "grid") {
      productItem = `<div
            class="bg-white rounded-md shadow-md h-full py-3 px-4 md:p-4 flex flex-col"
          >
            <img
              src="${product.image}"
              alt="${product.name}"
              class="w-full h-36 md:h-48 object-cover rounded-md"
            />
            <h3 class="text-lg md:text-xl font-bold mt-2">${product.name}</h3>
            <p class="text-gray-600 text-sm md:text-base mt-2 flex-grow">
              ${product.description}
            </p>
            <div class="mt-3 md:mt-4">
              <span class="font-bold block mb-2">$${product.price}</span>
              <button
                onclick="addToCart(${product.id})"
                class="w-full bg-indigo-900 py-1.5 md:py-2 px-4 rounded-md hover:bg-indigo-800 text-white text-sm md:text-base"
              >
                Add to Cart
              </button>
            </div>
          </div> `;
    }

    if (view === "list") {
      productItem = `<div
            class="bg-white rounded-md shadow-md w-full p-4 flex flex-col md:flex-row gap-4"
          >
            <img
              src="${product.image}"
              alt="${product.name}"
              class="w-full md:w-48 h-48 object-cover rounded-md"
            />
            <div class="flex flex-col flex-grow">
              <h3 class="text-xl font-bold">${product.name}</h3>
              <p class="text-gray-600 mt-2 flex-grow">
                ${product.description}
              </p>
              <div class="flex items-center justify-between mt-4">
                <span class="font-bold text-xl">$${product.price}</span>
                <button
                  onclick="addToCart(${product.id})"
                  class="bg-indigo-900 py-2 px-6 rounded-md hover:bg-indigo-800 text-white"
                >
                  Add to Cart
                </button>
              </div>
            </div>
          </div>`;
    }

    productsContainer.innerHTML += productItem;
  }
}

function setActiveView(view) {
  const gridBtn = document.querySelector('#grid-view');
  const listBtn = document.querySelector('#list-view');
  
  if (view === 'grid') {
    gridBtn.classList.add('text-indigo-800');
    listBtn.classList.remove('text-indigo-800');
  } else {
    listBtn.classList.add('text-indigo-800');
    gridBtn.classList.remove('text-indigo-800');
  }
}
