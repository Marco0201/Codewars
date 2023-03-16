// Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

// Example:

// "riley" --> "Hello Riley!"
// "JACK"  --> "Hello Jack!"

var greet = function(name) {
  let n = name.toLowerCase()
  let rest = n.slice(1)
  return 'Hello' + ' ' + n.charAt(0).toUpperCase() + rest + '!'
};