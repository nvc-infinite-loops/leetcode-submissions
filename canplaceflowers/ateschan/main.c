#include <stdbool.h>

bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {

  //Fucking ridiculous edge cases
  if (n == 0) {
    return true;
  }

  if (flowerbedSize == 1) {
    if (flowerbed[0] == 0) {
        return true;
    }
    else {
        return false;
    }
  }

  int ncp = n;
  for (int i = 0; i < flowerbedSize; i++) {
    if (flowerbed[i] == 0) {
      //case ahead and behind
      if ((i - 1 >= 0) && (i + 1 < flowerbedSize)) {
        if ((flowerbed[i - 1] != 1) && (flowerbed[i + 1] != 1)) {
          flowerbed[i] = 1;
          ncp = ncp - 1;
        }
      }
      //case ahead
      else if (i == 0) {
        if ((flowerbed[i + 1] != 1)) {
          flowerbed[i] = 1;
          ncp = ncp - 1;
        }
      }
      //case behind
      else if (i == flowerbedSize - 1) {
        if (flowerbed[i - 1] != 1) {
          flowerbed[i] = 1;
          ncp = ncp - 1;
        }
      }
    }
  }
  if (ncp > 0) {
    return false;
  }
  return true;
}
