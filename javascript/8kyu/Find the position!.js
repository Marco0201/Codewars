// When provided with a letter, return its position in the alphabet.

// Input :: "a"

// Ouput :: "Position of alphabet: 1"
function position(l){
    let alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    // let i = alph.indexOf(l)
    return `Position of alphabet: ${alph.indexOf(l)}`
  }