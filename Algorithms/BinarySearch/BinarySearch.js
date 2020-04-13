// left = 0
// right = arr.length -1
// Array must be SORTED !
function binarySearch(el, arr, left, right) {
  // what if passing the element and not found ?  the arr will be shrinked to 0 elements
  // in other words {right = arr.length-1 = -1}  , {left = 0}
  if (right < left) return -1;

  let mid = Math.floor((left + right) / 2);
  if (arr[mid] === el) return el; // my base condition
  if (el < arr[mid]) {
    return binarySearch(el, arr, left, mid - 1);
  }
  return binarySearch(el, arr, mid + 1, right);

  // o(logN)
}


console.log(binarySearch(6, [1,2,3,4,5], 0, 5))