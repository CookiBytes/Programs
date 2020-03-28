// Change let role to moderator, you'll get the message, Moderator User
// And the same if you let the role go undefined.
let role = "guest";

switch (role) {
  case "guest":
    console.log("Guest User");
    break;

  case "moderator":
    console.log("Moderator User");
    break;

  default:
    console.log("Unknown User");
}
