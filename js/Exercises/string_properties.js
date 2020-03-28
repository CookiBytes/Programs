const movie = {
  title: "The Last Jedi",
  releaseYear: 2018,
  rating: 4.5,
  director: "Peppa Pig"
};

showProperties(movie);

function showProperties(obj) {
  for (let key in obj) {
    if (typeof obj[key] === "string") {
      console.log(key, obj[key]);
    }
  }
}
