// Write function bmi that calculates body mass index (bmi = weight / height2).

// if bmi <= 18.5 return "Underweight"

// if bmi <= 25.0 return "Normal"

// if bmi <= 30.0 return "Overweight"

// if bmi > 30 return "Obese"

function bmi(w, h) {
  let B = w / (h**2)
  if (B <= 18.5) {
    return "Underweight"
  } else if (B > 18.5 && B <= 25){
    return "Normal"
  } else if (B > 25 && B <= 30){
    return "Overweight"
  } else if (B > 30){
    return "Obese"
  } 
}