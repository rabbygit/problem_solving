func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	charMap := make(map[byte]int)

	for i := 0; i < len(s); i++ {
		char := s[i]
		charMap[char]++
	}

	for i := 0; i < len(t); i++ {
		char := t[i]
		count, exists := charMap[char]
		if !exists || count <= 0 {
			return false
		}
		charMap[char]--
	}

	return true
}