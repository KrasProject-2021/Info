import requests,os

os.system('clear')

while True:
	print()
	link = input("Введите конкретную ссылку : ")
	print()
	print(F"Поиск информации из сайта : {link}")
	g = requests.get(F"{link}").text
	print()
	print(F"{g}")
	print()
	filename = input("Чтобы сохранить код ведите название файла : ")
	file = open(F"{filename}.txt", "w")
	file.write(F"{g}")
	os.system('clear')
input
