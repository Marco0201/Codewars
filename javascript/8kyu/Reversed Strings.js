// Complete the solution so that it reverses the string passed into it.

// 'world'  =>  'dlrow'
// 'word'   =>  'drow'

function solution(str){
  let newlist = str.split("")
  let total = []
  for(let i = (newlist.length - 1); i >= 0; i--) {
    total.push(newlist[i])
  }
  return total.join("")
}