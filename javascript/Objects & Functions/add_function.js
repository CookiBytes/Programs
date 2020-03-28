// Add a Function in a Object
const circle = {
  radius: 1,
  location: {
    x: 1,
    y: 1
  },
  isVisible: true,
  // Function:
  draw: function() {
    console.log("draw");
  }
};

// Call a function in a object
circle.draw();
