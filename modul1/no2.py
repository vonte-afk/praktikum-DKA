# input suhu
celsius = float(input("Masukkan suhu dalam Celsius: "))

# konversi
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# output
print(format (celsius), "°C =", format(fahrenheit), "°F =", format(kelvin), "°K")