def romanToInt(s: str) -> int:
    # Tạo từ điển ánh xạ chữ số La Mã sang giá trị tương ứng
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    # Duyệt qua chuỗi chữ số La Mã từ trái sang phải
    for i in range(len(s) - 1):
        # Nếu giá trị của chữ số tiếp theo lớn hơn giá trị của chữ số hiện tại
        if roman_map[s[i]] < roman_map[s[i+1]]:
            result -= roman_map[s[i]]
        else:
            result += roman_map[s[i]]
    
    # Cộng giá trị của chữ số cuối cùng vào kết quả cuối cùng 
    result += roman_map[s[-1]]
    
    return result

# Test
print(romanToInt("III"))     # Output: 3
print(romanToInt("LVIII"))   # Output: 58
print(romanToInt("MCMXCIV")) # Output: 1994
        