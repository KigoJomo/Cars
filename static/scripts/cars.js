const cars = document.querySelectorAll(".box");
const sections = document.querySelectorAll("section");
const searchForm = document.getElementById("searchForm");

searchForm.addEventListener("submit", function (event) {
  event.preventDefault();
  console.log("submitted");

  const searchInput = document.querySelector("#searchForm input").value;
  if (searchInput.trim() !== "") {
    search(searchInput);
  }
});

function search(query) {
  fetch(`/search/?query=${query}`)
    .then((response) => response.json())
    .then((data) => {
      // console.table(data);
      sections.forEach((section) => {
        section.style.display = "none";
      });
      const boxes = document.querySelectorAll(".box");
      boxes.forEach((box) => {
        box.style.display = "none";
      });

      data.forEach((carItem) => {
        const car = document.createElement("div");
        car.classList.add("box");
        const carName = document.createElement("h2");
        carName.innerText = carItem.name;
        const carMake = document.createElement("h3");
        carMake.innerText = carItem.make;
        const carModel = document.createElement("h4");
        carModel.innerText = carItem.model;
        const image = document.createElement("img");
        image.setAttribute("src", carItem.image);
        const price = document.createElement("p");
        price.innerText = carItem.price;
        const trimLevel = document.createElement("p");
        trimLevel.innerText = carItem.trimlevel;
        const yearMfct = document.createElement("p");
        yearMfct.innerText = carItem.yearMfct;

        const details = [
          carName,
          carMake,
          carModel,
          image,
          price,
          trimLevel,
          yearMfct,
        ];
        details.forEach((detailsItem) => {
          car.appendChild(detailsItem);
        });
        document.body.appendChild(car);
      });
    });
}
