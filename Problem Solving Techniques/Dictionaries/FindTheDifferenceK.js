function twoIntDiff(arr, k) {
  // Brute Force solution :
  // foreach element i will "search" for the second element that matches the cond "n+2 = m"
  // does this arr sorted  ?  this will speed up the search for "m" if a BinarySearch
  // duplicates ??? n = 2,2   m= 4   k=2 , will I count 2,2 as two elements ?? yes : HashTable
  // am I supposed the the minus values ? or all n values are > 0 ?

  let set = new Set();
  for (let i = 0; i < arr.length; i++) {
    // O(N)
    if (!set.has(arr[i])) set.add(arr[i]);
  }

  // A set is used for speed lockup, instead of using BinarySearch !
  let arrTwoDiff = new Set();
  for (let i = 0; i < arr.length; i++) {
    let target = -1;
    if (set.has(k - arr[i])) {
      target = k - arr[i];
    }
    if (target != -1) {
      arrTwoDiff.add(arr[i]);
      arrTwoDiff.add(target);
    }
  }
  return arrTwoDiff;
}


let arr = [1, 5, 10, 2, 3, 4, 5, 6, 8];

console.log(twoIntDiff(arr, 11))  // { 1, 10, 5, 6, 3, 8 }