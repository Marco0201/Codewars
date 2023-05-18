// Write a function which calculates the average of the numbers in a given list.

// Note: Empty arrays should return 0.

function findAverage(arr) {
    let sum = 0
    if (arr.length !== 0) {
      for ( let i = 0; i < arr.length; i++){
        sum += arr[i]
      }
      return sum/(arr.length)
    } else {
      return 0
    }
  }