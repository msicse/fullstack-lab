document.addEventListener("DOMContentLoaded", (e) => {
	const cartPanel = document.querySelector("#cart-panel");

  displayProducts("grid");
  setActiveView("grid");

  document.querySelector("#grid-view").addEventListener("click", () => {
    displayProducts("grid");
    setActiveView("grid");
  });

  document.querySelector("#list-view").addEventListener("click", () => {
    displayProducts("list");
    setActiveView("list");
  });

});
