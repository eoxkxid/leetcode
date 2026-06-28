func findAnagrams(s string, p string) []int {
    result := []int{}

    if len(p) > len(s) {
        return result
    }

    var pCount [26]int
    var windowCount [26]int

    // p의 문자 빈도 계산
    for i := 0; i < len(p); i++ {
        index := int(p[i] - 'a')
        pCount[index]++
    }

    left := 0
    pLen := len(p)

    for right := 0; right < len(s); right++ {
        // 오른쪽 문자 추가
        rightIndex := int(s[right] - 'a')
        windowCount[rightIndex]++

        // 윈도우 크기가 pLen보다 커지면 왼쪽 문자 제거
        if right-left+1 > pLen {
            leftIndex := int(s[left] - 'a')
            windowCount[leftIndex]--
            left++
        }

        // 윈도우 크기가 pLen이고 문자 빈도가 같으면 애너그램
        if right-left+1 == pLen && windowCount == pCount {
            result = append(result, left)
        }
    }

    return result
}