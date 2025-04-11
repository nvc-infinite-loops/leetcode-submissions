func canPlaceFlowers(flowerbed []int, n int) bool {
	bedlength := len(flowerbed);
	if bedlength == 1 {
		if (n == 1 && flowerbed[0] == 0) || n == 0 {
			return true;
		}
		return false;
	}
    
	for i := 0; i < bedlength; i++ {
        leftcheck := i == 0 || flowerbed[i - 1] == 0;
        rightcheck := i == bedlength - 1 || flowerbed[i + 1] == 0;

        if leftcheck && rightcheck && flowerbed[i] == 0{
            flowerbed[i] = 1;
            n -= 1;
		}
	}

	if n > 0 {
		return false;
	}
	return true;
}
